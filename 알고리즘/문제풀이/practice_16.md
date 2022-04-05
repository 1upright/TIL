# practice_16

## 1) [창용 마을 무리의 개수](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWngfZVa9XwDFAQU)

```python
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    tree = [[] for _ in range(N+1)]
    visited = [0]*(N+1)
    cnt = 0
 
    for _ in range(M):
        x, y = map(int, input().split())
        tree[x].append(y)
        tree[y].append(x)
 
    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = 1
            cnt += 1
            q = [i]
            while q:
                v = q.pop(0)
                for x in tree[v]:
                    if not visited[x]:
                        visited[x] = 1
                        q.append(x)
 
    print(f'#{tc} {cnt}')
```



## 2) [벽돌 깨기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRQm6qfL0DFAUo)

```python
from collections import deque
 
def boo(i, N):
    global res
    if i == N:
        cols = [[] for _ in range(W)]
        for j in range(W):
            for i in range(H):
                if arr[i][j]:
                    cols[j].append(arr[i][j])
        cnt = 0
        for x in bit:
            if cols[x]:
                top = len(cols[x])
                target = cols[x][0]
                q = deque([(x, target, top)])
 
                while q:
                    idx, num, jdx = q.popleft()
                    if idx-num+1 >= 0:
                        left = idx-num+1
                    else:
                        left = 0
                    if idx+num <= W:
                        right = idx+num
                    else:
                        right = W
                    for j in range(left, right):
                        tmp = len(cols[j])
                        k = tmp - jdx
                        if k >= 0 and cols[j][k]:
                            q.append((j, cols[j][k], jdx))
                            cols[j][k] = 0
 
                    tmp = len(cols[idx])
                    if jdx+num-1 <= tmp:
                        up = tmp-jdx-num+1
                    else:
                        up = 0
                    if jdx-num >= 0:
                        down = tmp-jdx+num
                    else:
                        down = tmp
                    for j in range(up, down):
                        if cols[idx][j]:
                            q.append((idx, cols[idx][j], tmp-j))
                            cols[idx][j] = 0
 
                for c in cols:
                    while 0 in c:
                        c.remove(0)
 
        for a in range(W):
            cnt += len(cols[a])
        if res > cnt:
            res = cnt
 
    else:
        for j in range(W):
            bit[i] = j
            boo(i+1, N)
 
T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
 
    res = 181
    bit = [0]*N
    boo(0, N)
    print(f'#{tc} {res}')
```



## 3) [숫자 만들기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeRZV6kBUDFAVH)

```python
# 시간 초과
from collections import deque

def boo(i, n):
    global max_V, min_V
    if i == n:
        copy_cals = cals[:]
        copy_nums = nums[:]
        q = deque([copy_nums.pop(0)])
        while copy_cals or copy_nums:
            if len(q) == 2:
                a, b = q.popleft(), q.popleft()
                x = copy_cals.pop(0)
                if x == '+':
                    q.append(a+b)
                elif x == '-':
                    q.append(a-b)
                elif x == '*':
                    q.append(a*b)
                elif x == '/':
                    q.append(int(a/b))
            else:
                q.append(copy_nums.pop(0))
        tmp = q[0]
        if max_V < tmp:
            max_V = tmp
        if min_V > tmp:
            min_V = tmp
    else:
        for j in range(i, n):
            cals[i], cals[j] = cals[j], cals[i]
            boo(i+1, n)
            cals[i], cals[j] = cals[j], cals[i]
    return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cal = list(map(int, input().split()))
    cals = ['+']*cal[0] + ['-']*cal[1] + ['*']*cal[2] + ['/']*cal[3]
    nums = list(map(int, input().split()))
    max_V, min_V = -99999999, 99999999
    boo(0, N-1)
    print(f'#{tc} {max_V - min_V}')
   
# 정답
def dfs(i, n, s):
    global max_V, min_V
    if i == n:
        if max_V < s:
            max_V = s
        if min_V > s:
            min_V = s
    else:
        for x in range(4):
            if cal[x]:
                if x == 0:
                    cal[0] -= 1
                    dfs(i+1, n, s+num[i])
                    cal[0] += 1
                elif x == 1:
                    cal[1] -= 1
                    dfs(i+1, n, s-num[i])
                    cal[1] += 1
                elif x == 2:
                    cal[2] -= 1
                    dfs(i+1, n, s*num[i])
                    cal[2] += 1
                elif x == 3:
                    cal[3] -= 1
                    dfs(i+1, n, int(s/num[i]))
                    cal[3] += 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cal = list(map(int, input().split()))
    num = list(map(int, input().split()))
    max_V, min_V = -99999999, 99999999
    dfs(1, N, num[0])
    print(f'#{tc} {max_V - min_V}')
```



## 4) [등산로 조성](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PoOKKAPIDFAUq)

```python
# 내 풀이
def dfs(i, j, cnt):
    global res
    for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        ni, nj = i+di, j+dj
        if 0<=ni<N and 0<=nj<N and arr[ni][nj] < arr[i][j]:
            dfs(ni, nj, cnt+1)
    else:
        if res < cnt:
            res = cnt

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    res = 0

    maxH = 0
    for i in range(N):
        for j in range(N):
            if maxH < arr[i][j]:
                maxH = arr[i][j]

    for a in range(N):
        for b in range(N):
            for k in range(1, K+1):
                arr[a][b] -= k
                for i in range(N):
                    for j in range(N):
                        if arr[i][j] == maxH:
                            dfs(i, j, 1)
                arr[a][b] += k
    print(f'#{tc} {res}')

    
# 교수님 풀이
def f(i, j, N, c, K):  # c 지나온 칸 수, K 깎을 수 있는 높이
    global maxL
    if maxL < c + 1:  # 현재칸을 포함한 등산로 길이
        maxL = c + 1
    visited[i][j] = 1   # 등산로에 포함
    for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
        ni, nj = i + di, j + dj
        if 0<=ni<N and 0<=nj<N and visited[ni][nj]==0: # 등산로에 포함되지 않은 칸
            if H[i][j] > H[ni][nj]:   # 더 낮은 경우
                f(ni, nj, N, c+1, K)
            elif H[i][j] > H[ni][nj] - K:   # 깎아서 이동할 수 있는 경우
                tmp = H[ni][nj] # 깎기전 높이
                H[ni][nj] = H[i][j] - 1 # 이동할 수 있는 만큼만 깎음
                f(ni, nj, N, c+1, 0)    # 한번만 깎을 수 있으므로 K = 0
                H[ni][nj] = tmp # 복구
    visited[i][j] = 0  # 다른 경로 선택을 위해 리턴할 준비
    return
 
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    H = [list(map(int, input().split())) for _ in range(N)]
 
    # 최대 높이 찾기
    maxH = 0
    for i in range(N):
        for j in range(N):
            if maxH<H[i][j]:
                maxH = H[i][j]
 
    # 최대 높이 봉우리에서 등산로 조성해보기
    visited = [[0]*N for _ in range(N)] # 현재 만들고 있는 등산로 표시
    maxL = 0    # 최대 등산로 길이
    for i in range(N):
        for j in range(N):
            if maxH == H[i][j]:
                f(i, j, N, 0, K)
 
    print(f'#{tc} {maxL}')
```

