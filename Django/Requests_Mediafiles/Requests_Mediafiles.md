# Requests/Media_files

## Handling HTTP requests

#### shortcuts function

- render()

- redirect()

- get_object_or_404()

  - 상황에 따라 적절한 예외처리를 하고 클라이언트에게 올바른 에러 상황을 전달하는 것 또한 개발의 중요한 요소

- get_list_or_404()

- 만약 render가 없었다면?

  ```python
  from django.http import HttpResponse
  from django.template import loader # 이런 것들을 import해서 템플릿을 loader해야 함
  
  def index(request):
      articles = Article.objects.order_by('-pk')
      template = loader.get_template('articles/index.html')
      context = {
          'articles': articles,
      }
      return HttpResponse(template.render(context, request))
  ```

- 만약 get_object_or_404()가 없었다면?

  ```python
  from django.http import Http404 #
  
  def detail(request, pk):
      try:
          article = Article.objects.get(pk=pk)
      except Article.DoesNotExist:
          raise Http404('No Article matches the given query.')
      context = {
          'article': article,
      }
      return render(request, 'articles/detail.html', context)
  ```



#### Django View decorators

> Django는 다양한 HTTP 기능을 지원하기 위해 view 함수에 적용할 수 있는 여러 데코레이터 제공

##### [참고] Decorator(데코레이터)

- 어떤 함수에 기능을 추가하고 싶을 때, 함수를 수정하지 않고 기능을 연장해주는 함수

```python
def myWrapper(func):
    def myInnerFunc():
        print("Inside wrapper.")
        func()
    return myInnerFunc

@myWrapper
def myFunc():
    print("Hello, World!")
    
myFunc()
```

- Allowed HTTP method

  - 요청 메서드에 따라 view 함수에 대한 엑세스 제한
  - 요청이 조건을 충족시키지 못하면 HttpResponseNotAllowed을 return(405 Method Not Allowed)
  - 종류
    - require_http_methods() : view 함수가 특정 method 요청에 대해서만 허용하도록 하는 데코레이터
    - require_POST() : view 함수가 POST method 요청만 승인하도록 하는 데코레이터
    - require_safe() : view 함수가 GET 및 HEAD method만 허용하도록 하는 데코레이터
      - require_GET도 있지만 django는 대신에 require_safe() 쓰는 것을 권장한다

- 적용

  ```python
  # views.py
  
  @require_POST # 이 부분이 if request.method == 'POST'를 대신할 수 있다(else일 경우 405 에러 발생)
  def delete(request, pk):
      article = Article.objects.get(pk=pk)
      article.delete()
      return redirect('articles:index')
  ```



## Media file

> 미디어 파일
>
> 사용자가 웹에서 업로드하는 정적 파일
>
> 유저가 업로드 한 모든 정적 파일

#### ImageField()

- 이미지 업로드에 사용하는 모델 필드
- FileField를 상속받는 서브 클래스이기 때문에 FileField의 모든 속성 및 메서드 사용 가능 + 유효 이미지 검사
- 이미지 파일이 아닌 경로로 저장되므로 최대 길이가 100자인 문자열로 DB에 생성됨



#### FileField()

- 파일 업로드에 사용되는 모델 필드

- 종류

  - upload_to

    - `image = models.ImageField(upload_to='images/', blank=True)`와 같이 사용

      - upload_to='images/' : 실제 이미지가 저장되는 경로
      - blank=True : 이미지 필드에 빈 값이 허용되도록 설정
      - `image = models.ImageField(upload_to='uploads/%Y/%m/%d/')`와 같이 strftime() 형식 포함 가능

    - 반드시 2개의 인자를 사용

      - instance : FileField가 정의한 모델의 인스턴스, 대부분 이 객체는 아직 db에 저장되지 않아 pk값이 없을 수 있음
      - filename : 기존 파일에 제공된 파일 이름

      ```python
      # models.py
      
      def articles_image_path(instance, filename):
          return f'image_{instance.pk}/{filename}'
      
      def Article(models.Model):
          image = models.ImageField(upload_to=articles_image_path)
      ```

    - blank & null

      - blank : 기본 값 False, True인 경우 필드 비워둘 수 있음, 유효성 검사에서 사용
      - null : 기본 값 False, True인 경우 django는 빈 값에 대해 DB에 NULL로 저장
      - 문자열 기반 필드는 빈 문자열에 대해서 blank와 null 모두 저장될 수 있기 때문에 null=True를 사용하지 않는다(blank=True 사용)
      - DataField처럼 문자열 기반 필드가 아니라면 둘 다 사용 가능

  - storage



