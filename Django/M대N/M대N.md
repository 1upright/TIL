# M:N

## 병원 진료 기록 시스템

> 여러 의사와 여러 환자가 있다. 의사는 여러 환자를 진료하고 환자는 여러 의사에게 진찰받을 수 있다. 둘의 관계를 어떻게 표현할 수 있을까?



#### 중개 모델

```python
from django.db import models

class Doctor(models.Model):
    name = models.TextField()
    
class Patient(models.Model):
    name = models.TextField()
  
class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
```



## ManyToManyField

> M:N 관계 설정 시 사용하는 모델 필드

```python
from django.db import models

class Doctor(models.Model):
    name = models.TextField()
    
class Patient(models.Model):
    doctors = models.ManyToManyField(Doctor) #
    name = models.TextField()
```

- 환자/의사에게 예약된 의사/환자 목록 확인(target 모델의 인스턴스는 _set을 붙인다)
  - patient1.doctors.all()
  - doctor1.patients_set.all()
- M:N 관계에서는 한쪽이 다른쪽에 종속하지 않는다
  - doctor에 patients를 쓰든 patient에 doctors를 쓰든 똑같다
  - 참조-역참조의 관계나 테이블 이름 정도만 달라질 뿐
  - 따라서 추가/삭제는 둘 중 어느쪽에서 하든 상관이 없다



#### Arguments

- `related_name`
  - target_model이 source model을 참조할 때 사용할 manager의 이름을 설정할 수 있다
  - Patient 모델 안에서 `doctors = models.ManyToManyField(Doctor, related_name='patients')`로 설정했다면 `doctor1.patients.all()`과 `patient1.doctors.all()` 모두 사용 가능하다
  - ForeignKey의 related_name과 동일
  - 특히, 한 모델이 여러 개의 M:N 구조를 가진다면 이를 지정해주어야 구분이 가능하다
  
- `through`
  - 중개 테이블을 직접 작성하는 경우, through 옵션을 사용하여 중개 테이블을 나타내는 Django 모델을 지정할 수 있다
  
  - 일반적으로 중개 테이블에 추가 데이터를 사용하는 M:N 관계와 연결하려는 경우에 주로 사용된다
  
    ```python
    class Patient(models.Model):
        doctors = models.ManyToManyField(Doctor, through='Reservation')
        name = models.TextField()
        
    class Reservation(models.Model):
        doctor =
        patient =
        symptom = models.TextField()
        reserved_at = models.DateTimeField(auto_now_add=True)
    ```
  
- `symmetrical`
  - ManyToManyField가 동일한 모델(on self)을 가리키는 정의에서만 사용
  - symmetrical=True일 경우 Django는 person_set 매니저를 추가하지 않음
  - 내가 당신의 친구라면 당신도 내 친구가 됨 => 대칭을 원하지 않을 경우 False로 설정



#### Related Manager

- Related Manager
  - 1:N 또는 M:N 관련 컨텍스트에서 사용하는 매니저
  - 같은 이름의 메서드여도 각 관계에 따라 다르게 사용 및 동작
  - 종류
    - add()
      - 지정된 객체를 관련 객체 집합에 추가
      - 이미 존재하는 관계에 사용하면 관계가 복제되지 않음
      - 모델 인스턴스, 필드값을 인자로 허용
    - remove()
      - 관련 객체 집합에서 지정된 모델 객체를 제거
      - 내부적으로 QuerySet.delete()를 사용하여 관계가 삭제됨
      - 모델 인스턴스, 필드 값(PK)을 인자로 허용
    - create()
    - clear()
    - set()



## Like

> 좋아요 기능 구현

- `related_name='like_articles'`

  - 필드 생성시 자동으로 역참조는 .article.set 매니저를 생성하지만 이전 1:N 관계에서 이미 해당 매니저 이름을 사용하므로 related_name을 추가해준다

  ```python
  # articles/models.py
  
  class Article(models.Model):
      user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
      like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles') #
  ...
  ```

- User - Article 간 사용 가능한 DB API

  - article.user : 게시글 작성한 유저(1:N)
  - article.like_user : 게시글을 좋아요한 유저(M:N)
  - user.article_set : 유저가 작성한 게시글(역참조, 1:N)
  - user.like_articles : 유저가 좋아요한 게시글(역참조, M:N)

- url 작성

  ```python
  # articles/urls.py
  
  path('<int:article_pk>/likes/', views.likes, name='likes'),
  ```

- view 작성

  ```python
  @require_POST
  def likes(request, article_pk):
      if request.user.is_authenticated:
          article = get_object_or_404(Article, pk=article_pk)
  
          # 이 게시글에 좋아요를 누른 유저 목록에 현재 요청하는 유저가 있다면.. 좋아요 취소
          # if request.user in article.like_users.all(): 
          if article.like_users.filter(pk=request.user.pk).exists():
              article.like_users.remove(request.user)
          else:
              article.like_users.add(request.user)
          return redirect('articles:index')
      return redirect('accounts:login')
  ```

  - `exists()` : QuerySet 결과가 포함되어 있으면 True를 반환하고 그렇지 않으면 False를 반환

