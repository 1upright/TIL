# Static_files

> 응답할 때 별도의 처리 없이 파일 내용을 그대로 보여주면 되는 파일

- 특정 위치(URL)에 있는 자원을 요청(HTTP request)받아 제공하는 응답(HTTP response)을 처리하는 것을 기본 동작으로 함
- 자원(ex. 사진파일)과 접근 가능한 주소(ex. 웹 주소)가 정적으로 연결
- 파일 자체가 고정되어 있고, 서비스 중에도 추가되거나 변경되지 않고 고정되어 있음



## 구성

1. `django.contrib.staticfiles`가 INSTALLED_APPS에 포함되어 있는지 확인
2. settings.py에서 STATIC_URL 정의
3. 템플릿에서 static 템플릿 태그를 사용하여 지정된 상대경로에 대한 URL 빌드

```django
{% load static %}
<img src="{% static 'sample.jpg' %}" alt="My image">
```

4. 앱의 static 디렉토리에 정적 파일 저장



- `STATICFILES_DIRS` :  정적 파일 경로 목록 정의하는 리스트
  -  `BASE_DIR / 'static',` 같은거 추가
- `STATIC_URL` : `STATIC_ROOT`에 있는 정적 파일 참조할 때 사용할 URL
  - 실제 파일이나 디렉토리가 아님
  - 비어 있지 않은 값으로 설정한다면 `/`로 끝나야 함
- `STATIC_ROOT` : collectstatic이 배포를 위해 정적 파일을 수집하는 디렉토리의 절대 경로
  - django 프로젝트에서 사용하는 모든 정적 파일을 한곳에 모아넣음
  - settings.py의 DEBUG 값이 True로 되어 있으면 작성되지 않음
    - DEBUG 값이 True이면 개발단계
    - DEBUG 값이 False이면 배포단계 => 오류나도 디버깅 화면 등이 안뜸



## Django template tag

#### log
  - 사용자 정의 템플릿 태그 세트를 로드
  - 로드하는 라이브러리, 패키지에 등록된 모든 태그와 필터를 불러옴
#### static
  - STATIC_ROOT에 저장된 정적 파일에 연결



## 경로

#### 기본 경로

- 정적 파일 경로 - app/static/app
- template에서 경로 참조

```django
{% extend 'base.html' %}
{% load static %} {# 여기 #}

{% block content %}
	<img scr="{% static 'articles/sample.jpg' %}" alt="sample"> {# 여기 #}
	....
{% endblock content%}
```



#### 추가 경로

- 정적 파일 위치 및 추가 경로 작성

```python
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
```

- template에서 경로 참조

```django
<!-- base.html -->

{% load static %} {# 여기 #}
   
...
<body>
    <img scr="{% static 'articles/sample2.jpg' %}" alt="sample2"> {# 여기 #}
</body>
...
```
