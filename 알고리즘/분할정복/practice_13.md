# practice_13

## 1) 전기버스 2

> data[0] = 정거장 수
>
> data[1:] = 정거장마다 충전지 용량
>
> 목적지에 도착할 때 최소 경유횟수는?

```python
T = int(input())
for tc in range(1, T+1):
    data = list(map(int, input().split()))
    N = data[0]
    dp = [100]*(N+1)
    dp[1] = 0
    for i in range(1, N):
        for j in range(i+1, i+data[i]+1):
            if j<=N:
                dp[j] = min(dp[j], dp[i]+1)
    print(f'#{tc} {dp[N]-1}')
```



## 2) 최소생산비용

> NxN 배열에서 정수하나씩 더해서 최소값 구하기

```python
def boo(i, n, s):
    global res
    if i == n:
        if res > s:
            res = s
    elif res < s:
        return
    else:
        for j in range(n):
            if not v[j]:
                v[j] = 1
                boo(i+1, n, s+arr[i][j])
                v[j] = 0
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v, res = [0]*N, N*100
    boo(0, N, 0)
    print(f'#{tc} {res}')
```



## 3) [동철이의 일 분배](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LuHfqDz8DFAXc)

```python
def boo(i, n, r):
    global res
    if i == n:
        if res < r:
            res = r

    elif res >= r:
        return

    else:
        for j in range(n):
            if not v[j]:
                v[j] = 1
                boo(i+1, n, arr[i][j]/100*r)
                v[j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v, res = [0]*N, 0
    boo(0, N, 100)
    print(f'#{tc} {res:.6f}')
```

