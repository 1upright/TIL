# Django기초

> Python Web framework

1. 가상환경 생성 및 활성
2. django 설치
3. 프로젝트 생성
4. 서버 켜서 로켓 확인하기
5. 앱 생성
6. 앱 등록



## 기본 구조

- Django의 기본 구조?

  - MTV (Model - Template - View) 패턴 ⇒ MVC 패턴

  | Django   | MVC        | 뜻            |
  | -------- | ---------- | ------------- |
  | Model    | Model      | DB            |
  | Template | View       | 보여지는 화면 |
  | View     | Controller | 처리          |



## 요청 처리 흐름

- URL => VIEWS => TEMPLATE
  - URL 요청이 왔을 때, VIEWS로 작업을 해서 TEMPLATE으로 HTML 응답

![Image Pasted at 2022-3-2 13-45](Django%EA%B8%B0%EC%B4%88.assets/Image%20Pasted%20at%202022-3-2%2013-45.png)



## 1. 가상환경

> 프로젝트별로 pip로 설치되는 패키지를 독립적으로 관리하기 위하여 생성



#### 가상환경 생성

```bash
$ python -m venv venv
```



#### 가상환경 활성

```bash
$ source venv/Scripts/activate
```



#### 가상환경 종료

```bash
$ deactivate
```



## 2. Django 설치

```bash
$ pip install django==3.2.12
```



- 4.x 버전 설치한 경우 삭제 후 재설치

```bash
$ pip uninstall django
```



## 3. 프로젝트 생성

```bash
$ django-admin startproject firstpjt .
```

- `urls.py`, `wsgi.py`, `manage.py`는 건드려도 되지만`__init__.py`, `asgi.py`, `settings.py`는 터치 X



## 4. Django 실행

```bash
$ python manage.py runserver
```

- Starting development server at '주소'
  - 주소 클릭 후 로켓 확인 가능

- 이후 서버 종료해야함



## 5. 앱 생성

```bash
$ python manage.py startapp articles
```

- `admin.py`, `models.py`, `views.py`는 건드려도 되지만`__init__.py`, `apps,py`, `tests.py`는 터치 X



## 6. 앱 등록

- settings.py의 INSTALLED_APPS에 'articles' 집어넣기

```python
INSTALLED_APPS = [
    'articles',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```



#### URL

- urls.py
  - `admin/` : url 주소 일부분, 로켓 주소뒤에다가 /admin 집어넣으면 로그인창 뜸
  - 장고에서는 /(end slash)를 반드시 붙여줘야함, 클라이언트에서 접속할 때는 안붙여도 된다
  - 끝에 `,` (trailing comma)를 꼭 붙여주어야 한다
  - 새로운 경로 설정
    - from articles import views 넣어주기
    - index 경로 들어오면 articles에 있는 views내 index 함수를 가져올거다

```python
from django.contrib import admin
from django.urls import path
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    # URL에 bts로 들어오면
    # bts 함수를 실행시킬 것이다.
    path('bts/', views.bts),
]
```



#### View

- views.py에 def로 함수 만들어줌
  - 요청 정보 : `request`, 처리, 응답을 위해 `render`


```python
from django.shortcuts import render

# index 함수는
# 어떠한 작업을 하고 (아짂 쓰지 않음)
# index.html을 랜더링할 것이다

# Create your views here.
def index(request):
    # 작업
    return render(request, 'index.html')

def bts(request):
    return render(request, 'bts.html')
```



#### Template

- articles 안에 templates 폴더 생성후 index.html 작성
  - app폴더 안에 templates라는 폴더 안에 html을 쓰는 것은 약속!! 
  - 순수한 html이 아니라 Django Template Language임

```html
<!-- articles/templates/index.html -->
<h1>안녕</h1>
```



#### 추가 설정

- settings.py
  - LANGUAGE_CODE = 'ko-kr'
  - TIME_ZONE = 'Asia/Seoul'



## Django Template Language(DTL)

> 단순히 Python이 HTML에 포함된 것이 아니며, 프로그래밍 로직이 아니라 프레젠테이션을 표현하기 위한 것



