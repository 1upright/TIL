# CRUD

> 대부분의 소프트웨어가 가지는 기본적인 데이터 처리 기능
>
> Create(생성), Read(읽기), Update(갱신), Delete(삭제)



#### CREATE

```shell
# 방법 1
article = Article()
article.title = '제목임미당'
article.content = '내용임미당'
article.save()

# 방법 2
article = Article(title='제목임미당', content='내용임미당')
article.save()

# 방법 3
Article.objects.create(title='제목임미당', content='내용임미당')
```



#### READ

- 전체 데이터 조회 - all()

```shell
Article.objects.all()
```

- 단일 데이터 조회(객체로) - get()

```shell
Article.objects.get(pk=3)
# => <Article: Article object (3)>
```

```shell
# 2-1. 없는 데이터 => 에러
Article.objects.get(pk=10000)
# => DoesNotExist: Article matching query does not exist.

# 2-2. 여러개 있는 경우 => 에러
Article.objects.get(title='제목임미당')
# => MultipleObjectsReturned: get() returned more than one Article -- it returned 2!
```

- 여러 데이터 조회(QuerySet) - filter()

```shell
Article.objects.filter(title='제목임미당')
```



#### UPDATE

```shell
article = Article.objects.get(pk=3)
article.title = '변경된 제목'
article.save()
```



#### DELETE

```shell
article.objects.get(pk=3)
article.delete()
```



## CRUD with views

#### INDEX

> 전체 게시물 목록

- URL : `/articles/index/`
- View : 
  - DB 접근
  - Article.objects.all()
  - context - 게시글 전체(QuerySet)
- Template : articles 반복하여 출력

```python
# articles/views.py

from django.shortcuts import render, redirect # redirect 필요해지면 넣어도 됨
from .models import Article

def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)
```

```django
{# articles/templates/articles/index.html #}
{% extends 'base.html' %}

{% block body %}
  <h1>안녕하세요</h1>

  {% for article in articles %}
    <p> {{ article.title }} </p>
    <hr>
  {% endfor %}
{% endblock body %}
```



#### CREATE

**new**

> 게시글 작성 양식

- URL : `/articles/new/`
- View : 그냥 render
- Template : form 활용
  - form tag(action, method)
  - input tag(name)
  - textarea tag(name)

```python
# articles/views.py
def new(request):
    return render(request, 'articles/new.html')
```

```django
{# articles/templates/articles/new.html #}
{% extends 'base.html' %}

{% block body %}
  {% comment %} <form action="/articles/create/" method="GET"> {% endcomment %}
  <form action="{% url 'articles:create' %}" method="GET">
    <label for="title">제목 : </label>
    <input type="text" id="title" name="title">
{# id는 라벨 때문에 했던거임, 라벨은 해당 input에 포커스를 주기 위함 #}
    <hr>
    <label for="content">내용 : </label>
    <textarea name="content"></textarea>
    <hr>
    <input type="submit" value="제출">
  </form>
{% endblock body %}
```



**create**

> 게시물 생성(DB)하고 redirect

- URL : `/articles/create/`
- View :
  - DB 접근
  - Article.objects.create()
- Template : X
- template 없이 `redirect('/articles/<pk>')`해도 되지만 예시에서는 template 사용

```python
# articles/views.py
def create(request):
    # 1) 사용자 입력 받기
    title = request.GET.get('title')
    content = request.GET.get('content')

    # 2) DB에 저장(CREATE의 세가지 방법 활용 )
    article = Article()
    article.title = title
    article.content = content
    article.save()

    # 3) template에서 보여주기
    context = {
        'article': article
    }
    return render(request, 'articles/create.html', context)
```

```django
{# articles/templates/articles/create.html #}
{% extends 'base.html' %}

{% block body %}
  <h1>{{ article.id }}번 글이 작성 완료되었습니다.</h1>
  <h2>{{ article.title }}</h2>
  <p>{{ article.content }}</p>
{% endblock body %}
```



```python
# redirect로 하고 싶다면?
def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    article = Article()
    article.title = title
    article.content = content
    article.save()
    
    return redirect('articles:detail', article.pk)
```



#### Read

> 특정 게시글 조회

- URL : `/articles/<pk>`
- View :
  - pk, DB 접근
  - Article.object.get(pk=pk)
  - context : 특정 게시글 객체
- Template : article 내용 출력

```python
# articles/views.py
def detail(request, pk):
    # pk번글 조회
    article = Article.objects.get(pk=pk)

    # 템플릿에서 활용
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)
```

