# REST API

## HTTP

#### URL(Uniform Resource Locator)

- 통합 자원 위치
- 네트워크 상에 자원이 어디 있는지 알려주기 위한 약속
- 과거에는 실제 자원의 위치를 나타냈지만 현재는 추상화된 의미론적인 구성
- 웹주소, 링크

#### URN(Uniform Resource Name)

- 통합 자원 이름
- URL과 달리 자원의 위치에 영향을 받지 않는 유일한 이름 역할
- 잘 안씀

#### URI(Uniform Resource Identifier)

- 통합 자원 식별자
- 인터넷 자원을 식별하는 유일한 주소
- 인터넷에서 자원을 식별하거나 이름을 지정하는데 사용되는 간단한 문자열
- URL, URN의 상위 개념이지만 URN의 사용 비중이 적어 URI와 같은 의미로 사용하기도 함
- 구조
  - Scheme
    - 브라우저가 사용해야 하는 프로토콜
    - http(s), data, file, ftp, malito
  - Host
    - 요청을 받는 웹 서버의 이름
    - IP address를 직접 사용할 수도 있지만 실 사용시 불편하므로 웹에서 자주 사용되지 않음
    - google의 IP address == 142.251.42.142
  - Port
    - 웹 서버 상의 리소스에 접근하는데 사용되는 기술적인 문(gate)
    - HTTP 프로토콜 표준 포트
      - HTTP 80
      - HTTPS 443
  - Path
    - 웹 서버 상의 리소스 경로
    - 초기에는 실제 파일이 위치한 물리적 위치를 나타냈지만, 오늘날은 실제 위치가 아닌 추상화 형태의 구조로 표현
  - Query(Identifier)
    - Query String Parameters
    - 웹 서버에 제공되는 추가적인 매개 변수
  - Fragment
    - Anchor
    - 자원 안에서의 북마크의 한 종류를 나타냄
    - 브라우저에게 해당 문서의 특정 부분을 보여주기 위한 방법
    - 브라우저에게 알려주는 요소이기 때문에 fragment identifier(부분 식별자)라고 부르며, '#' 뒤의 부분은 요청이 서버에 보내지지 않음



## RESTful API

#### API

- Application Programming Interface
- 프로그래밍 언어가 제공하는 기능을 수행할 수 있게 만든 인터페이스
- Web API
  - 웹 애플리케이션 개발에서 다른 서비스에 요청을 보내고 응답을 받기 위해 정의된 명세
- 응답 데이터 타입
  - HTML, XML, JSON 등
- 대표적인 API 서비스
  - Youtube API, Naver Papago API, Kakao Map API



#### REST

- REpresentational State Transter
- API Server를 개발하기 위한 일종의 소프트웨어 설계 방법론
- 네트워크 구조 원리의 모음
  - 자원을 정의하고 자원에 대한 주소를 지정하는 전반적인 방법
- REST 원리 따르는 시스템을 RESTful이란 용어로 지칭
- 자원과 주소의 지정 방법
  - 자원 : URI
  - 행위 : HTTP Method
  - 표현 : 자원의 행위를 통해 궁극적으로 표현되는 결과물, JSON으로 표현된 데이터 제공
- JSON(JavaScript Object Notation)
  - lightweight data-interchange format
- 핵심 규칙
  - 정보는 URI로 표현
  - 자원에 대한 행위는 HTTP Method로 표현(GET, POST, PUT, DELETE)
- Google로 로그인, Naver로 로그인~ 이런 것들이 REST API의 일종



## Response

#### 기본

- settings.py에 설치된 앱

  ```python
  # settings.py
  
  INSTALLED_APPS = [
      'articles',
      'django_seed',
      ...
  ]
  ```

  - 쿼리셋 => serialization => 중간과정 => json/XML 등 다른 데이터 타입

- 작성된 url

  ```python
  # my_api/urls.py
  
  from django.contrib import admin
  from django.urls import path, include
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('api/v1/', include('articles.urls')),
  ]
  ```

  ```python
  # articles/urls.py
  
  from django.urls import path
  from . import views
  
  urlpatterns = [
      path('html/', views.article_html), #1
      path('json-1/', views.article_json_1), #2
      path('json-2/', views.article_json_2), #3
      path('json-3/', views.article_json_3), #4
  ]
  ```

- 작성된 model

  ```python
  # article/models.py
  
  from django.db import models
  
  # Create your models here.
  class Article(models.Model):
      title = models.CharField(max_length=100)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  ```