#### ImageField 사용

1. settings.py에 MEDIA_ROOT, MEDIA_URL 설정

   ```python
   MEDIA_ROOT = BASE_DIR / 'media'
   
   MEDIA_URL = '/media/'
   ```

2. upload_to 속성을 정의하여 업로드 된 파일에 사용할 MEDIA_ROOT의 하위 경로 지정

3. 업로드 된 파일의 경로는 django가 제공하는 'url'속성을 통해 얻을 수 있음

   ```django
   <img src="{{ article.image.url }}" alt="{{ article.image }}">
   ```



- 계발 단계에서 사용자가 업로드한 파일 제공하기

```python
# crud/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings #
from django.conf.urls.static import static #

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles,urls')),
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #
]
```

- ImageField를 사용하기 위해선 Pillow 라이브러리 설치 필요(없으면 마이그레이션시 에러)



#### 이미지 Upload

##### CREATE

```django
<!-- articles/create.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>CREATE</h1>
  <hr>
  <form action="{% url 'articles:create' %}" method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
  <a href="{% url 'articles:index' %}">back</a>
{% endblock content %}
```

- enctype 속성 지정
  - multipart/form-data
    - 파일/이미지 업로드 시 반드시 사용해야함
  - application/x-www-form-urlencoded
  - text/plain
- input 요소 - accept 속성
  - 입렵 허용할 파일 유형을 나타내는 문자열
  - 파일을 검증하는 것이 아님
  - 고유 파일 유형 지정자
  - 파일 업로드 시 허용할 파일 형식에 대해 자동으로 필터링
- views.py 수정 : 업로드 한 파일은 request.FILES 객체로 전달됨

```python
# views.py
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
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



##### READ

- article.image.url : 업로드 파일의 경로
- article.image : 업로드 파일의 파일 이름
- static, media 파일 모두 서버에서 요청해서 조회하는 것(서버 요청 위해 url 필요)



##### UPDATE

- 이미지는 바이너리 데이터(하나의 덩어리)이기 때문에 텍스트처럼 일부만 수정하는 것이 불가능
- 새로운 사진으로 덮어 씌우는 방식 사용

```django
<!-- articles/create.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>UPDATE</h1>
  <hr>
  <form action="{% url 'articles:update' article.pk %}" method="POST" enctype="multipart/form-data"> {##}
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
  <a href="{% url 'articles:detail' article.pk %}">back</a>
{% endblock content %}
```

```python
# views.py
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES,instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)
```



#### 이미지 Resizing

##### 이미지 크기 변경

- 실제 원본 이미지를 서버에 그대로 업로드 하는 것은 서버의 부담이 큰 작업
- `<img>` 태그에서 직접 사이즈 조정할 수 있지만 업로드될 때 이미지 자체를 resizing 하는 방법 고려!
  - django-imagekit 라이브러리 활용
- 방법
  - django-imagekit 설치
  - INSTALLED_APPS에 추가

```python
# models.py

from distutils.command.upload import upload
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    # image = models.ImageField(upload_to='images/', blank=True)
    image = ProcessedImageField(
        blank=True,
        upload_to='thumbnails/',
        processors=[Thumbnail(200, 300)],
        format='JPEG',
        options={'quality': 60}
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
```

- django-imagekit 라이브러리 문서 참고

- ProcessedImageField()의 parameter로 작성된 값들은 변경하더라도 다시 makemigrations를 해줄 필요 없이 즉시 반영됨

- 추가된 ImageSpecField() 사용

  ```django
  <!-- detail.html -->
  <img src="{{ article.image_thumbnail.url }}" alt="{{ article.image_thumbnail }}">
  ```
