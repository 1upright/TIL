# practice_06

## 1) Forth

> 후위 표기법 계산기, `.` 나오면 숫자 꺼내 출력, 형식이 잘못되어 연산이 불가능한 경우 'error' 출력

```python
def calc(s):
    stack = []
    for x in s:
        try:
            if '0' <= x <= '9':
                stack.append(x)
            elif x == '+':
                stack.append(int(stack.pop())+int(stack.pop()))
            elif x == '*':
                stack.append(int(stack.pop())*int(stack.pop()))
            elif x == '/':
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a // b)
            elif x == '-':
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a - b)
            elif x == '.':
                if len(stack) == 1:
                    return stack[0]
                else:
                    return 'error'
        except:
            return 'error'
T = int(input())
for tc in range(1, T+1):
    expr = list(map(str, input().split()))
    print(f'#{tc} {calc(expr)}')
 
# try, except 없이 풀기
def calc(s):
    stack = []
    for x in s:
        if '0' <= x <= '9':
            stack.append(x)
        elif x in ('+', '*', '/', '-') and len(stack) < 2:
            return 'error'
        elif x == '+':
            stack.append(int(stack.pop())+int(stack.pop()))
        elif x == '*':
            stack.append(int(stack.pop())*int(stack.pop()))
        elif x == '/':
            b = int(stack.pop())
            a = int(stack.pop())
            if not b:
                return 'error'
            stack.append(a // b)
        elif x == '-':
            b = int(stack.pop())
            a = int(stack.pop())
            stack.append(a - b)
        elif x == '.':
            if len(stack) == 1:
                return stack[0]
            else:
                return 'error'

T = int(input())
for tc in range(1, T+1):
    expr = list(map(str, input().split()))
    print(f'#{tc} {calc(expr)}')
```



## 2) 토너먼트 카드게임

> i번부터 j번까지 i~(i+j)//2와 (i+j)//2+1~j 두 그룹으로 나눠서 승자를 계속 뽑는다.
>
> 1 == 가위, 2 == 바위, 3 == 보

```python
def rps(a, b):
    A, B = card[a-1], card[b-1]
    if A == B:
        return a
    elif (A == 1 and B == 3) or (A == 2 and B == 1) or (A == 3 and B == 2):
        return a
    else:
        return b
 
def tourn(i, j):
    if i == j:
        return i
    else:
        L = tourn(i, (i+j)//2)
        R = tourn((i+j)//2 + 1, j)
        return rps(L, R)
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card = list(map(int, input().split()))
    print(f'#{tc} {tourn(1, N)}')
```



## 3) 미로

```python
# 고심 끝에 나온 코드
di = [-1, 0, 1, 0] # 상 우 하 좌
dj = [0, 1, 0, -1]

def maze(i, j):
    visited[i][j] = 1
    while stack:
        i, j = stack.pop()
        for a in range(4):
            ni = i + di[a]
            nj = j + dj[a]
            if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0:
                if arr[ni][nj] == '0':
                    stack.append([ni, nj])
                    visited[i][j] = 1
                if arr[ni][nj] == '3':
                    return 1
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                si, sj = i, j
    stack = [[si, sj]]
    visited = [[0]*N for _ in range(N)]
    print(f'#{tc} {maze(si, sj)}')
    
### 교수님 코드
def fstart(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j
    return -1, -1

def dfs1(i, j, N):  # 스택 사용
    stack = []      # 스택생성
    visted = [[0]*N for _ in range(N)]  # visited생성
    while (1):
        # i, j 칸 방문
        visted[i][j] = 1
        if maze[i][j] == 3:  # 목적지면
            return 1
        # 현재 위치 i, j에서 갈 수 있는 곳 탐색
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            # 미로 내부, 벽이 아니고(통로 or 도착칸), 방문하지 않은 칸
            if 0<=ni<N and 0<=nj<N and maze[ni][nj]!=1 and visted[ni][nj]==0:
                stack.append((i, j))    # 현재 위치 스택에 저장
                i, j = ni, nj           # ni, nj로 이동
                break                   # ni, nj 방문
        else: # 갈수있는 칸이 없으면
            if stack:                   # 뒷걸음질
                i, j = stack.pop()
            else:                       # 출발지까지 되돌아온경우
                break                   # 3번칸에 도착할 수 없는 상황
    return 0

def dfs2(i, j, N):      # 재귀
    visited[i][j] = 1
    if maze[i][j]==3:
        return 1
    else:
        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and maze[ni][nj]!=1 and visited[ni][nj]==0:
                if dfs2(ni, nj, N):
                    return 1
        return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    # 출발위치 찾기
    sti, stj = fstart(N)

    # 미로 탐색
    #ans = dfs1(sti, stj, N)
    #print(f'#{tc} {ans}')
    visited = [[0]*N for _ in range(N)] # dfs2 용
    print(f'#{tc} {dfs2(sti, stj, N)}')
```



## 4) 배열 최소 합

```python
# 실행시간 오래 걸림
def f(i, N):
    global min_cnt
    if i == N:
        cnt = 0
        for idx in range(N):
            cnt += arr[idx][p[idx]]
        if min_cnt > cnt:
            min_cnt = cnt
    else:
        for j in range(i, N):
            p[i], p[j] = p[j], p[i]
            f(i + 1, N)
            p[i], p[j] = p[j], p[i]  # 원상복구
    return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_cnt = 0
    for i in range(N):
        min_cnt += arr[i][i]

    p = list(range(N))
    f(0, N)

    print(f'#{tc} {min_cnt}')
    
    
# 가지치기 이용해서 짧게
def boo(i, n, s):
    global min_cnt

    if i == n:
        if min_cnt > s:
            min_cnt = s

    elif min_cnt < s:
        return

    else:
        for j in range(n):
            if not visited[j]:
                visited[j] += 1
                boo(i+1, n, s+arr[i][j])
                visited[j] -= 1
    return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N

    min_cnt = 0
    for i in range(N):
        min_cnt += arr[i][i]

    boo(0, N, 0)
    print(f'#{tc} {min_cnt}')
```



## 5) 계산기 3

> 주어진 식을 후위 표기식으로 바꾼 후에 그것을 계산하는 프로그램 만들기(연산자는 '+'와 '*', 그리고 괄호)

```python
for tc in range(1, 11):
    N = int(input())
    exp = input()
    stack = []
    res = []
    icp = {'+': 1, '*': 2, '(': 3}
    isp = {'+': 1, '*': 2, '(': 0}
    for x in exp:
        if '0' <= x <= '9':
            res.append(x)
        elif x == ')':
            while isp[stack[-1]]:
                res.append(stack.pop())
            stack.pop()
        else:
            while stack and isp[stack[-1]] >= icp[x]:
                res.append(stack.pop())
            stack.append(x)
    while stack:
        res.append(stack.pop())

    for x in res:
        if x == '+':
            stack.append(int(stack.pop()) + int(stack.pop()))
        elif x == '*':
            stack.append(int(stack.pop()) * int(stack.pop()))
        else:
            stack.append(x)
    print(f'#{tc} {stack[0]}')
```

