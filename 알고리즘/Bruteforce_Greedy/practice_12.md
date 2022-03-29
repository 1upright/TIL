# practice_12

## 1) 원소의 합이 0이 되는 부분집합 출력

> input : -1, 3, -9, 6, 7, -6, 1, 5, 4, -2

```python
def boo(i, n):
    if i == n:
        check = []
        for j in range(N):
            if bit[j]:
                check.append(sub[j])
        if sum(check) == 0 and check:
            print(check)
    else:
        boo(i+1, n)
        bit[i] = 1
        boo(i+1, n)
        bit[i] = 0
    
    return

sub = list(map(int, input().split(', ')))
N = len(sub)
bit = [0]*N
boo(0, N)
```



## 2) 최소합

> 맨 왼쪽 위에서 오른쪽 아래까지 이동할 때, 지나는 칸에 써진 숫자의 합계가 최소가 되는 것

```python
def boo(idx, n, i, j, s):
    global res
    if idx == n*2-2:
        if res > s:
            res = s
    elif s >= res:
        return
    else:
        for di, dj in [(1, 0), (0, 1)]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N:
                boo(idx+1, n, ni, nj, s+arr[ni][nj])
        return
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    res = 1690
    boo(0, N, 0, 0, arr[0][0])
    print(f'#{tc} {res}')
    
# 하평님의 dp
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
 
    dp = [[0] * N for _ in range(N)]
    dp[0][0] = arr[0][0]
    for i in range(0, N):
        for j in range(0, N):
            if i == 0 and 0 <= j-1 < N:
                dp[i][j] = arr[i][j] + dp[i][j-1]
            elif j == 0 and 0 <= i-1 < N:
                dp[i][j] = arr[i][j] + dp[i-1][j]
            elif 0 <= j-1 < N and 0 <= i-1 < N:
                dp[i][j] = arr[i][j] + min(dp[i-1][j], dp[i][j-1])
 
    print(f'#{tc} {dp[N-1][N-1]}')
```



## 3) 전자키트

> N*N표에서 1-A-B-....-C-1의 경로가 가능할 때 각각 저장된 배터리 소비량의 합이 최소가 되는 것

```python
def boo(idx, n, i, s):
    global res
    if idx == n-1:
        s += arr[i][0]
        if res > s:
            res = s
    elif s >= res:
        return
    else:
        for j in range(n):
            if not v[j]:
                v[j] = 1
                boo(idx+1, n, j, s+arr[i][j])
                v[j] = 0
    return
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [0]*N
    v[0] = 1
    res = 10000
    boo(0, N, 0, 0)
    print(f'#{tc} {res}')

# 원래 의도된 느낌?
def boo(i, n):
    global res
    if i == n:
        cnt = 0
        ppp = [0] + p + [0]
        for j in range(n+1):
            cnt += arr[ppp[j]][ppp[j+1]]
        if res > cnt:
            res = cnt
    else:
        for j in range(i, n):
            p[i], p[j] = p[j], p[i]
            boo(i+1, n)
            p[i], p[j] = p[j], p[i]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    p = list(range(1, N))
    res = 10000
    boo(0, N-1)
    print(f'#{tc} {res}')
```



## 4) 컨테이너 운반

> 첫 줄 N, M
>
> 둘째 줄 N개의 컨테이너 각각의 무게
>
> 셋째 줄 M개의 트럭 각각의 적재용량
>
> 한번에 옮길 수 있는 최대 무게?

```python
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    cont = sorted(list(map(int, input().split())), reverse=True)
    truck = sorted(list(map(int, input().split())), reverse=True)
    res = i = 0
 
    for t in truck:
        while i < N and t < cont[i]:
            i += 1
        if i == N:
            break
        res += cont[i]
        i += 1
    print(f'#{tc} {res}')
```



## 5) 화물 도크

> [회의실 배정](https://www.acmicpc.net/problem/1931)과 비슷

```python
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    work = []
    for _ in range(N):
        work.append(list(map(int, input().split())))
    work.sort(key = lambda x: (x[1], x[0]))
 
    e = cnt = 0
    for i, j in work:
        if i >= e:
            e = j
            cnt += 1
    print(f'#{tc} {cnt}')
```



## 6) 베이비진 게임

> 카드를 player 1, 2가 한장씩 받을 때 처음 baby-gin 달성하면 우승, 12장 줬는데 우승자 없으면 무승부
>
> [베이비진이란?](https://github.com/1upright/TIL/blob/master/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98/List/List.md#baby-gin-game)

```python
def bg(l):
    global state
    for j in range(10):
        if l[j] == 3:
            state = 1
            return
        if l[j] and l[j+1] and l[j+2]:
            state = 1
            return
 
T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    p1 = [0]*12
    p2 = [0]*12
    state = 0
    for i in range(12):
        if i%2:
            p2[cards[i]] += 1
            bg(p2)
            if state:
                print(f'#{tc} 2')
                break
        else:
            p1[cards[i]] += 1
            bg(p1)
            if state:
                print(f'#{tc} 1')
                break
    else:
        print(f'#{tc} 0')
```



## 7) [균형점](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15MeBKAOgCFAYD)

```python
T = int(input())
for C in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    xs, ms = arr[:N], arr[N:]
    print(f'#{C}',end=' ')

    for i in range(N-1):
        s, e = xs[i], xs[i+1]
        while e-s > 10**(-12):
            mid = (s+e)/2
            l = r = 0
            for j in range(N):
                F = ms[j]/(mid-xs[j])/(mid-xs[j])
                if xs[j] < mid:
                    l += F
                else:
                    r += F
            if l<r:
                e = mid
            else:
                s = mid
        print(f'{mid:.10f}', end=' ')
    print()
```



## 8) [최대 상금](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15Khn6AN0CFAYD)

```python
def boo(di, i, N):
    global res
    if i == N:
        check = int(''.join(arr))
        if res < check:
            res = check
        return
    else:
        for j in range(di, L):
            for k in range(j+1, L):
                if arr[j] <= arr[k]:
                    arr[j], arr[k] = arr[k], arr[j]
                    boo(j, i+1, N)
                    arr[k], arr[j] = arr[j], arr[k]
 
T = int(input())
for C in range(1, T+1):
    tmp, n = input().split()
    arr, res, N, L = list(tmp), int(tmp), int(n), len(tmp)
    boo(0, 0, N)
    if L == 2 or (arr == sorted(arr, reverse=True) and len(set(arr)) == L):
        if N%2:
            arr[-1], arr[-2] = arr[-2], arr[-1]
        res = int(''.join(arr))
    print(f'#{C} {res}')
```

