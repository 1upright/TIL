# practice_15

## 1) 그룹나누기

> 연결된 애들 전부다 같은 팀이면 총 팀은 몇 개?

```python
from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    tree = [[] for _ in range(N+1)]
    visited = [0]*(N+1)
    data = list(map(int, input().split()))
    cnt = 0

    for i in range(M):
        tree[data[i*2]].append(data[i*2+1])
        tree[data[i*2+1]].append(data[i*2])

    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = 1
            q = deque([i])
            cnt += 1
            while q:
                v = q.popleft()
                for x in tree[v]:
                    if not visited[x]:
                        q.append(x)
                        visited[x] = 1

    print(f'#{tc} {cnt}')
    
# 의도된 풀이
def find_set(n):
    while rep[n] != n:
        n = rep[n]
    return n
 
def union(a, b):
    rep[find_set(b)] = find_set(a)
 
T = int(input())
 
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    rep = [i for i in range(N+1)]
    for i in range(M):
        a, b = lst[2*i], lst[2*i + 1]
        union(a, b)

    res = set()
    for j in range(1, len(rep)):
        res.add(find_set(j))
 
    print(f'#{tc} {len(res)}')
```



## 2) 최소 신장 트리

> 최소신장트리를 구성하는 간선의 가중치를 모두 더해라

```python
def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edge = []

    for _ in range(E):
        u, v, w = map(int, input().split())
        edge.append([w, v, u])
    edge.sort()
    rep = list(range(V+1))
    cnt = total = 0

    for w, v, u in edge:
        if find_set(v) != find_set(u):
            cnt += 1
            rep[find_set(v)] = find_set(u)
            total += w
            if cnt == V:
                break
    
    print(f'#{tc} {total}')
```



## 3) 최소 비용

> 2차원 배열에서 한칸 갈 때마다 연료가 1씩 들고 더 높은 곳으로 가면 높이차만큼 연료가 추가로 들음. 최소 연료 소비량은?

```python
from collections import deque
 
def bfs():
    q = deque([(0, 0)])
    while q:
        i, j = q.popleft()
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = i + di, j + dj
            if 0<=ni<N and 0<=nj<N:
                tmp = 0
                if arr[i][j] < arr[ni][nj]:
                    tmp = arr[ni][nj] - arr[i][j]
                if dp[ni][nj] > dp[i][j]+tmp+1:
                    dp[ni][nj] = dp[i][j]+tmp+1
                    q.append((ni, nj))
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dp = [[99999] * N for _ in range(N)]
    dp[0][0] = 0
    bfs()
    print(f'#{tc} {dp[N-1][N-1]}')
```



## 4) 최소 이동 거리

> 줄마다 구간 시작 지점 s, 구간 끝 지점 e, 구간 거리 w가 주어진다. 0번 지점에서 N번 지점까지 이동하는데 걸리는 최소한의 거리는?

```python
def dijkstra(s, N):
    U = [0]*(N+1)
    U[s] = 1
    for i in range(N+1):
        D[i] = adj[s][i]
 
    for _ in range(N):
        minV = INF
        w = 0
        for i in range(N+1):
            if not U[i] and minV > D[i]:
                minV = D[i]
                w = i
        U[w] = 1
        for v in range(N+1):
            if 0<adj[w][v]<INF:
                D[v] = min(D[v], D[w]+adj[w][v])
 
T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    INF = 10000
    adj = [[INF]*(N+1) for _ in range(N+1)]
    for i in range(N+1):
        adj[i][i] = 0
    for _ in range(E):
        u, v, w = map(int, input().split())
        adj[u][v] = w
 
    D = [0]*(N+1)
    dijkstra(0, N)
    print(f'#{tc} {D[N]}')
```



## 5) [하나로](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15StKqAQkCFAYD)

```python
def find_set(x):
    while x != p[x]:
        x = p[x]
    return x

def union(x, y):
    p[find_set(y)] = find_set(x)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    pos = []
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    E = float(input())
    for i in range(N):
        pos.append((x_list[i], y_list[i]))

    edge = []
    for i in range(N-1):
        for j in range(i+1, N):
            x1, y1 = pos[i]
            x2, y2 = pos[j]
            w = ((x1-x2)**2+(y1-y2)**2)*E
            edge.append((w, i, j))
    edge.sort()

    cnt = total = 0
    p = list(range(N))
    for w, u, v in edge:
        if find_set(u) != find_set(v):
            cnt += 1
            union(u, v)
            total += w
            if cnt == N-1:
                break
    print(f'#{tc} {total:.0f}')
```



## 6) [작업순서](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV18TrIqIwUCFAZN)

```python
for tc in range(1, 11):
    V, E = map(int, input().split())
    data = list(map(int, input().split()))
    arr = [[]*(V+1) for _ in range(V+1)]
    visited = [0]*(V+1)
    print(f'#{tc}',end=' ')
 
    for i in range(E):
        arr[data[i*2+1]].append(data[i*2])
 
    for i in range(1, V+1):
        if not arr[i] and not visited[i]:
            q = [i]
            visited[i] = 1
             
            while q:
                v = q.pop(0)
                print(v, end=' ')
                for j in range(1, V+1):
                    if v in arr[j]:
                        arr[j].remove(v)
                for j in range(1, V+1):
                    if not arr[j] and not visited[j]:
                        q.append(j)
                        visited[j] = 1
                        break
    print()
```



## 7) [인수의 생일 파티](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV4xuqCqBeUDFAUx)

```python
# 시간 초과 - 플로이드 워셜
T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())
    INF = 1000000
    arr = [[INF]*N for _ in range(N)]
    for i in range(N):
        arr[i][i] = 0
    for _ in range(M):
        x, y, c = map(int, input().split())
        arr[x-1][y-1] = c
 
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if arr[i][j] > arr[i][k] + arr[k][j] and j != k:
                    arr[i][j] = arr[i][k] + arr[k][j]
 
    res = 0
    for i in range(N):
        if i != X-1:
            tmp = arr[i][X-1]+arr[X-1][i]
            if res < tmp:
                res = tmp
 
    print(f'#{tc} {res}')

# 정답 - dijkstra 
def dijkstra(s, N, arr):
    U = [0]*(N+1)
    U[s] = 1
    D = [0]*(N+1)
    for i in range(N+1):
        D[i] = arr[s][i]

    for _ in range(N+1):
        minV = INF
        w = 0
        for i in range(N+1):
            if not U[i] and minV > D[i]:
                minV = D[i]
                w = i
        U[w] = 1
        for v in range(N+1):
            if 0<arr[w][v]<INF:
                D[v] = min(D[v], D[w]+arr[w][v])

    return D

T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())
    INF = 99999999
    arr1 = [[INF]*N for _ in range(N)]
    arr2 = [[INF]*N for _ in range(N)]

    for i in range(N):
        arr1[i][i] = 0
        arr2[i][i] = 0

    for _ in range(M):
        x, y, c = map(int, input().split())
        arr1[x-1][y-1] = c
        arr2[y-1][x-1] = c

    D1 = dijkstra(X-1, N-1, arr1)
    D2 = dijkstra(X-1, N-1, arr2)

    res = 0
    for i in range(N):
        tmp = D1[i]+D2[i]
        if res < tmp:
            res = tmp

    print(f'#{tc} {res}')
```

