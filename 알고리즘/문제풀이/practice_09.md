# practice_09

## 1) [사칙연산](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV141J8KAIcCFAYD)

```python
def post_order(v):
    if v:
        post_order(int(ch1[v]))
        post_order(int(ch2[v]))
        exp.append(tree[v])
for tc in range(1, 11):
    E = int(input())
    tree = [0]*(E+1)
    ch1 = [0]*(E+1)
    ch2 = [0]*(E+1)
    for _ in range(E):
        data = list(map(str, input().split()))
        tree[int(data[0])] = data[1]
        if len(data) == 4:
            ch1[int(data[0])] = data[2]
            ch2[int(data[0])] = data[3]
    exp = []
    post_order(1)
 
    stack = []
    for x in exp:
        if x == '+':
            stack.append(float(stack.pop()) + float(stack.pop()))
        elif x == '*':
            stack.append(float(stack.pop()) * float(stack.pop()))
        elif x == '-':
            a = stack.pop()
            b = stack.pop()
            stack.append(float(b) - float(a))
        elif x == '/':
            a = stack.pop()
            b = stack.pop()
            stack.append(float(b) / float(a))
        else:
            stack.append(x)
    print(f'#{tc} {int(stack[0])}')
```



## 2) [Contact](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15B1cKAKwCFAYD&categoryId=AV15B1cKAKwCFAYD&categoryType=CODE&problemTitle=contact&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

```python
def bfs(v):
    q = [v]
    visited[v] = 1
    while q:
        n = q.pop(0)
        for i in tree[n]:
            if not visited[i]:
                q.append(i)
                visited[i] = visited[n]+1
 
for tc in range(1, 11):
    L, S = map(int, input().split())
    tree = [[] for _ in range(101)]
    arr = list(map(int, input().split()))
    for i in range(L//2):
        p, c = arr[i*2], arr[i*2+1]
        if c not in tree[p]:
            tree[p].append(c)
     
    visited = [0]*101
    bfs(S)
     
    res = 0
    for i in range(101):
        if visited[res] <= visited[i]:
            res = i
    print(f'#{tc} {res}')
```

```python
# 교수님 풀이
def BFS(s):
    q = []
    v = [0]*101
 
    q.append(s)
    v[s] = 1
    sol = s
 
    while q:
        c = q.pop(0)
        if v[sol]<v[c] or v[sol]==v[c] and sol<c:
            sol = c
 
        for j in range(1, 101):
            if adj[c][j] and v[j]==0:
                q.append(j)
                v[j]=v[c]+1
    return sol
 
T = 10
# T = int(input())
for test_case in range(1, T + 1):
    N, S = map(int, input().split())
    lst = list(map(int, input().split()))
    # [1] lst 연결값을 인접행렬에 저장
    adj = [[0]*101 for _ in range(101)]
    for i in range(0, len(lst), 2):
        adj[lst[i]][lst[i+1]]=1
    ans = BFS(S)
    print(f'#{test_case} {ans}')
```



## 3) [장훈이의 높은 선반](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV2b7Yf6ABcBBASw&categoryId=AV2b7Yf6ABcBBASw&categoryType=CODE&problemTitle=%EC%9E%A5%ED%9B%88%EC%9D%B4&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

```python
def boo(i, n, s, rs):
    global res
    if s >= B:
        if s < res:
            res = s

    elif i == n:
        return

    elif s + rs < B:
        return

    else:
        boo(i + 1, n, s + staff[i], rs - staff[i])
        boo(i + 1, n, s, rs - staff[i])

T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    staff = list(map(int, input().split()))
    res = sum(staff)
    boo(0, N, 0, sum(staff))
    print(f'#{tc} {res - B}')
```

```python
def DFS(n, ssum):
    global ans
     
    if ssum >= B+ans:
        return
     
    if n==N:
        if ssum >= B and ans > ssum-B:
            ans = ssum-B
        return
 
    DFS(n+1, ssum+lst[n]) # 포함하는 경우
    DFS(n+1, ssum)  # 포함하지 않는 경우
 
 
T = int(input())
# T = 10
for test_case in range(1, T + 1):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))
    ans = 12345678
    DFS(0, 0)
    print(f'#{test_case} {ans}')
```



## 4) [정사각형 방](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LtJYKDzsDFAXc&categoryId=AV5LtJYKDzsDFAXc&categoryType=CODE&problemTitle=%EC%A0%95%EC%82%AC%EA%B0%81%ED%98%95&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

```python
di = [0, 1, 0, -1]
dj = [-1, 0, 1, 0]
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    check = [0]*(N*N+1)
     
    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni, nj = i + di[k], j+ dj[k]
                if 0<=ni<N and 0<=nj<N and arr[i][j]+1 == arr[ni][nj]:
                    check[arr[i][j]] = 1
                    break
     
    num = max_cnt = cnt = 1
    for i in range(N*N+1):
        if check[i]:
            cnt += 1
        else:
            if max_cnt < cnt:
                max_cnt = cnt
                num = i-cnt+1
            cnt = 1
             
    print(f'#{tc} {num} {max_cnt}')
```

```python
# 교수님 풀이
def BFS(si, sj):
    q = []
    s = []
 
    q.append((si,sj))
    v[si][sj]=1
    s.append(arr[si][sj])
 
    while q:
        ci,cj = q.pop(0)
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj]==0 and \
                abs(arr[ci][cj]-arr[ni][nj])==1:
                q.append((ni,nj))
                v[ni][nj]=1
                s.append(arr[ni][nj])
    return min(s), len(s)                
 
# T = 10
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [[0]*N for _ in range(N)]
    num = N*N
    cnt = 0
    for i in range(N):
        for j in range(N):
            if v[i][j]==0:
                tn, tc = BFS(i, j)
                if cnt<tc or cnt==tc and num>tn:
                    cnt=tc
                    num=tn
    print(f'#{test_case} {num} {cnt}')
```



