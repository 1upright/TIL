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
        elif cnt == 5:
            if bonus_num in random_num:
                cnt_rank[1] += 1
            else:
                cnt_rank[2] += 1
        elif cnt == 4:
            cnt_rank[3] += 1
        elif cnt == 3:
            cnt_rank[4] += 1
        else:
            cnt_rank[5] += 1

    context = {
        'win_list': win_list,
        'bonus_num': bonus_num,
        'cnt_rank': cnt_rank,
    }
    return render(request, 'lotto.html', context)