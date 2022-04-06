# Form/ModelForm

## Django Form Class

- HTML form, input을 통해 데이터를 받으면 유효성 검증 시 반복 코드 발생
  - 유효성 검증 : 사용자가 입력한 데이터를 검증하는 것
- Django Form을 사용하면 과중한 작업(데이터 유효성 검증, 필요시 입력된 데이터 검증 결과 재출력, 유효한 데이터에 대해 요구되는 동작 수행)과 반복 코드를 줄여 이 작업을 쉽고 빠르고 안전하게 할 수 있음
- Django가 처리해 주는 form 관련 작업
  1. 렌더링을 위한 데이터 준비 및 재구성
  2. 데이터에 대한 HTML forms 생성
  3. 클라이언트로부터 받은 데이터 수신 및 처리
- Form내 field, field 배치, 디스플레이 widget, label, 초기값, 유효하지 않은 field 관련 에러 메세지 결정



#### Form 선언

```python
# articles/forms.py
from django import forms

clss ArticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField()
```

- Models 선언하는 것과 유사하며 같은 필드타입 사용
- forms 라이브러리에서 파생된 Form 클래스를 상속받음



#### 사용

```python
# articles/views.py
from .forms import ArticleForm

def new(request):
    form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)
```

```django
<!-- new.html -->
{% extends 'base.html' %}

{% block body %}
  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="제출">
  </form>
{% endblock body %}
```



#### From rendering options

- as_p() : 각 필드가 `<p>` 태그로 감싸져서 렌더링 됨
- as_ul() : 각 필드가 `<li>` 태그로 감싸져서 렌더링 됨
  - `<ul>` 태그는 직접 작성해야 함
- as_table() : 각 필드가 `<tr>` 태그로 감싸져서 렌더링 됨
  - `<table>` 태그는 직접 작성해야 함



#### input 요소 표현 방법

- Form fields
  - input에 대한 유효성 검사 로직을 처리하며 템플릿에서 직접 사용
- Widgets
  - HTML input 요소 렌더링
  - GET/POST 딕셔너리에서 데이터 추출
  - widgets은 반드시 Form fields에 할당됨
  - 주의사항
    - input 유효성 검사를 처리하는 Form Fields와 혼동하지 말 것!
    - Widgets은 input element의 처리만!



## ModelForm

> Model을 통해 Form Class를 만들 수 있는 Helper
>
> 일반 Form Class와 완전히 같은 방식으로 view에서 사용 가능



#### 선언

```python
# articles/forms.py
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
		model = Article
        fields = '__all__'
        # exclude = ('title',)
```

- 정의한 클래스 안에 Meta 클래스를 선언하고, 어떤 모델을 기반으로 Form을 작성할 것인지에 대한 정보를 Meta클래스에 지정
- fields와 exclude는 동시에 사용할 수 없음에 주의



#### Meta class

> Model의 정보를 작성하는 곳

- ModelForm을 사용할 경우 사용할 모델이 있어야 하는데 Meta Class가 이를 구성함



#### ModelForm을 적용한 CRUD

##### CREATE

```python
# articles/views.py

def create(request):
    form = ArticleForm(request.POST)
    if form.is_valid(): #
        article = form.save() #
        return redirect('articles:detail', article.pk)
    return redirect('articles:new')
```

- `is_valid()` method

  - 유효성 검사를 실행하고 데이터가 유효한지 여부를 boolean으로 반환
  - 데이터 유효성 검사를 보장하기 위해 Django에서 제공하는 메소드
  - 요청한 데이터가 필드 조건에 충족하는지 확인하여, 올바르지 않은 데이터가 서버로 전송되거나 저장되는 것을 방지하기 위함

- `save()` method

  - Form에 바인딩 된 데이터에서 데이터베이스 객체를 만들고 저장
  - Modelform의 하위 클래스는 기존 모델 인스턴스를 키워드 인자(instance)로 받아 들일 수 있음
    - 중요 : 이것이 제공되면 `save()`는 해당 인스턴스를 수정하는 UPDATE의 기능을, 제공되지 않으면 지정된 모델의 새 인스턴스를 만드는 CREATE의 기능을 수행할 것!
  - Form의 유효성이 확인되지 않은 경우 `save()`를 호출하면 form.errors를 통해 에러 확인 가능

- "new"를 없애고 싶다면??

  ```python
  # articles/views.py
  
  def create(request):
      if request.method == 'POST':
          form = ArticleForm(request.POST)
          if form.is_valid():
              article = form.save()
              return redirect('articles:detail', article.pk)
      else:
          form = ArticleForm()
      context = {
          'form': form,
      }
      return render(request, 'articles/create.html', context)
  ```

  - new.html도 create.html로 바꿔주기
  - new 함수와 url path를 삭제하기
  - 다른 템플릿 등에서 호출한 모든 new를 create로 바꾸어주기
  - NEW라고 이름지은 `<a>`도 모두 CREATE로 바꾸어주기(선택)