#### 1. Response - HTML

```python
# articles/views.py

def article_html(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/article.html', context)
```

```django
<!-- articles/article.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>Article List</h1>
  <hr>
  <p>
    {% for article in articles %}
      <h2>{{ article.pk }}번 글. {{ article.title }}</h2>
      <p>{{ article.content }}</p>
      <hr>
    {% endfor %}
  </p>
</body>
</html>
```



#### 2. Response - JsonResponse

```python
# articles/views.py

from django.http.response import JsonResponse

def article_json_1(request):
    articles = Article.objects.all()
    articles_json = []

    for article in articles:
        articles_json.append(
            {
                'id': article.pk,
                'title': article.title,
                'content': article.content,
                'created_at': article.created_at,
                'updated_at': article.updated_at,
            }
        )
    return JsonResponse(articles_json, safe=False)
```

- Content-Type entity hearder

  - 데이터의 media type을 나타내기 위해 사용
  - 응답 내에 있는 컨텐츠의 컨텐츠 유형이 실제로 무엇인지 클라리언트에  알려줌

- JsonResponse objects

  - JSON-encoded response를 만드는 HttpResponse의 서브 클래스

  - "safe" parameter

    - 기본값 : True
    - dict 이외의 객체를 직렬화하려면 False로 설정해야 함

    ```python
    # JsonResponse 예시
    
    response = JsonResponse({'foo': 'bar'})
    response = JsonResponse([1, 2, 3], safe=False)
    ```




#### 3. Response - Django Serializer

```python
# articles/views.py

from django.http.response import JsonResponse, HttpResponse
from django.core import serializers

def article_json_2(request):
    articles = Article.objects.all()
    data = serializers.serialize('json', articles)
    return HttpResponse(data, content_type='application/json')
```

- Serialization(직렬화)
  - 데이터 구조나 객체 상태를 동일하거나 다른 컴퓨터 환경에 저장하고, 나중에 재구성할 수 있는 포맷으로 변환하는 과정
  - Django ModelSrializer는 파이썬 article, user 혹읜 queryset의 객체를 JSON으로 변환해주는 것을 말한다
    - 주어진 모델 정보를 활용하기 때문에 이전과 달리 필드를 개별적으로 만들어 줄 필요가 없다



#### 4. Response - Django REST Framework

- Django REST framework(DRF) 라이브러리를 사용한 JSON 응답
- djangorestramework 설치

```python
# settings.py
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

```python
# articles/serializers.py

from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'
```

```python
# articles/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArticleSerializer

# @api_view(['GET'])
@api_view()
def article_json_3(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)
```

- ArticleSerializer의 many=True는 단일 객체가 아닐 때 사용
- Django REST Framework(DRF)
  - Web API 구축을 위한 강력한 Toolkit을 제공하는 라이브러리
  - DRF의 Serializer는 Django의 Form 및 ModelForm 클래스와 매우 유사하게 구성되고 작동함
  - 쿼리셋 => serialization => 중간과정 => json/XML 등 다른 데이터 타입



## Single Model

> 단일 모델의 data를 serialization하여 JSON으로 변환하는 방법에 대한 학습
>
> 단일 모델에 대한 CRUD
>
> Postman 이용하여 설계

#### 1. Init Project

- 가상환경 설정 및 패키지 설치

- 설치된 app

  ```python
  # settings.py
  INSTALLED_APPS = [
      'articles',
      'django_seed',
      'django_extensions',
      'rest_framework',
  ]
  ```

- 작성된 url

  ```python
  # my_api/urls.py
  
  from django.contrib import admin
  from django.urls import path, include
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('api/v1/', include('articles.urls')),
  ]
  ```

  ```python
  # articles/urls.py
  
  from django.urls import path
  from . import views
  
  urlpatterns = [
  
  ]
  ```
  
- 작성된 model

  ```python
  # article/models.py
  
  from django.db import models
  
  # Create your models here.
  class Article(models.Model):
      title = models.CharField(max_length=100)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  ```



#### 2. Create Dummy Data

```bash
$ python manage.py migrate
$ python manage.py seed articles --number=20
```



#### 3. ModelSerializer

- 모델 필드에 해당하는 필드가 있는 Serializer 클래스를 자동으로 만들 수 있는 shortcut
- 핵심 기능
  - 모델 정보에 맞춰 자동으로 필드 생성
  - serializer에 대한 유효성 검사기를 자동으로 생성

```python
# articles/serializers.py