```django
{# articles/templates/articles/detail.html #}
{% extends 'base.html' %}

{% block body %}
  <h1>{{ article.pk }}번 글</h1>
  <h2>{{ article.title }}</h2>
  <h5>{{ article.created_at }} | {{ article.updated_at }}</h5>
  <hr>
  <p>{{ article.content }}</p>
{% endblock body %}
```

```django
{# articles/templates/articles/index.html 변경 #}
<h1>안녕하세요</h1>

  {% for article in articles %}
    <a href="{% url 'articles:detail' article.pk %}"> {# detail이 나오게 #}
      <p> {{ article.title }} </p> {# title을 클릭하면 #}
    </a>
    <hr>
  {% endfor %}
{% endblock body %}
```



#### Delete

> 특정 게시글 삭제하고 redirect

- URL : `/articles/<pk>/delete/`
- View :
  - pk, DB 접근
  - Article.objects.get(pk=pk)
- Template : X

```python
# articles/views.py
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')
```

```django
{# articles/templates/articles/detail.html 변경 #}
{% extends 'base.html' %}

{% block body %}
  <h1>{{ article.pk }}번 글</h1>
  <h2>{{ article.title }}</h2>
  <h5>{{ article.created_at }} | {{ article.updated_at }}</h5>
  <hr>
  <p>{{ article.content }}</p>
  <a href="{% url 'articles:delete' article.pk %}">글 삭제</a> {# 추가 #}
{% endblock body %}
```



#### Update

**edit**

> 특정 게시글 수정 양식

- URL : `/articles/<pk>/edit/`
- View :
  - pk, DB 접근
  - Article.objects.get(pk=pk)
- Template : form 활용
  - form tag(action, method)
  - input tag(name)
  - textarea tag(name)
  - new.html과 비슷하지만 input에서 value="작성된 제목"으로 해주고 textarea의 안에 작성된 내용을 넣어주면 깔끔

```python
# articles/views.py
def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/edit.html', context)
```

```django
{# articles/templates/articles/edit.html #}
{% extends 'base.html' %}

{% block body %}
  <h1>게시글 수정</h1>
  <form action="{% url 'articles:update' article.pk %}" method="GET">
    <label for="title">제목 : </label>
    <input type="text" id="title" name="title" value="{{article.title}}"> 
    <hr>
    <label for="content">내용 : </label>
    <textarea name="content">{{article.content}}</textarea>
    <hr>
    <input type="submit" value="제출">
  </form>
{% endblock body %}
```

```django
{# articles/templates/articles/detail.html 변경 #}
{% extends 'base.html' %}

{% block body %}
  <h1>{{ article.pk }}번 글</h1>
  <h2>{{ article.title }}</h2>
  <h5>{{ article.created_at }} | {{ article.updated_at }}</h5>
  <hr>
  <p>{{ article.content }}</p>
  <a href="{% url 'articles:delete' article.pk %}">글 삭제</a> 
  <a href="{% url 'articles:edit' article.pk %}">글 수정</a> {# 추가 #}
{% endblock body %}
```



**update**

> 특정 게시글 수정(DB)하고 redirect

- URL : `articles/<pk>/update/`
- View : 
  - pk, DB 접근
  - article = Article.objects.get(pk=pk)
  - Article.objects.create()
- Template : X

```python
# articles/views.py
def update(request, pk):
    title = request.GET.get('title')
    content = request.GET.get('content')

    article = Article.objects.get(pk=pk)
    article.title = title
    article.content = content
    article.save()

    return redirect('articles:detail', article.pk)
```



#### 최종 URL

```python
# articles/urls.py
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name="create"),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'),
]
```



#### POST

- GET을 사용하면 `/article/create/?title=jemok&content=naeyong` 이런식으로 서버 로그에 모든 정보가 담김
  - 하지만 id와 password 받는 상황이면 그거까지 집어넣는건 에바 아님?
    - 정보를 숨겨 보내기 위해 method="GET"이 아닌 method="POST"로 바꿔보자!
- 보안상 서버에 요청할 때 GET으로 달라고 하는게 아닌 POST로 달라고 하는게 국룰!
- 구현

```django
{# articles/templates/articles/edit.html #}
<form action="{% url 'articles:update' article.pk %}" method="GET">

=>
    
<form action="{% url 'articles:update' article.pk %}" method="POST">
  {% csrf_token %}
    
{# articles/templates/articles/new.html #}    
<form action="{% url 'articles:create' article.pk %}" method="GET">

=>
    
<form action="{% url 'articles:create' article.pk %}" method="POST">
  {% csrf_token %}
```

```python
# articles/views.py의 create, update 함수에서..
title = request.GET.get('title')
content = request.GET.get('content')

=>

title = request.POST.get('title')
content = request.POST.get('content')
```

