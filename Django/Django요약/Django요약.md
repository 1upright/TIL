# Django요약

> 템플릿 상속을 이용하는 형태로 개발하여 model을 활용하기까지..

1. 폴더 생성 후 vscode 열기

2. bash 터미널에 `$ python -m venv venv`(가상 환경 생성)

3. `$ source venv/Scripts/activate` (가상 환경 활성화)

4. `$ pip install Django==3.2.12` (Django 설치)

5. `$ django-admin startproject pjt .` (프로젝트 생성)

6. `$ python manage.py runserver` (서버 실행)

7. 로켓 확인 후 `ctrl+c`로 서버 종료

8. `$ python manage.py startapp articles` (앱 생성)

9. settings.py의 INSTALLED_APPS에 `'articles',` 집어넣기 (앱 등록)

10. settings.py에서 `LANGUAGE_CODE = 'ko-kr'`, `TIME_ZONE = 'Asia/Seoul'`로 변경

11. URL 설정 분리

    1. articles(앱)에 urls.py를 만든 후 
       - `from django.urls import path`, `from . import views`(필요한 모듈 import)
       - `app_name = 'articles'`(appname 지정)
       - `urlpatterns = []`(받을 url들)
    2. pjt/urls.py에서 `from django.urls import path` => `from django.urls import path, include`
    3. pjt/urls.py의 urlpatterns에 `path('articles/', include('articles.urls')),` 추가

12. UVT 패턴에 의한 요청흐름 만들기

    1. URL

       - urlpatterns에 `path('index/', views.index, name='index')` 집어넣기(경로 설정)

    2. VIEW

       - ```python
         def index(request):
             return render(request, 'articles/index.html')
         ```

       - (request받아 render하는 함수 만들기)

    3. TEMPLATES

       - 템플릿 상속

         1. settings.py의 TEMPLATES의 'DIRS'의 [] 안에 `BASE_DIR / 'templates'` 집어넣기

         2. 처음 만든 폴더에 templates폴더를 만든 후 그 안에 base.html 만들고 상속시킬 내용 작성. 상속시킬 내용 아래에는 `{% block body %} {% endblock body%}` 넣어주기

            ```django
            {# 예시 #}
            <!DOCTYPE html>
            <html lang="en">
            <head>
              <meta charset="UTF-8">
              <meta http-equiv="X-UA-Compatible" content="IE=edge">
              <meta name="viewport" content="width=device-width, initial-scale=1.0">
              <title>django | {% block title %}{% endblock %}</title>
              <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
            </head>
            <body>
              <nav class="navbar navbar-expand-lg navbar-light bg-light">
                <div class="container-fluid">
                  <a class="navbar-brand" href="#">Navbar</a>
                  <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                  </button>
                  <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav">
                      <li class="nav-item">
                        <a class="nav-link" href="{% url 'articles:index' %}">인덱스</a>
                      </li>
                    </ul>
                  </div>
                </div>
              </nav>
            
              {% block body %}
              {% endblock body%}
            
             
              <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
            </body>
            </html>
            
            ```

         3. 이후 만드는 템플릿의 맨 위에 `{% extend 'base.html' %}`을 쓰고 `{% block body %}`와 `{% endblock body %}` 사이에 원하는 내용을 작성해야 한다 

            ```django
            {# 예시 #}
            {% extends 'base.html' %}
            
            {% block body %}
              <h1>안녕</h1>
            {% endblock body %}
            ```

       - articles 내에 templates 폴더 생성 후 articles 폴더 생성(마지막 폴더는 앱이 더 있으면 섞이지 않으려고)

       - articles/templates/articles 내에 index.html 만들기

       - index.html 간단히 작성 후 runserver해서 잘 뜨는지 확인

       - index.html 제대로 작성

13. 이후 새로운 요청받기 만드려면 그때마다 UVT 패턴에 따라 작성

14. models.py 작성

    ```python
    # 예시
    class Article(models.Model):
        title = models.CharField(max_length=30)
        content = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
    ```

15. `$ python manage.py makemigrations` (새로운 마이그레이션 생성)

16. `$ python manage.py migrate` (마이그레이션을 DB에 반영)

17. `$ python manage.py showmigrations`를 통해 마이그레이션 상태 확인(X 표시 뜨면 성공적으로 migrate된 것)

18. admin.py 작성

    ```python
    # admin.py
    from django.contrib import admin
    from .models import Article
    
    # Register your models here.
    admin.site.register(Article)
    ```

18. `$ python manage.py createsuperuser`

18. 사용자 이름, 이메일 주소, password, password(again) 정하고 y

18. db.sqlite3에 Open Database를 해서 잘 되고 있는지 확인

19. 모델을 수정하게 된다면 터미널에서 `1 enter enter` 누르면 디폴트 값으로 필드 설정하여 수정 가능

20. `$ pip install ipython django-extensions`(django extensions 설치)($ pip list로 확인 가능)

20. settings.py의 INSTALLED_APPS에 `'django_extensions',` 집어넣기

21. 이후 모델을 사용하여 UVT 패턴에 따라 개발