# API서버활용

- 서버
  - 클라이언트에게 '정보'와 '서비스' 즉 '리소스'를 제공하는 컴퓨터 시스템



## 시작 전

> Model과 Serializer 작성

```python
# articles/models.py

from django.db import models
from django.conf import settings

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

```python
# articles/serializers/article.py

from rest_framework import serializers
from django.contrib.auth import get_user_model

from ..models import Article
from .comment import CommentSerializer

User = get_user_model()


class ArticleSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    comments = CommentSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)
    like_users = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Article
        fields = ('pk', 'user', 'title', 'content', 'comments', 'like_users')


# Article List Read
class ArticleListSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)
    # queryset annotate (views에서 채워줄것!)
    comment_count = serializers.IntegerField()
    like_count = serializers.IntegerField()

    class Meta:
        model = Article
        fields = ('pk', 'user', 'title', 'comment_count', 'like_count')
```

```python
# articles/serializers/comment.py

from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import Comment

User = get_user_model()

class CommentSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('pk', 'user', 'content', 'article',)
        read_only_fields = ('article', )
```

```python
# accounts/serializers.py

from rest_framework import serializers
from django.contrib.auth import get_user_model
from articles.models import Article

class ProfileSerializer(serializers.ModelSerializer):

    class ArticleSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Article
            fields = ('pk', 'title', 'content')

    like_articles = ArticleSerializer(many=True)
    articles = ArticleSerializer(many=True)

    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'email', 'like_articles', 'articles',)
```



## CORS

#### Same-Origin Policy(SOP)

- 동일 출처 정책

- 특정 출처에서 불러온 문서나 스크립트가 다른 출처에서 가져온 리소스와 상호작용하는 것을 제한하는 보안 방식

- Origin(출처)

  - 두 URL의 Protocol, Port, Host가 모두 같아야 동일한 출처

  ![origin](API%EC%84%9C%EB%B2%84%ED%99%9C%EC%9A%A9.assets/origin.PNG)

- 잠재적으로 해로울 수 있는 문서를 분리함으로써 공격받을 수 잇는 경로를 줄임

- 8000에서는 8000에서 불러온 문서만 받아주고 8001에서는 8001에서 불러온 문서만 받아주는 식



#### Cross-Origin Resource Sharing(CORS)

- 교차 출처 리소스(자원) 공유
- **추가 HTTP header를 사용**하여, 특정 출처에서 실행중인 웹 어플리케이션이 **다른 출처의 자원에 접근할 수 있는 권한을 부여**하도록 브라우저에 알려주는 체제
- 리소스가 자신의 출처와 다를 때 교차 출처 HTTP 요청을 실행
- 보안 상의 이유로 브라우저는 교차 출처 HTTP 요청을 제한
- 다른 출처의 리소스를 불러오려면 그 출처에서 올바른 CORS header를 포함한 응답을 반환해야 함
- CORS Policy
  - 교차 출처 리소스(자원) 공유 정책
  - 다른 출처에서 온 리소스를 공유하는 것에 대한 정책 <=> SOP
- 교차 출처 접근 허용
  - CORS는 HTTP의 일부로, 어떤 호스트에서 자신의 컨텐츠를 불러갈 수 있는지 서버에 지정할 수 있는 방법
- 왜 CORS인가?
  - 브라우저 & 웹 애플리케이션 보호
    - 악의적인 사이트의 데이터를 가져오지 않도록 사전 차단
    - 응답으로 받는 자원에 대한 최소한의 검증
    - 서버는 정상적으로 응답하지만 브라우저에서 차단
  - Server의 자원 관리
    - 누가 해당 리소스에 접근할 수 있는지 관리 가능
- 어떻게 쓸까?
  - CORS 표준에 의해 추가된 HTTP Header를 통해 이를 통제



#### Access-Control-Allow-Origin 응답 헤더

- 이 응답이 주어진 출처로부터 요청 코드와 공유될 수 있는지를 나타냄
- 예시
  - Access-Control-Allow-Origin: *
    - 브라우저 리소스에 접근하는 임의의 origin으로부터 요청을 허용한다고 알리는 응답에 포함



#### CORS 시나리오 예시

- `https://localhost:8080(Vue.js)`의 웹 컨텐츠가 `https://lab.ssafy.com(Django)` 도메인의 컨텐츠를 호출하기를 원하는 상황이라면?
  - 요청 헤더의 Origin을 보면 localhost:8080으로부터 요청이 온 것을 확인 가능
  - 서버는 이에 대한 응답으로 Access-Control-Allow-Origin 응답 헤더 다시 전송
    - localhost:8080의 요청만 접근을 허용하려면? Access-Control-Allow-Origin: localhost:8080

1. Vue.js에서 A 서버로 요청
2. A서버는 Access-Control-Allow-Origin에 특정한 origin을 포함시켜 응답
   - 서버는 CORS Policy와 직접적인 연관이 없고 그저 요청에 응답
