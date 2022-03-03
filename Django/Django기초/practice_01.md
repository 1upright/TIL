# practice_01

https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1 

에서 api 따와서 1000회 분량의 로또 번호를 비교하고

![로또](practice_01.assets/%EB%A1%9C%EB%98%90.PNG)

와 같이 출력하기



## 코드

- url.py

```python
from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lotto/', views.lotto),
]
```



- views.py

```python
from django.shortcuts import render
import requests
import random

# Create your views here.
def lotto(request):
    resp = requests.get('https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1').json()
    win_list = [resp.get('drwtNo1'), resp.get('drwtNo2'), resp.get('drwtNo3'), resp.get('drwtNo4'), resp.get('drwtNo5'), resp.get('drwtNo6')]
    bonus_num = resp.get('bnusNo')
    cnt_rank = [0]*6
    for _ in range(1000):
        random_num = random.sample(range(1,46), 6)
        cnt = 0
        for num in random_num:
            if num in win_list:
                cnt += 1
        if cnt == 6:
            cnt_rank[0] += 1
        if cnt == 5:
            if bonus_num in random_num:
                cnt_rank[1] += 1
            else:
                cnt_rank[2] += 1
        if cnt == 4:
            cnt_rank[3] += 1
        if cnt == 3:
            cnt_rank[4] += 1
        else:
            cnt_rank[5] += 1

    context = {
        'win_list': win_list,
        'bonus_num': bonus_num,
        'cnt_rank': cnt_rank,
    }
    return render(request, 'lotto.html', context)
```



- lotto.html

```django
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>로또 당첨 횟수를 알아보자.</h1>
  <hr>
  <h2>이번 회차 당첨 번호 : {{ win_list }} + {{ bonus_num }}</h2>
  <ul>
    {% for num in cnt_rank %}
      {% if forloop.last %}
        <li>꽝 : {{ num }}번</li>
      {% else %}
        <li>{{ forloop.counter }}등 : {{ num }}번</li>
      {% endif %}
    {% endfor %}
  </ul>
</body>
</html>
```

