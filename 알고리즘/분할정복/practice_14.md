# practice_14



## [N-Queen](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7GKs06AU0DFAXB)

```python
def boo(i, N):
    global cnt
    if i == N:
        cnt += 1
        return
    else:
        for j in range(N):
            v[i] = j
            if far(i):
                boo(i+1, N)
 
def far(x):
    for i in range(x):
        if v[i] == v[x] or abs(i-x) == abs(v[i]-v[x]):
            return 0
    return 1
 
T = int(input())
for tc in range(1, T+1):
    N, cnt = int(input()), 0
    v = [0]*N
    boo(0, N)
    print(f'#{tc} {cnt}')
```



## [보급로](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15QRX6APsCFAYD)

```python
def bfs():
    q = [(0, 0)]
    while q:
        i, j = q.pop(0)
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and dp[ni][nj]>dp[i][j]+arr[ni][nj]:
                dp[ni][nj] = dp[i][j] + arr[ni][nj]
                q.append((ni, nj))
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    dp = [[90000]*N for _ in range(N)]
    dp[0][0] = 0
    bfs()
    print(f'#{tc} {dp[N-1][N-1]}')
```



## [원자 소멸 시뮬레이션](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRFInKex8DFAUo)

```python
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    res = 0
    atoms = []
    for i in range(N):
        x, y, d, k = map(int, input().split())
        atoms.append([x*2+2000, y*2+2000, d, k])
    while atoms:
        dic = {}
        for _ in range(len(atoms)):
            x, y, d, k = atoms.pop(0)
            x += [0, 0, -1, 1][d]
            y += [1, -1, 0, 0][d]
            if 0<=x<4001 and 0<=y<4001:
                atoms.append([x, y, d, k])
                if (x, y) in dic:
                    dic[(x, y)].append([d, k])
                else:
                    dic[(x, y)] = [[d, k]]

        for dic_key in dic:
            if len(dic[dic_key]) >= 2:
                for d, k in dic[dic_key]:
                    atoms.remove([dic_key[0], dic_key[1], d, k])
                    res += k

    print(f'#{tc} {res}')
```



## [벌꿀채취](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V4A46AdIDFAWu&categoryId=AV5V4A46AdIDFAWu&categoryType=CODE&problemTitle=%EB%B2%8C%EA%BF%80&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

```python
import itertools

def boo(cnt):
    global res
    if cnt == 2:
        cost_sum = 0
        for i in range(2):
            cost = 0
            for j in range(1, M+1):
                for c in itertools.combinations(check[i], j):
                    if sum(c) <= C:
                        tmp = 0
                        for num in c:
                            tmp += num**2
                        if cost < tmp:
                            cost = tmp
            cost_sum += cost
        if res < cost_sum:
            res = cost_sum
        return

    for i in range(N):
        for j in range(N-M+1):
            if visited[i][j:j+M] == [0]*M:
                for dj in range(M):
                    nj = j+dj
                    visited[i][nj] = 1
                    check[cnt].append(arr[i][nj])
                boo(cnt+1)
                for dj in range(M):
                    nj = j+dj
                    visited[i][nj] = 0
                    check[cnt].pop()

T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    check = [[],[]]
    res = 0
    boo(0)
    print(f'#{tc} {res}')
```
