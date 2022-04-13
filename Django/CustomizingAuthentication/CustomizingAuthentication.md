# CustomizingAuthentication

> Customizing authentication in Django

## Substituting a custom User model

#### User 모델 대체하기

- 일부 프로젝트에서는 Django의 내장 User 모델이 제공하는 인증 요구사항이 적절하지 않을 수 있음
- Django에서는 User을 참조하는데 사용하는 AUTH_USER_MODEL 값을 제공하여, default user model을 재정의(override)할 수 있도록 함
- Django는 새 프로젝트를 시작하는 경우 **커스텀 유저 모델을 설정하는 것을 강력히 권장**
  - 프로젝트의 모든 migrations 혹은 첫 migrate를 실행하기 전에 이 작업 마쳐야 함



#### AUTH_USER_MODEL

> User를 나타내는데 사용하는 모델

- 프로젝트가 진행되는 동안 변경이 불가능
- 프로젝트 시작 시 설정하기 위한 것이며, 참조하는 모델은 **첫번째 마이그레이션에서 사용할 수 있어야 함**
- 기본 값 : 'auth.User'



#### Custom User 모델 정의하기

1. 관리자 권한과 함께 완전한 기능을 갖춘 User 모델을 구현하는 기본 클래스인 AbstractUser를 상속받아 새로운 User 모델 작성

   ```python
   # accounts/models.py
   
   from django.contrib.auth.models import AbstractUser
   
   class User(AbstarctUser):
       pass
   ```

2. 기존에 Django가 사용하는 User 모델이었떤 auth 앱의 User 모델을 account 앱의 User 모델을 사용하도록 변경(중요)

   ```python
   # settings.py
   
   AUTH_USER_MODEL = 'accounts.User'
   ```

3. admin site에 Custom User 모델 등록

   ```python
   # accounts/admin.py
   
   from django.contrib import admin
   from django.contrib.auth.admin import UserAdmin
   from .models import User
   
   admin.site.register(User, UserAdmin)
   ```

4. migrate



## Custom user & Built-in Auth Forms

> UserCreationForm과 UserChangeForm은 기존에 내장 User 모델을 사용하던 것과 달리 커스텀 User 모델을 사용해야 함

```python
# accounts/forms.py

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('email',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name',)
```

```python
# accounts/views.py

from .forms import CustomUserCreationForm, CustomUserChangeForm #

@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST) #
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm() #
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user) #
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user) #
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)
```



#### get_user_model()

- 현재 프로젝트에서 활성화된 사용자 모델 반환
  - User 모델을 커스터마이징한 경우 Custom User모델 반환
- 이 때문에 Django는 User 클래스는 직접 참조하는 대신 django.contrib.auth.get_user_model()을 사용하여 참조해야 한다고 강조



## 1:N 관계 설정

#### User - Article (1:N)

- Django에서 user 모델을 참조할 때
  1. models.py에서는 `settings.AUTH_USER_MODEL`
     - User 모델에 대한 외래 키 또는 다대다 관계 정의할 때 사용
  2. models.py를 제외한 다른 모든 곳은 `get_user_model()`
     - 현재 활성화된 User 모델 반환



##### User와 Article 간 모델 관계 정의 후 migration

```python
# articles/models.py

from django.conf import settings

class Article(models.Model):
    user = mouser = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ...
```

- migrate시 선택창이 나옴

  - 1 enter : 현재 화면에서 기본 값을 설정하겠다
  - 1 enter : 기존 테이블에 추가되는 user_id 필드의 값을 1로 설정하겠다

