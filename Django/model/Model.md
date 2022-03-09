# Model

> 단일한 데이터에 대한 정보를 가지는 데이터베이스의 구조
>
> Django는 model을 통해 데이터에 접속하고 관리할 수 있다

- 데이터베이스 : 체계화된 데이터의 모임
- 쿼리 : 데이터를 조회하기 위한 명령어
- 스키마 : 데이터베이스에서 자료의 구조, 표현방법, 관계 등을 정의한 구조
- 테이블
  - 열 : 필드 or 속성
  - 행 : 레코드 or 튜플



## ORM

> Object-Relational-Mapping

- 객체 지향 프로그래밍 언어를 사용하여 Django와 SQL 등 호환되지 않는 유형의 시스템간에 데이터를 변환하는 프로그래밍 기술
- Django의 경우 내장 Django ORM을 사용
- DB를 객체(object)로 조작하기 위해 ORM을 사용한다



## Models.py

```python
class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

- 각 모델은 django.models.Model 클래스의 서브 클래스로 표현됨
- models 모듈을 통해 어떤 타입의 DB 컬럼을 정의할 것인지 정의
- CharField(max_length=None, **options)
  - 길이의 제한이 있는 문자열을 넣을 때 사용
  - max_length는 필수 인자
- TextField(**options)
  - 글자의 수가 많을 때 사용



## Migrations

> Django가 model에 생긴 변화를 반영하는 방법

1. makemigrations
   - model을 변경한 것에 기반한 새로운 마이그레이션을 만들 때 사용
2. migrate
   - 마이그레이션을 DB에 반영하기 위해 사용
   - 설계도를 실제 DB에 반영하는 과정
3. sqlmigrate
   - 마이그레이션에 대한 SQL 구문을 보기 위해 사용
   - 마이그레이션이 SQL 문으로 어떻게 해석되어서 동작할지 미리 확인 할 수 있음
4. showmigrations
   - 프로젝트 전체의 마이그레이션 상태를 확인하기 위해 사용
   - 마이그레이션 파일들이 migrate 됐는지 안됐는지 여부 확인 가능

```bash
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py showmigrations
$ python manage.py sqlmigrate app_name 0001
```



#### model 수정

- 추가모델 필드 작성 후 makemigrations 진행
- 추가 필드에 대해 default 값을 설정할 것인지 물어보는데 1, enter, enter를 눌러 기본값으로 설정된 상태로 models.py의 수정사항을 반영할 수 있다



#### 요약

1. models.py
2. $ python manage.py makemigrations
3. $ python manage.py migrate



## Databas API

> DB를 조작하기 위한 도구
>
> Django가 기본적으로 ORM을 제공함에 따른 것으로 DB를 편하게 조작할 수 있도록 도움

- 쿼리 만들기 : Article.objects.all()
  - Article : class name
  - objects : Manager(django 모델에 데이터베이스 query 작업이 제공되는 인터페이스)
  - all() : QuerySet(데이터베이스로부터 전달받은 객체 목록) API
- Django shell
  - DB API 구문 테스트를 진행할 수 있는 기능으로 Django-extensions 라이브러리의 기능 중 하나
  - $ pip install ipython django-extensions 후 settings.py의 INSTALLED_APPS에 `'django_extensions',` 집어넣기
  - $ python manage.py shell_plus로 사용