3. 브라우저는 응답에서 Access-Control-Allow-Origin을 확인한 후 허용 여부 결정
4. 프레임워크 별로 이를 지원하는 라이브러리 존재
   - django는 django-cors-headers 라이브러리를 통해 응답 헤더 및 추가 설정 가능



#### django-cors-headers 라이브러리

- 응답에 CORS header를 추가해주는 라이브러리

- 다른 출처에서 보내는 Django 애플리케이션에 대한 브라우저 내 요청 허용

- Django App이 header 정보에 CORS를 설정한 상태로 응답을 줄 수 있게 도와주며, 이 설정을 통해 브라우저는 다른 origin에서 요청을 보내는 것이 가능해짐

  ```bassh
  pip install django-cors-headers
  ```

  ```python
  # settings.py
  
  INSTALLED_APPS = [
      ...
  	'corsheaders',
      ...
  ]
  
  ...
  
  MIDDLEWARE = [
      'corsheaders.middleware.CorsMiddleware', # CommonMiddleware보다 위에 있어야 함
  	...
      'django.middleware.common.CommonMiddleware',
  	...
  ]
  
  ...
  
  # 특정 origin 에게만 교차 출처 허용
  CORS_ALLOWED_ORIGINS = [
      # Vue LocalHost
      'http://localhost:8080',
      'http://127.0.0.1:8001',
  ]
  
  # or 모두에게 교차출처 허용
  # CORS_ALLOW_ALL_ORIGINS = True
  ```

  

## Authentication & Authorization

#### Authentication

> verifying who a user is

- 인증, 입증
- 자신이라고 주장하는 사용자가 누구인지 확인하는 행위
- 모든 보안 프로세스의 첫 번째 단계
- 내가 누구인지를 확인하는 과정
- 401 Unauthorized
  - HTTP 표준에서는 '미승인(unauthorized)'을 하고 있지만, 의미상 이 응답은 '비인증(unauthenticated)'을 의미



#### Authorization

> verifying what they have access to

- 권한 부여, 허가
- 사용자에게 특정 리소스 또는 기능에 대한 액세스 권한을 부여하는 과정(절차)
- 보안 환경에서 권한 부여는 항상 인증을 따라야 함
- 서류의 등급, 웹 페이지에서 글을 CRUD하는 방법, 제한 구역
  - 인증이 되었어도 모든 권한을 부여받는 것이 아님
- 403 Forbidden
  - 401과 다른 점 : 서버는 클라이언트가 누구인지 알고 있다는 것



## DRF Authentication

#### 다양한 인증 방식

- Session Based
- Token Based
  - Basic Token
    - 이걸 쓸거임
  - JWT
    - 이거 왜 안써요? => 털리면 서버 측에서 지켜줄 수 없는 방식이라..
- Oauth
  - google
  - facebook
  - github
  - 그 외 많음



#### Basic Token Based

1. POST /login {username, password} (C => S)
2. token 테이블에 저장
3. token 값 응답 (S => C)
4. 브라우저에 token 정보 저장
5. Request Header에 토큰과 함께 요청
6. token 값을 token 테이블에서 확인 후 로그인
7. 응답



#### JWT

- Json Web Token
- JSON 포맷을 활용하여 요소 간 안전하게 정보를 교환하기 위한 표준 포맷
- 암호화 알고리즘에 의한 디지털 서명이 되어 있기 때문에 JWT 자체로 검증 가능
- JWT 자체가 필요한 정보를 모두 갖기 때문에 이를 검증하기 위한 다른 검증 수단이 필요 없음
- 기본 토큰 인증 체계와 달리 JWT 인증 확인은 데이터베이스를 사용하여 토큰의 유효성을 검사할 필요가 없음



#### dj-rest-auth & django-allauth

```bash
$ pip install django-allauth
$ pip install dj-rest-auth
```

```python
# settings.py

INSTALLED_APPS = [
    # local apps(원래 있던거)
    'accounts',
    'articles',
    # 3rd party apps
    'django_extensions',
    
    'rest_framework',
    'rest_framework.authtoken',  # token 기반 auth
    # DRF auth
    'dj_rest_auth',  # signup 제외 auth 관련 담당
    'dj_rest_auth.registration',  # signup 담당

    # signup 담당을 위해 필요 
    'allauth', 
    'allauth.account',
    'allauth.socialaccount',

    # CORS 세팅(원래 있던거)
    'corsheaders',

    # native apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',  # dj-rest-auth signup 필요
]

SITE_ID = 1

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        # 모두에게 허용
        # 'rest_framework.permissions.AllowAny', 

        # 인증된 사용자만 모든일이 가능(로그인, 회원가입 빼고) / 비인증 사용자는 모두 401 Unauthorized
        'rest_framework.permissions.IsAuthenticated'
    ]
}
```

```python
# urls.py

...
urlpatterns = [
	...
    path('api/v1/accounts/', include('dj_rest_auth.urls')),
    path('api/v1/accounts/signup/', include('dj_rest_auth.registration.urls')),
]
```