- 게시글 작성시 User를 선택하는 창이 나옴

  - 필드 수정

    ```python
    # articles/forms.py
    
    class ArticleForm(forms.ModelForm):
    
        class Meta:
            model = Article
            exclude = ('user',)
    ```

  - CREATE 수정 : 게시글 작성 시 작성자 정보 추가 후 게시글 작성 재시도

    ```python
    # articles/views.py
    
    @login_required
    @require_http_methods(['GET', 'POST'])
    def create(request):
        if request.method == 'POST':
            form = ArticleForm(request.POST)
            if form.is_valid():
                article = form.save(commit=False) 	#
                article.user = request.user 		#
                article.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm()
        context = {
            'form': form,
        }
        return render(request, 'articles/create.html', context)
    
    ```

  - DELETE 수정 : 자신이 작성한 게시글만 삭제 가능하도록 설정

    ```python
    # articles/views.py
    
    @require_POST
    def delete(request, pk):
        article = get_object_or_404(Article, pk=pk)
        if request.user.is_authenticated:
            if request.user == article.user:	#
                article.delete()
        return redirect('articles:index')
    ```

  - UPDATE 수정 : 자신이 작성한 게시글만 수정 가능하도록 설정

    ```python
    # articles/views.py
    
    @login_required
    @require_http_methods(['GET', 'POST'])
    def update(request, pk):
        article = get_object_or_404(Article, pk=pk)
        if request.user == article.user:			#
            if request.method == 'POST':
                form = ArticleForm(request.POST, instance=article)
                if form.is_valid():
                    article = form.save()
                    return redirect('articles:detail', article.pk)
            else:
                form = ArticleForm(instance=article)
        else:										#
            return redirect('articles:index')		#
        context = {
            'article': article,
            'form': form,
        }
        return render(request, 'articles/update.html', context)
    ```

  - READ 수정

    - 게시글 작성 user가 누구인지 출력

      ```django
      <!-- articles/index.html -->
      
      <p>작성자: {{ article.user }}</p>
      ```

    - 해당 게시글의 작성자가 아니라면, 수정/삭제 버튼을 출력하지 않도록 처리

      ```django
      <!-- articles/detail.html -->
      
      {% if request.user == article.user %}
        <a href="{% url 'articles:update' article.pk %}">수정</a>
        <form action="{% url 'articles:delete' article.pk %}" method="POST">
          {% csrf_token %}
          <input type="submit" value="삭제">
        </form>
      {% endif %}
      ```

      

#### User - Comment (1:N)

##### User와 Comment 간 모델 관계 정의 후 migration

```python
# articles/models.py

from django.conf import settings

class Comment(models.Model):
    user = mouser = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ...
```

- migrate시 선택창이 나옴

  - 1 enter : 현재 화면에서 기본 값을 설정하겠다
  - 1 enter : 기존 테이블에 추가되는 user_id 필드의 값을 1로 설정하겠다

- 댓글 작성시 User를 선택하는 창이 나옴

  - 필드 수정

    ```python
    # articles/forms.py
    
    class CommentForm(forms.ModelForm):
    
        class Meta:
            model = Comment
            fields = ('content',)
            # exclude = ('article', 'user',)
    ```

  - CREATE 수정 : 댓글 작성 시 작성자 정보 추가 후 댓글 작성 재시도

    ```python
    # articles/views.py
    
    @require_POST
    def comment_create(request, pk):
        if request.user.is_authenticated:
            article = get_object_or_404(Article, pk=pk)
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.article = article
                comment.user = request.user 	#
                comment.save()
            return redirect('articles:detail', article.pk)
        return redirect('accounts:login')
    ```

  - READ 수정

    - 비로그인 유저에게는 댓글 form 출력 숨기기

      ```django
      <!-- articles/detail.html -->
      
      {% if request.user == article.user %}
        <a href="{% url 'articles:update' article.pk %}">수정</a>
        <form action="{% url 'articles:delete' article.pk %}" method="POST">
          {% csrf_token %}
          <input type="submit" value="삭제">
        </form>
      {% else %}
        <a href="{% url 'accounts:login' %}">[댓글을 작성하려면 로그인하세요.]</a>
      {% endif %}
      ```

    - 댓글 작성자 출력하기

      ```django
      <!-- articles/detail.html -->
      
      <ul>
          {% for c in comments %}
            <li>
              {{ c.user }} - {{ c.content }} {##}
            ...
      </ul>
      ```

  - DELETE 수정

    - 자신이 작성한 댓글만 삭제 버튼을 볼 수 있도록 수정

      ```django
      <!-- articles/detail.html -->
      
      {% if request.user == c.user %}
        <form action="{% url 'articles:comment_delete' article.pk c.pk %}" method="POST">
          {% csrf_token %}
          <input type="submit" value="삭제">
        </form>
      {% endif %}
      ```

    - 자신이 작성한 댓글만 삭제할 수 있도록 수정

      ```python
      # articles/views.py
      
      @require_POST
      def comment_delete(request, article_pk ,comment_pk):
          if request.user.is_authenticated:
              comment = get_object_or_404(Comment, pk=comment_pk)
              if request.user == comment.user: 	#
                  comment.delete()
          return redirect('articles:detail', article_pk)
      ```

      

#### 그 외

- 댓글 수정 기능은 JavaScript 필요
  - 수정페이지로 넘어가서 댓글을 수정하는 것은 가능하지만 어색하게 구현되므로 하지 않기로 함