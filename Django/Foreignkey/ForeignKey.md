# ForeignKey

> 외래키. 관계형 데이터베이스에서 한 테이블의 필드 중 다른 테이블의 행을 식별할 수 있는 키

- 외래 키의 값이 반드시 부모 테이블의 기본 키일 필요는 없지만 유일한 값이어야 함
  - 참조 무결성 : 데이터베이스 관계 모델에서 관련된 2개 테이블 간의 일관성. 외래 키가 선언된 테이블의 외래 키 속성의 값은 그 테이블의 부모가 되는 테이블의 기본 키 값으로 존재해야 함



## ForeignKey field

- 다대일 관계

- 2개의 위치 인자 반드시 필요

  - 참조하는 model class
  - on_delete 옵션

- 필드 이름에 _id를 추가하여 데이터베이스 열 이름 만듦

  ```python
  # articles/models.py
  
  class Comment(models.Model):
      article = models.ForeignKey(Article, on_delete=models.CASCADE) #
      content = models.CharField(max_length=200)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  
      def __str__(self):
          return self.content
  ```

- on_delete

  - 외래 키가 참조하는 객체가 사라졌을 때 외래 키를 가진 객체를 어떻게 처리할지 정의
  - 데이터 무결성을 위해 매우 중요한 설정
    - 참조 무결성 : FK(외래 키) 값이 데이터베이스의 특정 테이블의 PK 값을 참조하는것
  - CASCADE : 부모 객체가 삭제됐을 때 이를 참조하는 객체도 삭제

- 이후 Migration 진행 후 articles_comment 테이블에서 ForeinKey 컬럼인 article은 article_id와 같이 `_id`가 붙어 필드이름이 작성된 것 확인(`_id` 직접 쓰지 않도록 주의)

  ```python
  c1 = Comment.objects.get(pk=1)
  c1.article # 아티클 객체
  c1.article_id # 아티클 id
  ```

  - 두가지 방법 모두 쓸 수 있지만 쓰는 방식이 다르다
    - comment.article_id = article.pk
      - comment.article_id : 물리적인 이름
      - comment.article.pk : 객체쪽 접근
    - comment.article = article -> 권장사항

- 1:N 관계 related manager

  - 참조('article') : Comment 필드에 직접 작성한다

    - Comment(N) -> Article(1)

  - 역참조('comment_set') : Article은 Comment를 역참조한다

    - Article(1) -> Comment(N)

    - 실제로 Article 클래스에는 Comment와의 어떠한 관계도 작성되어 있지 않음(물리적으로 불가능)

      ```shell
      article.comment_set.all()
      # <QuerySet [<Comment: Comment object (1)>]>
      ```

    - `related_name`을 이용하여 역참조시 사용할 이름 변경이 가능하다

      ```python
      # articles/models.py
      
      class Comment(models.Model):
          article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
      ```

      - 이렇게 변경할 경우 article.comment_set.all() 대신 article.comments.all()처럼 대체하여 사용해야하지만 바꿔 쓰는 것은 권장하지 않는다



## CREATE in Comment

- 생각해볼 점
  1. CommentForm에서 모든 필드를 받을 경우 article, 즉 댓글에 대한 게시물을 사용자가 직접 입력해야하는 상황이 발생하므로 content만 받도록 한다
  2. save(commit=False)의 활용
     - content만 받느라 article에 대한 정보가 반영되지 않았음 => 그대로 save할 경우 오류 발생
     - `article = form.save(commit=False)`를 해주면 content만 입력받은 채로 DB에 반영하지 않고 인스턴스 반환 => 필요한 값을 추가해서 직접 save!
     - 인스턴스 반환 시 유효성 통과한 article 객체를 반환
  3. 댓글 출력
- 정리

```python
# articles/forms.py

from .models import Article, Comment

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content',) # 1. all로 받을 경우 게시물을 사용자가 직접 입력해야하므로
```

```python
# articles/view.py
from .forms import ArtcileForm, CommentForm

def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm()
    # 조회한 article의 모든 댓글을 조회(역참조)
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments, # 3. 댓글 가져와서 context에 추가
    }
    return render(request, 'articles/detail.html', context)
```

```django
<!-- articles/detail.html -->
<ul>
  {% for c in comments %} {# 3. 댓글 출력 #}
    <li>
      {{ c.content }}
    </li>
  {% endfor %}
</ul>

<form action="{% url 'articles:comment_create' article.pk %}" method="POST">
    {% csrf_token %}
    {{ comment_form }}
    <input type="submit">
</form>
```

```python
# articles/urls.py

path('<int:pk>/comments/', views.comment_create, name='comment_create'),
```

```python
# articles/view.py
@require_POST
def comment_create(request, pk):
    if request.user.is_authenticated: # 인증된 사용자만 댓글 작성 가능
        article = get_object_or_404(Article, pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False) # 2. commit=False의 활용
            comment.article = article
            comment.save()
        return redirect('articles:detail', article.pk)
    return redirect('accounts:login')
```



## DELETE in Comment

```python
# articles/urls.py

path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),
```

```django
<!-- articles/detail.html -->

<ul>
  {% for c in comments %}
    <li>
      {{ c.content }}
      {% if request.user == c.user %}
        <form action="{% url 'articles:comment_delete' article.pk c.pk %}" method="POST">
          {% csrf_token %}
          <input type="submit" value="삭제">
        </form>
      {% endif %}
    </li>
  {% endfor %}
</ul>
```

```python
# articles/views.py

@require_POST
def comment_delete(request, article_pk ,comment_pk):
    if request.user.is_authenticated: # 인증된 사용자만 댓글 삭제 가능
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('articles:detail', article_pk)
```



## 그 외 추가기능

- 댓글 개수 출력

  ```django
  <!-- articles/detail.html -->
  
  {% if comments %}
  	{{ comments|length }}개의 댓글이 있습니다
  {% endif %}
  ```

- 댓글 없는 경우 대체 컨텐츠 출력

  ```django
  <!-- articles/detail.html -->
  
  {% for c in comments %}
  	...
  {% empty %}
  	댓글이 없어요
  {% endfor %}
