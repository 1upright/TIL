# api



## [TMDB API](developers.themoviedb.org/3) 이용하기

```python
import requests

### 사이트에서 get popular, search movie, get credit 등을 들어가면 해당 api를 위한 정보들이 나옴

response = requests.get(https://api.themoviedb.org/3/movie/popular, params=params).json()
# 와 같이 할당하면 원하는 정보를 가져올 수 있다.
# 이 사이트의 경우 해당 정보는 '딕셔너리로 이루어진 리스트' 구조

# 다른 정보가 필요한 경우
response2 = requests.get(https://api.themoviedb.org/3/movie/{movie_id}/recommendations, params=params).json()
# 와 같이 할당하는 경우가 있음

# 따라서
BASE_URL = https://api.themoviedb.org/3
path = '/search/movie'
path = '/movie/{movie_id}/movie'
# 와 같이 하면

response = requests.get(BASE_URL+path, params=params).json()
# 이런 식으로 이용 가능
### 사이트에서 BASE_URL과 path는 주어짐

#response2의 경우
response2 = requests.get(BASE_URL+'/movie/{}/recommendations'.format(movie_id), params=params2).json()

# params는
params = {
    'api_key': '1407940e8727569682a684bd25dedb04',
    'region': 'KR',
    'language': 'ko',
    'query' : title               
}

### 이런식으로 쓰이며 필수적으로 넣어야하는 것들은 사이트에서 제공됨

## 사이트의 api를 확인하여 형식과 넣어야하는 값들을 확인하면 다른 api도 사용할 수 있을 것.
```