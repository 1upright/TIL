# practice_04



## 1) 당근 수확

> field 중에서 pos 영역까지 수확할 때 왼쪽 오른쪽 차이가 가장 적고 그때의 차이는 min_val 

```python
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    field = list(map(int, input().split()))
    check = []
 
    for i in range(1, N):
        cnt = 0
        for j in range(i):
            cnt += field[j]
        for j in range(i, N):
            cnt -= field[j]
        check.append(abs(cnt))
     
    min_val = check[0]
    for i in range(N-1):
        if min_val > check[i]:
            min_val = check[i]
            pos = i+1
             
    print(f'#{tc} {pos} {min_val}')
```



## 2) 당근밭 옆 고구마밭

>점점 길어지면 하나의 줄기일 때, {긴 줄기의 개수}와 {가장 긴 줄기에 달린 고구마 총합}

```python
def dc_check(li): # 얌생이 같은 짓이긴 함
    for i in range(len(li)-1):
        if li[i] < li[i+1]:
            return False
    return True
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    field = list(map(int, input().split()))
    cnt_list = [0]*(N-1)
    cnt = 0
    for i in range(len(field)-1):
        if field[i] < field[i+1]:
            cnt += 1
        else:
            cnt = 0
        cnt_list[i] = cnt
 
    max_cnt = cnt_list[0]
    max_idx = []
    stem = 0
    for i in range(N-1):
        if cnt_list[i] == 1:
            stem += 1
        if cnt_list[i] > max_cnt:
            max_cnt = cnt_list[i]
 
    for i in range(N-1):
        if cnt_list[i] == max_cnt:
            max_idx.append(i)
 
    sweet_p_list = []
    for idx in max_idx:
        sweet_p = 0
        for i in range(idx - max_cnt + 1, idx + 2):
            sweet_p += field[i]
        sweet_p_list.append(sweet_p)
 
    max_sp = sweet_p_list[0]
    for i in range(len(sweet_p_list)):
        if sweet_p_list[i] > max_sp:
            max_sp = sweet_p_list[i]
 
    if dc_check(field):
        max_sp = 0
 
    print(f'#{tc} {stem} {max_sp}')
```



## 3) 우주선 착륙

> 팔방 중에서 사방 이상이 더 낮은 숫자를 갖는 중심의 개수는?

```python
di = [-1, -1, -1, 0, 1, 1, 1, 0]
dj = [-1, 0, 1, 1, 1, 0, -1, -1]
 
T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    # arr = [[-1]*(M+2)] + [[-1] + list(map(int, input().split())) +[-1] for _ in range(N)] + [[-1]*(M+2)]
    arr = [list(map(int, input().split())) for _ in range(N)]
 
    res = 0
    for i in range(N):
        for j in range(M):
            cnt = 0
            for k in range(8):
                if 0 <= i+di[k] < N and 0 <= j+dj[k] < M and arr[i+di[k]][j+dj[k]] < arr[i][j]:
                    cnt += 1
            if cnt >= 4:
                res += 1
    print(f'#{tc} {res}')
```



## 4) 파리퇴치 2

> 파리채가 X자 모양으로 친다

```python
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
 
    res = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            kill = 0
            for k in range(M):
                kill += arr[i+k][j+k]
                kill += arr[i+M-1-k][j+k]
            if M%2:
                kill -= arr[i+M//2][j+M//2]
            if kill > res:
                res = kill
    print(f'#{tc} {res}')
```



## 5) 토글

>1) 토글된다 = 1은 0으로, 0은 1로 바뀜
>2) NxN 영역
>3) i행과 j열의 영역(1<=i,j<=N)
>4) 1초부터 M초까지 k초가 되는 순간 i+j가 k의 배수가 되면 토글됨
>5) M이 k의 배수인 경우 전체가 토글됨

```python
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
     
    for k in range(1, M+1):
        for i in range(N):
            for j in range(N):
                if not (i+j+2)%k or not M%k:
                    arr[i][j] = (arr[i][j]-1)*(-1)
                     
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                cnt += 1
    print(f'#{tc} {cnt}')
```



## 6) 기지국

>A, B, C는 기지국이며 각각은 각 위치에서 동서남북으로 각 1개, 2개, 3개의 셀을 커버
>
>집이 위치한 곳은 H
>
>빈칸은 X
>
>기지국이 커버하지 못하는 집의 수는?

```python
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
eff = {1:'A', 2:'B', 3:'C'}
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
 
    for num in range(1, 4):
        for i in range(N):
            for j in range(N):
                if arr[i][j] == eff[num]:
                    for k in range(1, num+1):
                        for l in range(4):
                            if 0<=i+di[l]*k<N and 0<=j+dj[l]*k<N:
                                if arr[i+di[l]*k][j+dj[l]*k] == 'H':
                                    arr[i+di[l]*k][j+dj[l]*k] = 'X'
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'H':
                cnt += 1
    print(f'#{tc} {cnt}')
```