#### 1. variable

> render()를 사용하여 views.py에서 정의한 변수를 template 파일로 넘겨 사용하는 것

- template에서 `{{ variable }}`과 같이 입력하여 사용

- views에 세번째 인자로 {'name' : 'Alice'}, html에 {{ name }} 쓰면 출력은 Alice로 나옴
- 많은 변수가 호출되는 경우 함수명과 return 사이에 관행적으로 'context'라는 이름으로 dictionary를 만들어 사용한다

```html
{{ info.name|lower }} <!-- 딕셔너리.이름|함수 -->
{{ foods }} <!-- 리스트 -->
{{ foods.0 }} <!-- 리스트 인덱스 -->
```



#### 2. Filters

> 표시할 변수를 수정할 때

- `{{ variable|filter }}`와 같이 사용



#### 3. Tags

> 출력 텍스트를 만들거나, 반복 또는 논리를 수행하여 제어 흐름을 만드는 등 변수보다 복잡한 일들을 수행

- `{% tag %}`와 같이 사용
- [템플릿 내장 태그와 필터들](https://docs.djangoproject.com/en/4.0/ref/templates/builtins/)



#### 4. Comments

> Django template에서 라인의 주석을 표현

- `{#  #}`
- `<!--  -->`
- 여러줄 주석 사용시

```django
{% comment %}
	주석
	주석
{% endcomment %}
```



## 템플릿 상속

> 코드의 재사용성에 초점. 사이트의 모든 공통 요소를 포함하고, 하위 템플릿이 override할 수 있는 블록을 정의하는 기본 'skeleton' 템플릿을 만들 수 있음

- 모든 html에 부트스트랩을 넣고 싶은데 CDN 코드를 가져와 모든 html에 하나하나 집어넣는다?
  - 이런 반복 작업은 너무 싫으니 상속을 사용하자



#### 방법

1. settings.py의 TEMPLATES 내 'DIRS'에 `[BASE_DIR / 'templates',],`와 같이 템플릿 추가 경로 설정
2. base.html(부모 템플릿)에서 bootstrap 및 간단한 navbar 작성
   -  `{% block content %} {% endblock %}` : 하위 템플릿에서 overriden할 수 있는 블록 정의

```django
<!-- base.html -->
<nav>
    ...
    {# bootstrap에서 따온 navbar #}
</nav>
{% block content %} {# 상속 받을 공간 #}
{% endblock %}
```

3. index.html(자식 템플릿) 변경
   - `{ % extends '' %}` : 자식 템플릿이 부모 템플릿을 확장한다는 것을 알림

```django
<!-- index.html -->
{% extends 'base.html' %}

{% block content %}
<h1>만나서 반가워요!</h1>
<a href="/greeting/">greeting</a>
<a href="/index/">index</a>
{% endblock %}
```



#### 방법 2

1. _nav.html 생성
2. _nav.html에 부트스트랩 작성
3. base.html에서 'include tag' 사용
   - `{% include '_nav.html' %}` 

=> 깔끔

- 템플릿명에 `_`를 사용하는 이유 : 관행적으로 include되는 템플릿을 다른 템플릿들이랑 구분하기 위해



## Django 설계 철학

- 표현과 로직을 분리
  - 템플릿 시스템은 표현을 제어하는 도구이자 표현에 관련된 로직일 뿐이며 이러한 기본 목표를 넘어서는 기능을 지원하지 말아야 한다
- 중복 배제
  - Django 템플릿 시스템은 공통 header, footer, navbar 같은 공통 디자인을 가지며 이러한 요소를 한 곳에 저장하기 슆게 하여 중복 코드를 없애야 한다



## practice

> lotto 번호 무작위 6개 만들기

```python
# views.py

from django.shortcuts import render
import random

# Create your views here.
def lotto(request):
    context = {
        'lottonum': sorted(random.sample(range(1,46), 6))
    }
    return render(request, 'lotto.html', context)
```



```html
<!-- lotto.html -->

<body>
  <h1>당첨번호 : {{ lottonum }}</h1>
</body>
```