## 5) [탈주범 검거](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpLlKAQ4DFAUq&categoryId=AV5PpLlKAQ4DFAUq&categoryType=CODE&problemTitle=%ED%83%88%EC%A3%BC%EB%B2%94&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

```python
di = [-1, 0, 1, 0] # 상 우 하 좌
dj = [0, 1, 0, -1]
def bfs(i, j):
    q = []
    q.append((i, j))
    visited[i][j] = 1
    while q:
        i, j = q.pop(0)
        if visited[i][j] == L:
            break
        if arr[i][j] in [1, 2, 4, 7]:
            ni, nj = i+di[0], j+dj[0]
            if 0<=ni<N and 0<=nj<M and not visited[ni][nj] and arr[ni][nj] in [1, 2, 5, 6]:
                q.append((ni,nj))
                visited[ni][nj] = visited[i][j] + 1
        if arr[i][j] in [1, 3, 4, 5]:
            ni, nj = i+di[1], j+dj[1]
            if 0<=ni<N and 0<=nj<M and not visited[ni][nj] and arr[ni][nj] in [1, 3, 6, 7]:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
        if arr[i][j] in [1, 2, 5, 6]:
            ni, nj = i+di[2], j+dj[2]
            if 0<=ni<N and 0<=nj<M and not visited[ni][nj] and arr[ni][nj] in [1, 2, 4, 7]:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
        if arr[i][j] in [1, 3, 6, 7]:
            ni, nj = i+di[3], j+dj[3]
            if 0<=ni<N and 0<=nj<M and not visited[ni][nj] and arr[ni][nj] in [1, 3, 4, 5]:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
 
T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    bfs(R, C)
    cnt = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j]:
                cnt += 1
    print(f'#{tc} {cnt}')
```

```python
# 교수님 풀이
pipe = [[0,0,0,0],[1,1,1,1],[1,1,0,0],[0,0,1,1],[1,0,0,1],[0,1,0,1],[0,1,1,0],[1,0,1,0]]
di, dj = (-1,1,0,0), (0,0,-1,1)
opp = [1,0,3,2]
def BFS(N, M, si, sj, L):
    q = []
    v = [[0]*M for _ in range(N)]
 
    q.append((si,sj))
    v[si][sj]=1
    cnt = 1
 
    while q:
        ci,cj = q.pop(0)
 
        if v[ci][cj]==L:
            return cnt
 
        for k in range(4):
            ni,nj = ci+di[k], cj+dj[k]
            if 0<=ni<N and 0<=nj<M and v[ni][nj]==0 and\
                pipe[arr[ci][cj]][k] and pipe[arr[ni][nj]][opp[k]]:
                q.append((ni,nj))
                v[ni][nj]=v[ci][cj]+1
                cnt+=1
    return cnt
 
# T = 10
T = int(input())
for test_case in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = BFS(N, M, R, C, L)
    print(f'#{test_case} {ans}')
```



## 6) [요리사](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeUtVakTMDFAVH&categoryId=AWIeUtVakTMDFAVH&categoryType=CODE&problemTitle=%EC%9A%94%EB%A6%AC%EC%82%AC&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

```python
def boo(i):
    if bit.count(1) == N//2:
        global min_cnt
        comb1 = []
        comb2 = []
        for j in range(N):
            if bit[j]:
                comb1.append(j)
            else:
                comb2.append(j)
 
        cnt1 = 0
        for j in comb1:
            for k in comb1:
                if j != k:
                    cnt1 += arr[j][k]
        cnt2 = 0
        for j in comb2:
            for k in comb2:
                if j != k:
                    cnt2 += arr[j][k]
 
        if min_cnt > abs(cnt1-cnt2):
            min_cnt = abs(cnt1-cnt2)
 
    elif i == N:
        return
 
    else:
        bit[i] = 0
        boo(i+1)
        bit[i] = 1
        boo(i+1)
 
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
 
    min_cnt = 20000*8*7
    bit = [0]*N
    boo(0)
    print(f'#{tc} {min_cnt}')
```

```python
# 교수님 풀이
def DFS(n, alst, blst):
    global ans
    if n==N:
        if len(alst)==len(blst):
            asum = bsum = 0
            for i in range(len(alst)):
                for j in range(len(alst)):
                    asum += arr[alst[i]][alst[j]]
                    bsum += arr[blst[i]][blst[j]]
            if ans > abs(asum-bsum):
                ans = abs(asum-bsum)
        return
 
    DFS(n+1, alst+[n], blst)
    DFS(n+1, alst, blst+[n])
 
# T = 10
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 12345678
    DFS(0, [], [])
    print(f'#{test_case} {ans}')
```



## 7) [세제곱근을 찾아라](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXVyCaKugQDFAUo&categoryId=AWXVyCaKugQDFAUo&categoryType=CODE&problemTitle=%EC%84%B8%EC%A0%9C%EA%B3%B1%EA%B7%BC&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

```python
for t in range(1, int(input())+1):
    N, r, i = int(input()), -1, 0
    while i**3<N:
        i += 1
        if i**3==N:
            r = i
    print(f'#{t} {r}')
```

```python
def f(N):
    s = 0
    e = 1000000
    while s <= e:
        m = (s + e) // 2
        if arr[m] == N:  # 찾음
            return m
        elif arr[m] < N:
            s = m+1
        else:
            e = m-1
    return -1
 
T = int(input())
arr = [x*x*x for x in range(1000001)]
for tc in range(1, T+1):
    N = int(input())
 
    print(f'#{tc} {f(N)}')
```