- index 페이지에 like 출력 부분 작성

  ```django
  <div>
      <form action="{% url 'articles:likes' article.pk %}" method="POST">  
          {% csrf_token %}
          {% if user in article.like_users.all %}
          	<input type="submit" value="좋아요 취소">
          {% else %}
          	<input type="submit" value="좋아요">
          {% endif %}
      </form>
  </div>
  ```



## Profile

> follow 기능을 위한 프로필 페이지 구현

- url 작성

  ```python
  # accounts/urls.py
  
  path('<username>/', views.profile, name='profile'),
  ```

- view 작성

  ```python
  # accounts/views.py
  
  def profile(request, username):
      User = get_user_model()
      person = get_object_or_404(User, username=username)
      context = {
          'person': person,
      }
      return render(request, 'accounts/profile.html', context)
  ```

- template 작성

  ```django
  <!-- accounts/profile.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
  <h1>{{ person.username }}님의 프로필</h1>
  
  <hr>
  
  {% comment %} 이 사람이 작성한 게시글 목록 {% endcomment %}
  <h2>{{ person.username }}이 작성한 게시글</h2>
  {% for article in person.article_set.all %}
    <p>{{ article.title }}</p>
  {% endfor %}
  
  <hr>
  
  {% comment %} 이 사람이 작성한 댓글 목록 {% endcomment %}
  <h2>{{ person.username }}이 작성한 댓글</h2>
  {% for c in person.comment_set.all %}
    <p>{{ c.content }}</p>
  {% endfor %}
  
  <hr>
  
  {% comment %} 이 사람이 좋아요를 누른 게시글 목록 {% endcomment %}
  <h2>{{ person.username }}이 좋아요를 누른 게시글</h2>
  {% for article in person.like_articles.all %}
    <p>{{ article.title }}</p>
  {% endfor %}
  
  <a href="{% url 'articles:index' %}">[back]</a>
  
  {% endblock content %}
  ```

- base.html 작성

  ```django
  <!-- base.html -->
  
  {% if request.user.is_authenticated %}
  	<h3>Hello, {{ user }}</h3>
  	<a href="{% url 'accounts:profile' request.user.username %}">내 프로필</a>
  	...
  ```

- index 페이지에 프로필 링크 작성

  ```django
  <!-- articles/index.html -->
  {% for article in articles %}
  	<p>작성자:  <a href="{% url 'accounts:profile' article.user.username %}">{{ article.user }}</a></p>
  	...
  ```

  

## Follow

- url 작성

  ```python
  # account/urls.py
  
  path('<int:user_pk>/follow/', views.follow, name='follow'),
  ```

- view 작성

  ```python
  # accounts/views.py
  
  @require_POST
  def follow(request, user_pk):
      if request.user.is_authenticated:
          you = get_object_or_404(get_user_model(), pk=user_pk)
          me = request.user
  
          if me != you:
              if you.followers.filter(pk=me.pk).exists():
              # if me in you.followers.all():
                  # 언팔로우
                  you.followers.remove(me)
              else:
                  # 팔로우
                  you.followers.add(me)
          return redirect('accounts:profile', you.username)
      return redirect('accounts:login')
  ```

- profile 페이지에 팔로우와 언팔로우 버튼 생성

  - 팔로우 수 세는 법
    1. person.followers.all|length
    2. person.followers.count
  - dtl - with를 사용하면 이름을 정해두고 사용할 수 있다
    - 최적화와는 관련 X

  ```django
  <!-- accounts/profile.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
  <h1>{{ person.username }}님의 프로필</h1>
  
  {% with followers=person.followers.all followings=person.followings.all %}
    <div>
      팔로워 : {{ followers|length }} / 팔로우 : {{ followings|length }}
    </div>
  
  {##}
    <div>
      {% if user != person %}
        <form action="{% url 'accounts:follow' person.pk %}" method="POST">
          {% csrf_token %}
          {% if user in followers %}
            <input type="submit" value="언팔로우">
          {% else %}
            <input type="submit" value="팔로우">
          {% endif %}
        </form>
      {% endif %}
    </div>
  {##}
  {% endwith %}
  
  
  <hr>
  
  {% comment %} 이 사람이 작성한 게시글 목록 {% endcomment %}
  <h2>{{ person.username }}이 작성한 게시글</h2>
  {% for article in person.article_set.all %}
    <p>{{ article.title }}</p>
  {% endfor %}
  
  <hr>
  
  {% comment %} 이 사람이 작성한 댓글 목록 {% endcomment %}
  <h2>{{ person.username }}이 작성한 댓글</h2>
  {% for c in person.comment_set.all %}
    <p>{{ c.content }}</p>
  {% endfor %}
  
  <hr>
  
  {% comment %} 이 사람이 좋아요를 누른 게시글 목록 {% endcomment %}
  <h2>{{ person.username }}이 좋아요를 누른 게시글</h2>
  {% for article in person.like_articles.all %}
    <p>{{ article.title }}</p>
  {% endfor %}
  
  <a href="{% url 'articles:index' %}">[back]</a>
  
  {% endblock content %}
  ```