from rest_framework import serializers
from .models import Article


class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title',)
```



#### 4. 기능 구현

##### GET - Article List

```python
# articles/urls.py

urlpatterns = [
    path('articles/', views.article_list),
]
```

```python
# articles/views.py

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_list_or_404, get_object_or_404
from .serializers import ArticleListSerializer, ArticleSerializer
from .models import Article, Comment

@api_view(['GET', 'POST']) # 1
def article_list(request):
    if request.method == 'GET':
        # articles = Article.objects.all()
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # print(request.data)
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

- `@api_view` (1)
  - 기본적으로 GET 메서드만 허용되며 다른 메서드 요청에 대해서는 405 Method Not Allowed로 응답
  - View 함수가 응답해야 하는 HTTP 메서드의 목록을 리스트의 인자로 받음
  - DRF에서는 선택이 아닌 필수적으로 작성해야 해당 view 함수가 정상적으로 동작
- Postman에서 `http://127.0.0.1:8000/api/v1/articles/`로 GET 요청 후 응답 확인



##### GET - Article Detail

- Article List와 Article Detail을 구분하기 위해 추가 Serializer 정의

- 모든 필드를 직렬화하기 위해 fields 옵션을 `'__all__'`로 설정

  ```python
  # articles/serializers.py
  
  class ArticleSerializer(serializers.ModelSerializer):
      # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
      comment_set = CommentSerializer(many=True, read_only=True)
      comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
  
      class Meta:
          model = Article
          fields = '__all__'
  ```

- url 및 view

  ```python
    # articles/urls.py
    
    urlpatterns = [
        path('articles/<int:article_pk>/', views.article_detail),
    ]
  ```
  
    ```python
    # articles/views.py
    
    from django.shortcuts import get_list_or_404, get_object_or_404
    from .serializers import ArticleListSerializer, ArticleSerializer
    
    @api_view(['GET'])
    def article_detail(request, article_pk):
        article = get_object_or_404(Article, pk=article_pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    ```
  
- Postman에서 `http://127.0.0.1:8000/api/v1/articles/1/`로 GET 요청 후 응답 확인



##### 3. POST - Create Article

- 201 Created 상태 코드 및 메시지 응답

- article_list 함수로 게시글을 조회하거나 생성하는 행위 모두 처리 가능

- view 함수 수정

  ```python
  # articles/views.py
  
  from rest_framework import status
  
  @api_view(['GET', 'POST'])
  def article_list(request):
      if request.method == 'GET':
          # articles = Article.objects.all()
          articles = get_list_or_404(Article)
          serializer = ArticleListSerializer(articles, many=True)
          return Response(serializer.data)
  
      elif request.method == 'POST':
          # print(request.data)
          serializer = ArticleSerializer(data=request.data)
          if serializer.is_valid(raise_exception=True): #2
              serializer.save()
              return Response(serializer.data, status=status.HTTP_201_CREATED) #1
          # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  ```

- status codes (1)

  - DRF에는 status code를 보다 명확하고 읽기 쉽게 만드는 데 사용할 수 있는 정의된 상수 집합 제공
  - status 모듈에 HTTP status code 집합이 모두 포함되어 있다
  - `Response(serializer.data, status=201)`과 같이 표현할 수도 있지만 DRF에서 권장되지 않음
  - status를 import해 사용하며 원하는 상태를 만들어내는 것

- Postman에서 `http://127.0.0.1:8000/api/v1/articles/`로 POST 요청 후 응답 확인

  - body의 form-data에 작성하여 요청

- `raise_exception` argument (2)

  - is_valid()를 이용한 유효성 검사 오류가 있는 경우 serializers.ValidationError 예외를 발생시키는 선택적 raise_exception 인자 사용이 가능
  - HTTP status code 400 응답 반환
    - 400 status code를 응답하는 return 구문을 삭제해도 된다



##### DELETE - Delete Article

- 204 No Content 상태 코드 및 메시지 응답

- article_detail 함수로 상세 게시글을 조회하거나 삭제하는 행위 모두 처리 가능

  ```python
  # articles/views.py
  
  @api_view(['GET', 'DELETE'])
  def article_detail(request, article_pk):
      article = get_object_or_404(Article, pk=article_pk)
  
      if request.method == 'GET':
          serializer = ArticleSerializer(article)
          return Response(serializer.data)
  
      elif request.method == 'DELETE':
          article.delete()
          data = {
              'delete': f'데이터 {article_pk}번이 삭제되었습니다.',
          }
          return Response(data, status=status.HTTP_204_NO_CONTENT)
  ```

