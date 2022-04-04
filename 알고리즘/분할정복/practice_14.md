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

```python
# 교수님 풀이

# def check(si, sj):
#     # [1] 위쪽 방향
#     for i in range(si-1, -1, -1):
#         if v[i][sj]==1:
#             return 0
#
#     # [2] 좌측 대각선 위
#     i, j = si-1, sj-1
#     while i>=0 and j>=0:
#         if v[i][j]==1:
#             return 0
#         i, j = i-1, j-1
#
#     # [3] 우상단
#     i, j = si-1, sj+1
#     while i>=0 and j<N:
#         if v[i][j]==1:
#             return 0
#         i, j = i-1, j+1
#
#     # 3방향 퀸 없음: 성공
#     return 1
#
# def DFS(n):
#     global ans
#     if n==N:
#         ans+=1
#         return
#
#     for j in range(N):
#         if check(n, j):
#             v[n][j]=1
#             DFS(n+1)
#             v[n][j]=0
 
def DFS_1(n):
    global ans
    if n==N:
        ans+=1
        return
 
    for j in range(N):
        if v1[j]==v2[n+j]==v3[n-j]==0:
            v1[j]=v2[n+j]=v3[n-j]=1
            DFS_1(n+1)
            v1[j]=v2[n+j]=v3[n-j]=0
 
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    # v = [[0]*N for _ in range(N)]
    # ans = 0
    # DFS(0)
    ans=0
    v1, v2, v3 = [0]*30, [0]*30, [0]*30
    DFS_1(0)
    print(f'#{test_case} {ans}')
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

```python
# 교수님 풀이

from collections import deque
 
def BFS(si,sj,ei,ej):
    # q = [] # [1] q, v 생성
    q = deque()
    v = [[100000]*N for _ in range(N)]
 
    q.append((si,sj))   # [2] q 초기데이터(들) 삽입, v 표시
    v[si][sj]=arr[si][sj]
 
    while q:
        # ci,cj = q.pop(0)
        ci,cj = q.popleft()
 
        # 네방향/8방향/숫자차이가 일정값이하...
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj]>v[ci][cj]+arr[ni][nj]:
                q.append((ni,nj))
                v[ni][nj] = v[ci][cj] + arr[ni][nj]
 
    return v[ei][ej]
 
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    ans = BFS(0,0,N-1,N-1)
    print(f'#{test_case} {ans}')
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

```python
# 교수님 풀이
T = int(input())
di,dj = (1,-1,0,0),(0,0,-1,1)
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    #[1] 좌표*2
    for i in range(len(arr)):
        arr[i][0]*=2
        arr[i][1]*=2
    ans = 0
    for _ in range(4002): # 끝에서 끝 -2000 ~ 2000
        #[1] 좌표이동
        for i in range(len(arr)):
            arr[i][0]+=dj[arr[i][2]]
            arr[i][1]+=di[arr[i][2]]
 
        #[2] 좌표 중복되면 삭제후보
        ddel, v = set(), set()
        for i in range(len(arr)):
            cj, ci = arr[i][0],arr[i][1]
            if (cj,ci) in v:
                ddel.add((cj,ci))
            v.add((cj,ci))
 
        #[3] 삭제리스트에 있으면 삭제
        for i in range(len(arr)-1, -1, -1):
            if (arr[i][0],arr[i][1]) in ddel:
                ans+=arr[i][3]
                arr.pop(i)
    print(f'#{test_case} {ans}')
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

```python
# 교수님 풀이
def DFS(n, cnt, ssum, lst):
    global sol
    if cnt>C:
        return
    if n==M:
        if sol<ssum:
            sol = ssum
        return
 
    DFS(n+1, cnt+lst[n], ssum+lst[n]**2, lst)   # 포함 시키는 경우
    DFS(n+1, cnt, ssum, lst)    # 포함 시키지 않는 경우
 
T= int(input())
for test_case in range(1,T+1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
 
    # [1] 메모이제이션
    mem = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N-M+1):
            sol = 0
            DFS(0, 0, 0, arr[i][j:j+M])
            mem[i][j]=sol
 
    for i1 in range(N):
        for j1 in range(N-M+1):
            for i2 in range(i1, N):
                sj = 0
                if i1==i2:
                    sj = j1+M
                for j2 in range(sj, N-M+1):
                    ans = max(ans, mem[i1][j1]+mem[i2][j2])
    print(f'#{test_case} {ans}')
```

