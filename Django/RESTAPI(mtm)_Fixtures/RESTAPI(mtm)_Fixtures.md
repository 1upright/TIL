# RESTAPI(mtm)_Fixtures

## M:N에서의 REST API

- model 작성

    ```python
    # articles/models.py
    
    class Card(models.Model):
        articles = models.ManyToManyField(Article, related_name='cards')
        name = models.CharField(max_length=100)
    ```
    
- serializer 분리

    ```python
    # articles/serializers/article.py
    
    from rest_framework import serializers
    from .comment import CommentSerializer
    from .card import CardSerializer
    from ..models import Article
    
    class ArticleListSerializer(serializers.ModelSerializer):
    
        class Meta:
            model = Article
            fields = ('id', 'title',)
    
    class ArticleSerializer(serializers.ModelSerializer):
        # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
        comment_set = CommentSerializer(many=True, read_only=True)
        comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
        cards = CardSerializer(many=True, read_only=True)
    
        class Meta:
            model = Article
            fields = '__all__'
    
    ```

    ```python
    # articles/serializers/comment.py
    
    from rest_framework import serializers
    from ..models import Comment
    
    class CommentSerializer(serializers.ModelSerializer):
    
        class Meta:
            model = Comment
            fields = '__all__'
            read_only_fields = ('article',)
    
    ```

    ```python
    # articles/serializers/card.py
    
    from rest_framework import serializers
    from ..models import Card
    
    class CardSerializer(serializers.ModelSerializer):
    
        class Meta:
            model = Card
            fields = '__all__'
    ```

- url

    ```python
    # articles/urls.py
    
    path('cards/', views.card_list),
    path('cards/<int:card_pk>/', views.card_detail),
    ```

- view

    ```python
    # articles/views.py
    
    @api_view(['GET'])
    def card_list(request):
        cards = get_list_or_404(Card)
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data)
    
    @api_view(['GET', 'DELETE', 'PUT'])
    def card_detail(request, card_pk):
        card = get_object_or_404(Card, pk=card_pk)
    
        if request.method == 'GET':
            serializer = CardSerializer(card)
            return Response(serializer.data)
        ...
    ```

    

## REST API 문서화

#### drf-yasg 라이브러리

- 설치
    ```bash
    $ pip install drf-yasg
    ```
    
- 등록

    ```python
    # settings.py
    
    INSTALLED_APPS = [
        'drf_yasg',
    ]
    ```

- url

    ```python
    # articles/urls.py
    
    from drf_yasg.views import get_schema_view #
    from drf_yasg import openapi #
    from django.urls import path
    from . import views
    
    schema_view = get_schema_view( #
       openapi.Info(
            title="싸피 장고 REST API",
            default_version='v1',
            # 여기 아래부터는 선택 인자
            description="Test description",
            terms_of_service="https://www.google.com/policies/terms/",
            contact=openapi.Contact(email="contact@snippets.local"),
            license=openapi.License(name="BSD License"),
       ),
       public=True,
    )
    
    urlpatterns = [
        
    ]
    ```

    

## Fixtures

> 데이터베이스의 serialized된 내용을 포함하는 파일 모음 
>
> 앱을 처음 설정할 때 미리 준비된 데이터로 데이터베이스를 미리 채울 경우에 필요

- fixture 데이터 추출

  ```bash
  $ python manage.py seed articles --number=10
  ```

- loaddata

  ```bash
  $ python manage.py loaddata articles/articles.json articles/comments.json accounts/user.json
  ```



## Queryset

- 쿼리셋은 게으르다
- 쿼리셋을 만드는 작업에는 데이터베이스 작업이 포함되지 않음
- 하루종일 필터를 함께 쌓을 수 있으며, Django는 쿼리셋이 '평가(evaluated)'될 때까지 실제로 쿼리를 실행하지 않음
  - 쿼리셋에 해당하는 DB의 레코드들을 실제로 가져오는 것
  - 평가된 모델은 쿼리셋의 내장 캐시에 저장되며, 덕분에 우리가 쿼리셋을 다시 순회하더라도 똑같은 쿼리를 DB에 다시 전달하지 않음



#### 캐시(cache)

- 데이터나 값을 미리 복사해 놓는 임시 장소
- 캐시에 데이터를 미리 복사해 놓으면 계산이나 접근 시간 없이 더 빠른 속도로 데이터에 접근이 가능
- 시스템의 효율성을 위해 여러 분야에서 두루 사용됨



#### 쿼리셋 평가 시점

- Iteration
  - QuerySet은 반복 가능하며 처음 반복할 때 데이터베이스 쿼리를 실행
- bool()
  - bool() 또는 if문 사용과 같은 bool 컨텍스트에서 QuerySet을 테스트하면 쿼리가 실행
- 이외 Pickling, Caching, Slicing, repr(), len(), list() 등



#### 캐시와 쿼리셋

- 각 쿼리셋에는 데이터베이스 액세스를 최소화하는 '캐시'가 포함되어 있음
  - 새로운 쿼리셋이 만들어지면 캐시는 비어있음
  - 쿼리셋이 처음으로 평가되면 데이터베이스 쿼리가 발생
- 쿼리셋 캐시 꿀팁
  - with 탬플릿 태그 : 이름을 간단하게 하여 복잡한 변수를 캐시
  - iterator() : 객체가 많을 때 쿼리셋의 캐싱 동작으로 인해 많은 양의 메모리가 사용될 때 사용