- Postman에서 `http://127.0.0.1:8000/api/v1/articles/1/`로 DELETE 요청 후 응답 확인



##### PUT - Update Article

- article_detail 함수로 상세 게시글을 조회하거나 삭제, 수정하는 행위 모두 처리 가능

  ```python
  # articles/views.py
  
  @api_view(['GET', 'DELETE', 'PUT'])
  def article_detail(request, article_pk):
      article = get_object_or_404(Article, pk=article_pk)
  
      if request.method == 'GET':
          serializer = ArticleSerializer(article)
          return Response(serializer.data)
  
      elif request.method == 'DELETE':
          article.delete()
          data = {
              'delete': f'데이터 {article_pk}번이 삭제되었습니다.',
          }
          return Response(data, status=status.HTTP_204_NO_CONTENT)
  
      elif request.method == 'PUT':
          serializer = ArticleSerializer(article, request.data)
          # serializer = ArticleSerializer(article, data=request.data)
          if serializer.is_valid(raise_exception=True):
              serializer.save()
              return Response(serializer.data)
  ```

- Postman에서 `http://127.0.0.1:8000/api/v1/articles/1/`로 PUT 요청 후 응답 확인



## 1:N Relation

> Comment 기능 구현

- Comment 모델

  ```python
  # articles/models.py
  
  class Comment(models.Model):
      article = models.ForeignKey(Article, on_delete=models.CASCADE)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  ```

- CommentSerializer 작성

  ```python
  # articles/serializers.py
  
  class CommentSerializer(serializers.ModelSerializer):
  
      class Meta:
          model = Comment
          fields = '__all__'
  ```



#### GET - Comment List

- url, view 작성

  ```python
  # articles/urls.py
  
  urlpatterns = [
      path('comments/', views.comment_list),
  ]
  ```

  ```python
  # articles/views.py
  
  from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
  from .models import Article, Comment
  
  @api_view(['GET'])
  def comment_list(request):
      comments = get_list_or_404(Comment)
      serializer = CommentSerializer(comments, many=True)
      return Response(serializer.data)
  ```

- Postman에서 `http://127.0.0.1:8000/api/v1/comments/`로 GET 요청 후 응답 확인



#### GET - Comment Detail

- url, view 작성

  ```python
  # articles/urls.py
  
  urlpatterns = [
      path('comments/<int:comment_pk>/', views.comment_detail),
  ]
  ```

  ```python
  # articles/views.py
  
  @api_view(['GET'])
  def comment_detail(request, comment_pk):
      comment = get_object_or_404(Comment, pk=comment_pk)
      serializer = CommentSerializer(comment)
      return Response(serializer.data)
  ```

- Postman에서 `http://127.0.0.1:8000/api/v1/comments/1/`로 GET 요청 후 응답 확인



#### POST - Create Comment

- url, view 작성

  ```python
  # articles/urls.py
  
  urlpatterns = [
      path('articles/<int:article_pk>/comments/', views.comment_create),
  ]
  ```

  ```python
  # articles/views.py
  
  @api_view(['POST'])
  def comment_create(request, article_pk):
      article = get_object_or_404(Article, pk=article_pk)
      serializer = CommentSerializer(data=request.data)
      if serializer.is_valid(raise_exception=True):
          serializer.save(article=article) #1
          return Response(serializer.data, status=status.HTTP_201_CREATED)
  ```

- .save() 메서으 안에 인스턴스를 저장하는 과정에서 추가적인 데이터를 받을 수 있다

  - 인스턴스를 저장하는 시점에 추가 데이터 삽입이 필요한 경우
  - 위의 경우 save하기 전 article에 대한 정보가 없기 때문

- Postman에서 `http://127.0.0.1:8000/api/v1/articles/1/comments`로 POST 요청 후 응답 확인

  - 어떤 게시글에 작성하는 댓글인지에 대한 정보를 form-data로 넘겨주지 않았기 때문에 유효성 검사를 통과하지 못함

  - => **읽기 전용 필드(read_only_fields) 설정을 통해 직렬화하지 않고 반환 값에만 해당 필드가 포함되도록 설정해야함**

    ```python
    
    class CommentSerializer(serializers.ModelSerializer):
    
        class Meta:
            model = Comment
            fields = '__all__'
            read_only_fields = ('article',) #
    ```

