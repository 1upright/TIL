# practice_07

## 1. [토마토()](https://www.acmicpc.net/problem/7576)

```python
def bfs(N, M):  # N 행, M 열
    visited = [[0]*M for _ in range(N)]# visited 생성
    q = [0]*(N*M) # 큐생성
    front = -1
    rear = -1
    cnt = 0 # 안익은 토마토 개수
    for i in range (N): # 시작점 인큐 (익은 토마토 위치)
        for j in range(M):
            if tomato[i][j]==1:
                rear += 1   #q.append((i, j))
                q[rear] = (i, j)
                visited[i][j] = 1          # 시작점 인큐표시
            elif tomato[i][j] == 0:
                cnt += 1
    if cnt ==0 and len(q)>0:
        return 0        # 익은 토마토만 주어진 경우
    while front != rear:    # 큐가 비어있지 않으면
        #i, j = q.pop(0)     # 익은 토마토
        front += 1
        i, j = q[front]
        # visit(i,j)
        for di, dj in [[0,1], [1,0],[0,-1],[-1,0]]:
            ni, nj = i+di, j+dj     # 익은 토마토의 인접칸
            if 0<=ni<N and 0<=nj<M and tomato[ni][nj]==0 and visited[ni][nj]==0: # 인접칸에 안익은 토마토가 들어있으면
                rear += 1  # q.append((i, j))
                q[rear] = (ni, nj)
                visited[ni][nj] = visited[i][j] + 1
    # 익지않은 토마토가 있으면 -1 리턴
    # 모두 익은 경우 visited 최대값 리턴
    # 원래 모두 익은 경우 0 리턴!
    maxV = 0
    for i in range(N):
        for j in range(M):
            if tomato[i][j]==0:
                if visited[i][j]==0:    # 안익은 경우
                    return -1
                elif maxV < visited[i][j]:  # 익은 경우 날짜 비교
                    maxV = visited[i][j]
    return maxV -1

M, N = map(int, input().split())
tomato = [list(map(int,input().split())) for _ in range(N)]
print(bfs(N, M))
```



## 2. [단지번호붙이기](https://www.acmicpc.net/problem/2667)

```python
# BFS
def bfs(i, j, N):
    # visited 생성 (이미 생성)
    q = []  # 큐 생성
    q.append((i,j)) # 시작점 인큐
    v[i][j] = 1   # 단지에 포함
    h = 0           # 단지에 속한 집의 수
    while q:
        i, j = q.pop(0) # 디큐
        h += 1  # visit()
        for di, dj in [[0,1], [1,0],[0,-1],[-1,0]]:
            ni, nj = i+di, j+dj
            if 0<=ni< N and 0<=nj< N and arr[ni][nj]==1 and v[ni][nj] ==0:
                q.append((ni,nj))
                v[ni][nj] = 1   # 단지에 속한 집으로 인큐됨
    return h

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
#arr = [input() for _ in range(N)]
cnt = 0     # 단지 수
num = []    # 단지에 속한 집의 수
v = [[0]*N for _ in range(N)]   # 단지에 속했는지 표시
for i in range(N):
    for j in range(N):
        if arr[i][j]==1 and v[i][j] == 0:   # 아직 단지에 속하지 않은 집을 만나면
            cnt += 1    # 새로운 단지, 단지 수 증가
            r = bfs(i, j, N)    # 단지에 속한 집의 수
            num.append(r)
num.sort()  # 오름차순 정렬
print(cnt)  # 단지 수 출력
for x in num:   # 단지에 속한 집의 수 출력
    print(x)
    
# DFS1
def dfs1(i, j, N):
    global hcnt
    v[i][j] = 1 # 방문 정점 표시
    hcnt += 1   # 방문 정점 카운트
    for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 1 and v[ni][nj] == 0: # 인접 건물로 이동
            dfs1(ni, nj, N)

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
#arr = [input() for _ in range(N)]
cnt = 0     # 단지 수
num = []    # 단지에 속한 집의 수
v = [[0]*N for _ in range(N)]   # 단지에 속했는지 표시
for i in range(N):
    for j in range(N):
        if arr[i][j]==1 and v[i][j] == 0:   # 아직 단지에 속하지 않은 집을 만나면
            cnt += 1    # 새로운 단지, 단지 수 증가
            hcnt = 0
            dfs1(i, j, N)    # 단지에 속한 집의 수
            num.append(hcnt)
num.sort()  # 오름차순 정렬
print(cnt)  # 단지 수 출력
for x in num:   # 단지에 속한 집의 수 출력
    print(x)
    
# DFS2
def dfs2(i, j, N):
    v[i][j] = 1 # 방문 정점 표시
    hcnt = 1   # 방문 정점 카운트
    for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 1 and v[ni][nj] == 0: # 인접 건물로 이동
            hcnt += dfs2(ni, nj, N)
    return hcnt

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
#arr = [input() for _ in range(N)]
cnt = 0     # 단지 수
num = []    # 단지에 속한 집의 수
v = [[0]*N for _ in range(N)]   # 단지에 속했는지 표시
for i in range(N):
    for j in range(N):
        if arr[i][j]==1 and v[i][j] == 0:   # 아직 단지에 속하지 않은 집을 만나면
            cnt += 1    # 새로운 단지, 단지 수 증가
            hcnt = dfs2(i, j, N)    # 단지에 속한 집의 수
            num.append(hcnt)
num.sort()  # 오름차순 정렬
print(cnt)  # 단지 수 출력
for x in num:   # 단지에 속한 집의 수 출력
    print(x)
```



