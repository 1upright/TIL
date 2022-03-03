# Django기초2



## HTML Form

#### element

- form 
  - action : 입력 데이터가 전송될 URL 지정(폼을 처리할 URL)
  - method : 입력 데이터 전달 방식 지정(GET/POST)

- input 

  - id : label for 연결
  - type : 다양한 타입 (radio, text, email, password)

  - name : 핵심 속성, 값(value)을 담는 이름(변수 이름)

- label

  - for : input id 연결



#### 예시) throw & catch

```python
# views.py

def throw(request):
    return render(request, 'throw.html')

def catch(request):
    message = request.GET.get('message') # request.GET에서 'message'라는 키에 대한 값
    context = {
        'message': message # 템플릿(catch.html)에 넘겨줌
    }
    return render(request, 'catch.html', context)
```



```django
<!-- throw.html -->
<form action="/catch/" method="GET"> {# form에 정의된 action의 URL(/catch/)로 폼 전송 #}
  <label for="message">메시지 :</label>
  <input type="text" id="message" name="message"> {# name을 이름으로 message값 전달 #}
  <input type="submit" value="얍!">
</form>
```



```django
<!-- catch.html -->
<h1>{{ message }}</h1>
<a href="/throw/">다시 던지기</a>
```



## Variable Routing

> URL 주소를 변수로 사용하는 것
>
> URL의 일부를 변수로 지정하여 view 함수의 인자로 넘길 수 있다

- `path('accounts/user/<int:user_pk>/', ...)`와 같이 사용 가능
- path converters
  - str : 문자열, 작성하지 않을 경우 기본 값
  - int : 0 또는 양의 정수와 매치
  - slug : ASCII 문자 또는 숫자, 하이픈 및 밑줄 문자로 구성된 모든 슬러그 문자열과 매치
  - uuid
  - path



#### 예시)

```python
# urls.py

from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dinner/<menu>/<int:num>/', views.dinner),
]
```



```python
# views.py

def dinner(request, menu, num):
    context = {
        'menu': menu,
        'num': num,
    }
    return render(request, 'dinner.html', context)
```



```django
<!-- dinner.html -->
<body>
  <h1>저녁 메뉴</h1>
  <h1>저녁 먹을 사람?! {{ num }}명</h1>
  <h1>어떤 메뉴?! {{ menu }}</h1>
</body>
```

- 접속예시 : http://127.0.0.1:8000/dinner/chicken/6



## App URL mapping

- 등장배경
  1. app의 view 함수가 많아지면서 사용하는 path() 또한 많아지고, app 또한 더 많이 작성됨
  2. 프로젝트의 urls.py에서 이를 모두 관리하는 것은 프로젝트 유지보수에 좋지 않음
  3. 각 app에 urls.py를 작성해볼까?



#### 방법 1

> articles 앱 생성 및 등록 후 url 작성

```python
# firstpjt/urls.py

from articles import views as articles_views
from pages import views as pages_views

urlpatterns = [
    path('pages-lunch', pages_views.lunch),
    ...
]
```



#### 방법 2 - Naming URL patterns

> path() 함수의 name 인자를 정의해서 사용
>
> Django Template Tag 중 하나인 url 태그 사용 가능 => `{% url 'lunch' %}`



```python
# firstpjt/urls.py (다 쳐내졌음)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
]
```



```python
# articles/urls.py (! firstpjc/urls.py가 아님 !)
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('lunch/', views.index, name='index'),
    path('throw/', views.throw, name='throw'),
    path('catach/', views.catch, name='catch'),
]
```



```django
<!-- throw.html -->
<form action="{% url 'articles:catch' %}" method="GET"> {# url 태그 사용 #}
  <label for="message">메시지 :</label>
  <input type="text" id="message" name="message">
  <input type="submit" value="얍!">
```



```django
<!-- catch.html -->
<h1>{{ message }}</h1>
<a href="/throw/">다시 던지기</a>
<a href="{% url 'articles:throw' %}">다시 던지기</a>
<a href="/">홈</a>
```