- Postman에서 `http://127.0.0.1:8000/api/v1/articles/1/comments`로 POST 요청 재시도 후 확인



#### DELETE & PUT - delete, update Comment

- view

  ```python
  # articles/views.py
  
  @api_view(['GET', 'DELETE', 'PUT'])
  def comment_detail(request, comment_pk):
      comment = get_object_or_404(Comment, pk=comment_pk)
      
      if request.method == 'GET':
          serializer = CommentSerializer(comment)
          return Response(serializer.data) 
  
      elif request.method == 'DELETE':
          comment.delete()
          data = {
              'delete': f'데이터 {comment_pk}번이 삭제되었습니다.',
          }
          return Response(data, status=status.HTTP_204_NO_CONTENT)
  
      elif request.method == 'PUT':
          serializer = CommentSerializer(comment, request.data)
          # serializer = CommentSerializer(comment, data=request.data)
          if serializer.is_valid(raise_exception=True):
              serializer.save()
              return Response(serializer.data)
  ```

- Postman에서 `http://127.0.0.1:8000/api/v1/comments/1/`로 DELETE/PUT 요청 후 응답 확인



#### 특정 게시글에 작성된 댓글 목록 출력하기

##### 1. PrimaryKeyRelatedField

- pk를 사용하여 관계된 대상을 나타내는데 사용 가능
  - article.comment_set.all() 게시물 pk를 받아서 comment 출력하는 느낌
- 필드가 to many relationships를 나타내는데 사용되는 경우 many=True 속성 필요
- comment_set 필드 값을 form-data로 받지 않으므로 read_only=True 설정 필요
  - comment_set는 사용자로부터 받는 것이 아니라 조회만 되어야하지만 `fields = '__all__'` 안에 있는 것이 아니므로 read_only="True"가 PrimaryKeyRelatedField() 안에 들어간 것

```python
# articles/serializers.py

class ArticleSerializer(serializers.ModelSerializer):
    comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
```

- Postman에서 `http://127.0.0.1:8000/api/v1/articles/1/`로 GET 요청 후 응답 확인



##### 2. Nested relationships

- 모델 관계상으로 참조된 대상은 참조하는 대상의 응답에 포함되거나 중첩될 수 있음

  - 예시에서는 참조된 대상 == Article, 참조하는 대상 == Comment

- 이러한 중첩된 관계는 필드로 사용하여 표현 가능

  - PrimaryKeyRelatedField 대신 CommentSerializer로 사용 가능
  - 결과가 조금 달라지긴 함
    - 1번은 id만 가져 오지만 2번은 id와 내용, 생성 날짜 등 모든 필드 값을 다 가져옴
      - 다 가져오고 싶을 때 2번, JSON이 복잡해지는 것이 싫으면 1번

  ```python
  # articles/serializers.py
  
  class CommentSerializer(serializers.ModelSerializer):
  
      class Meta:
          model = Comment
          fields = '__all__'
          read_only_fields = ('article',)
  
  
  class ArticleSerializer(serializers.ModelSerializer):
      comment_set = CommentSerializer(many=True, read_only=True)
  
      class Meta:
          model = Article
          fields = '__all__'
  ```

- Postman에서 `http://127.0.0.1:8000/api/v1/articles/1/`로 GET 요청 후 응답 확인



#### 특정 게시글에 작성된 댓글의 개수 구하기

- comment_set 매니저는 모델 관계로 인해 자동으로 구성되므로 커스텀 필드를 구성하지 않아도 comment_set이라는 필드명을 fields 옵션에 작성하면 사용 가능했었음

- 지금처럼 별도의 값을 위한 필드를 사용하려는 경우 자동으로 구성되는 매니저가 아니므로 직접 필드를 작성해야 함

  ```python
  # articles/serializers.py
  
  class ArticleSerializer(serializers.ModelSerializer):
      # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
      comment_set = CommentSerializer(many=True, read_only=True)
      comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
  
      class Meta:
          model = Article
          fields = '__all__'
  ```

- `source` arguments

  - 필드를 채우는데 사용할 속성 이름
  - 점 표기법을 사용하여 속성을 탐색할 수 있음
  - .count()는 built-in Queryset API 중 하나

- Postman에서 `http://127.0.0.1:8000/api/v1/articles/1/`로 GET 요청 후 응답 확인