- Widgets 활용하기

  - 속성값을 넣기 위해 `attrs={}`를 활용한다

  - 첫 번째 방식
  
    ```python
    # articles/forms.py
    from django import forms
    from .models import Article
    
    class ArticleForm(forms.ModelForm):
        class Meta:
    		model = Article
            fields = '__all__'
            widgets = {
                'title': forms.TextInput(attrs={
                    'class': 'my-title',
                    'placeholder': 'Enter the title',
                    'maxlength': 10,
                	}
                )
            }
    ```

    - 하지만 구조상 Meta 클래스가 커지면 유지보수가 어려우므로 권장되지 않는 방식

  - 두 번째 방식(권장사항)
  
    ```python
    # articles/forms.py
    from django import forms
    from .models import Article
    
    class ArticleForm(forms.ModelForm):
        title = forms.CharField(
        	label='제목',
            widget=forms.TextInput(
                attrs={
                    'class': 'my-title',
                    'placeholder': 'Enter the title',
                }
            ),
        )
        
        class Meta:
    		model = Article
            fields = '__all__'
    ```

  - 예시
  
    ```python
    # articles/forms.py
    from django import forms
    from .models import Article
    
    
    class ArticleForm(forms.ModelForm):
        title = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    'class': 'my-title form-control',
                    'placeholder': 'Enter the title',
                }
            )
        )
        content = forms.CharField(
            widget=forms.Textarea(
                attrs={
                    'class': 'my-content form-control',
                }
            ),
            error_messages={
                'required': 'Please enter your content!!!',
            }
        )
    
        class Meta:
            model = Article
            fields = '__all__'
    ```
  



##### DELETE

```python
# articles/views.py

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    return redirect('articles:detail', article.pk)
```

```django
<!-- detail.html -->

<form action="{% url 'articles:delete' article.pk %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="DELETE">
</form>
```



##### UPDATE

```python
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        # update
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():  # 유효성 검사
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        # edit
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)
```

```django
<!-- update.html -->
{% extends 'base.html' %}

{% block content %}
  <h1>UPDATE</h1>
  <hr>
  <form action="{% url 'articles:update' article.pk %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
  <a href="{% url 'articles:detail' article.pk %}">back</a>
{% endblock content %}
```

- edit의 path와 view 삭제
- edit.html에서 update.html로 변경
- 다른 view와 템플릿들에서 edit의 흔적 없애주기
- UPDATE가 CREATE와 다른 점
  - UPDATE에는 데이터를 조회하는 부분이 들어감
  - instance=article을 넣어주어 CREATE가 아닌 UPDATE가 작동되도록 했음



#### ModelForm 왜 쓸까?

1. 모델로 만들어진 테이블 필드 속성에 맞는 html element를 쉽게 만들어줌
2. 이를 통해 받은 데이터를 가지고 view 함수에서 유효성 검사 가능
3. Form과의 역할이 다르다
   - Form
     - 어떤 Model에 저장해야 하는지 알 수 없으므로 유효성 검사 이후 cleaned_data 딕셔너리 생성
     - cleaned_data 딕셔너리에서 데이터를 가져온 후 .save() 호출해야 함
     - Model에 연관되지 않은 데이터를 받을 때 사용
     - ex) DB에 데이터를 저장할 필요가 없는 로그인 등에서 활용 가능
   - ModelForm
     - Django가 해당 model에서 양식에 필요한 대부분의 정보를 이미 정의
     - 어떤 레코드를 만들어야 할지 알고 있으므로 바로 .save() 호출 가능
     - ex) DB에 데이터를 저장해야하는 회원가입 등에서 활용 가능



## Rendering fields manually

```django
<!-- articles/create.html -->
{% extends 'base.html' %}


{% block content %}
  <h1>CREATE</h1>
  <hr>
  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
  <hr>

  <h2>1. Rendering fields manually</h2>
  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    <div>
      {{ form.title.errors }}
      {{ form.title.label_tag }}
      {{ form.title }}
    </div>
    <div>
      {{ form.content.errors }}
      {{ form.content.label_tag }}
      {{ form.content }}
    </div>
    <input type="submit">
  </form>
  <hr>
  
  <h2>2. Looping over the form’s fields</h2>
  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    {% for field in form %}
	  {{ field.errors }}
      {{ field.label_tag }}
      {{ field.title }}
    {% endfor %}
    <input type="submit">
  </form>

  <a href="{% url 'articles:index' %}">back</a>
{% endblock content %}
```

1. 그냥 렌더링
2. DTL의 반복문을 이용한 렌더링



- bootstrap 이용

  ```python
  # forms.py
  
  class ArticleForm(forms.ModelForm):
      title = forms.CharField(
          widget=forms.TextInput(
              attrs={
                  'class': 'my-title form-control',
                  'placeholder': 'Enter the title',
              }
          )
      )
      content = forms.CharField(
          widget=forms.Textarea(
              attrs={
                  'class': 'my-content form-control',
              }
          ),
          error_messages={
              'required': 'Please enter your content!!!',
          }
      )
  
      class Meta:
          model = Article
          fields = '__all__'
  ```

  ```django
  <!-- articles/create.html -->
  
  <form action="{% url 'articles:create' %}" method="POST">
      {% csrf_token %}
      {% for field in form %}
        {% if field.errors %}
          {% for error in field.errors %}
            <div class="alert alert-warning">{{ error }}</div>
          {% endfor %}
        {% endif %}
        {{ field.label_tag }}
        {{ field }}
      {% endfor %}
      <input type="submit">
  </form>



## 그 외 참고사항

- CREATE와 UPDATE의 view에서 `if request.method == 'POST'`로 할 수 밖에 없었다
  - DB를 조작하는 상황은 GET이나 다른 메서드들과 달리 POST메서드에서만 생기기 때문