## 3. [미로](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14vXUqAGMCFAYD)

```python
def bfs(i, j, N):
    q = []
    q.append((i, j))
    v[i][j] = 1
    while q:
        i, j = q.pop(0)
        if maze[i][j] == 3:
            return 1
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            ni, nj = i+di, j+dj
            if maze[ni][nj] != 1 and v[ni][nj] == 0:
                q.append((ni, nj))
                v[ni][nj] = 1
    return 0
 
for _ in range(10):
    T = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    v = [[0]*16 for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                print(f'#{T} {bfs(i, j, 16)}')
                break
```



## 4. 미로의 거리

> NxN 배열에서 출발지(2)에서 도착지(3)까지의 거리

```python
def bfs(i, j, N):
    q = []
    q.append((i, j))
    v[i][j] = 1
    while q:
        i, j = q.pop(0)
        for di, dj in [[0,1],[0,-1],[1,0],[-1,0]]:
            ni, nj = i+di, j+dj
            if maze[i][j] == 3:
                return v[i][j]-2
            if 0<=ni<N and 0<=nj<N and maze[ni][nj]!=1 and v[ni][nj]==0:
                q.append((ni,nj))
                v[ni][nj] = v[i][j]+1
    return 0
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    v = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                print(f'#{tc} {bfs(i, j, N)}')
```



## 5. 피자 굽기

> M개의 피자 중 N개까지 화덕에 넣을 수 있고 Ci만큼의 치즈가 피자에 각각 뿌려져있다.
>
> 화덕에 넣었다가 빼면 치즈의 양은 C //= 2가 된다
>
> 치즈가 다 녹으면 다음 피자를 순서대로 넣는다
>
> 가장 마지막까지 남아있는 피자 번호는?

```python
T = int(input())
for tc in range(1, T+1):
    N,M = map(int,input().split())
    Cis = list(map(int,input().split()))
    data = []
    for i in range(M):
        data.append([i, Cis[i]])
    Q = []
    for i in range(N):
        Q.append(data.pop(0))
 
    while len(Q) > 1:
        check = Q.pop(0)
        check[1] //= 2
        if check[1]:
            Q.append(check)
        else:
            if data:
                Q.append(data.pop(0))
    print(f'#{tc} {Q[0][0]+1}')
```

