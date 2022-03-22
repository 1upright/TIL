# practice_10

## 1) [재미있는 오셀로 게임](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWQmA4uK8ygDFAXj)

```python
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0]*N for _ in range(N)]
    arr[N//2-1][N//2] = arr[N//2][N//2-1] = 1
    arr[N//2][N//2] = arr[N//2-1][N//2-1] = 2
 
    for _ in range(M):
        x, y, c = map(int, input().split())
        i, j = y-1, x-1
        arr[i][j] = c
        for di, dj in [[0, -1], [1, 0], [0, 1], [-1, 0], [1, 1], [1, -1], [-1, -1], [-1, 1]]:
            for k in range(1, N):
                ni, nj = i+di*k, j+dj*k
                if 0<=ni<N and 0<=nj<N
                	if arr[ni][nj] == 0:
                    	break
                    if arr[ni][nj] == c:
                        for a in range(k):
                            arr[i+di*a][j+dj*a] = c
                        break
 
    cntB = 0
    cntW = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                cntB += 1
            if arr[i][j] == 2:
                cntW += 1
    print(f'#{tc} {cntB} {cntW}')
```



## 2) [정식이의 은행업무](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWMeRLz6kC0DFAXd&categoryId=AWMeRLz6kC0DFAXd&categoryType=CODE&problemTitle=%EC%A0%95%EC%8B%9D%EC%9D%B4&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

```python
def check(x, y):
    for i in range(len(x)):
        copy_x = x[:]
        copy_x[i] = str((int(copy_x[i])+1)%2)
        a = ''.join(copy_x)
        for j in range(len(y)):
            copy_y = y[:]
            copy_y[j] = str((int(copy_y[j])+1)%3)
            b = ''.join(copy_y)
            if int(a, 2) == int(b, 3):
                return int(a, 2)
            copy_y[j] = str((int(copy_y[j])+1)%3)
            b = ''.join(copy_y)
            if int(a, 2) == int(b, 3):
                return int(a, 2)
 
T = int(input())
for tc in range(1, T+1):
    x, y = list(input()), list(input())
    print(f'#{tc} {check(x, y)}')
```



## 3) [격자판의 숫자 이어 붙이기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7I5fgqEogDFAXB&categoryId=AV7I5fgqEogDFAXB&categoryType=CODE&problemTitle=%EA%B2%A9%EC%9E%90%ED%8C%90&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

```python
def boo(p, i, j):
    global word
    if p == 7:
        res.append(word)
 
    else:
        for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            ni, nj = i+di, j+dj
            if 0<=ni<4 and 0<=nj<4:
                word += str(arr[ni][nj])
                boo(p+1, ni, nj)
                word = word[:-1]
 
T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    res = []
    word = ''
    for i in range(4):
        for j in range(4):
            boo(0, i, j)
    print(f'#{tc} {len(set(res))}')
```



## 4) [미생물 격리](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV597vbqAH0DFAVl&categoryId=AV597vbqAH0DFAVl&categoryType=CODE&problemTitle=%EB%AF%B8%EC%83%9D%EB%AC%BC&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

```python
di = [0, -1, 1, 0, 0] # 0, 상, 하, 좌, 우
dj = [0, 0, 0, -1, 1]
T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(K)]
 
    for _ in range(M):
        v = [[0] * N for _ in range(N)]
        for i in range(len(arr)):
            a, b, c, d = arr[i][0], arr[i][1], arr[i][2], arr[i][3]
            if not c:
                continue
            a += di[d]
            b += dj[d]
            if a == N-1 or b == N-1 or not a*b:
                d = ((d+1)//2)*2 - (d%2+1)%2
                c //= 2
 
            else:
                if v[a][b]:
                    if v[a][b][0] > c:
                        arr[v[a][b][2]][2] += c
                        c = 0
                    else:
                        copy_val = arr[v[a][b][2]][2]
                        arr[v[a][b][2]][2] = 0
                        v[a][b] = [c, d, i]
                        c += copy_val
                else:
                    v[a][b] = [c, d, i] # 최대값, 최대방향, 최대인덱스
            arr[i] = [a, b, c, d]
 
    cnt = 0
    for x in arr:
        cnt += x[2]
    print(f'#{tc} {cnt}')
```



## 5) [홈 방범 서비스](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V61LqAf8DFAWu&categoryId=AV5V61LqAf8DFAWu&categoryType=CODE&problemTitle=%EB%B0%A9%EB%B2%94&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

```python
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    homes = []
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                homes.append([i, j])
    res = 0
    for k in range(1, N+2):
        cost = k*k+(k-1)*(k-1)
        for si in range(N):
            for sj in range(N):
                cnt = 0
                for i, j in homes:
                    if abs(i-si)+abs(j-sj) < k:
                        cnt += 1
                if cnt*M-cost >= 0:
                    if res < cnt:
                        res = cnt
    print(f'#{tc} {res}')
```



## 6) [디저트 카페](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5VwAr6APYDFAWu&categoryId=AV5VwAr6APYDFAWu&categoryType=CODE&problemTitle=%EB%94%94%EC%A0%80%ED%8A%B8&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

```python
di = [1, 1, -1, -1] # 우하, 좌하, 좌상, 우상
dj = [1, -1, -1, 1]
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    move = []
    for a in range(1, N-1):
        for b in range(1, N-a):
            move.append([0]*a+[1]*b+[2]*a+[3]*b)
 
    res = -1
    for i in range(N-1):
        for j in range(N-1):
            for ls in move:
                v = [0] * 101
                v[arr[i][j]] = 1
                ni, nj = i, j
                cnt = 1
 
                for x in ls:
                    if 0<=ni+di[x]<N and 0<=nj+dj[x]<N and not v[arr[ni+di[x]][nj+dj[x]]]:
                        ni += di[x]
                        nj += dj[x]
                        v[arr[ni][nj]] = 1
                        cnt += 1
                    else:
                        break
 
                if cnt == len(ls):
                    if res < cnt:
                        res = cnt
 
    print(f'#{tc} {res}')
```



## 7) [수영장](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpFQaAQMDFAUq&categoryId=AV5PpFQaAQMDFAUq&categoryType=CODE&problemTitle=%EC%88%98%EC%98%81%EC%9E%A5&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

```python
T = int(input())
for tc in range(1, T+1):
    a, b, c, d = map(int, input().split())
    plan = list(map(int, input().split()))
    costs = [0]*13
    for i in range(1,13):
        costs[i] = a * plan[i-1] + costs[i-1]
        if costs[i] > b + costs[i-1]:
            costs[i] = b + costs[i-1]
        if i > 2 and costs[i] > c + costs[i-3]:
            costs[i] = c + costs[i-3]
    ans = costs[12]
    if ans > d:
        ans = d
    print(f'#{tc} {ans}')
```

