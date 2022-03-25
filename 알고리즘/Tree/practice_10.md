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

```python
# 교수님 풀이
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [[0]*(N+1) for _ in range(N+1)]
    arr[N//2][N//2]=arr[N//2+1][N//2+1] = 2 # 초기 돌 놓기
    arr[N//2+1][N//2]=arr[N//2][N//2+1] = 1 # 초기 돌 놓기
    for _ in range(M):
        sj, si, d = map(int, input().split())
        arr[si][sj]=d
        for di,dj in ((-1,-1),(-1,0),(-1,1),(1,-1),(1,0),(1,1),(0,-1),(0,1)):
            s = []
            for k in range(1, N):
                ni,nj = si+di*k, sj+dj*k
                if 1<=ni<=N and 1<=nj<=N:
                    if arr[ni][nj]==0:
                        break
                    elif arr[ni][nj]==d:
                        for ci,cj in s:
                            arr[ci][cj]=d
                        break
                    else:
                        s.append((ni,nj))
                else:
                    break
    bcnt = wcnt = 0
    for lst in arr:
        bcnt += lst.count(1)
        wcnt += lst.count(2)
    print(f'#{test_case} {bcnt} {wcnt}')
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

```python
# 교수님 풀이
def solve(lst3):
    for i in range(len(lst2)):
        # 1비트 값만 바꿔서 10진수 값으로 변환
        lst2[i] = (lst2[i]+1)%2
 
        dec = 0 # 10진수로 변환
        for idx in range(len(lst2)):
            dec = dec*2 + lst2[idx]
 
        s = []  # 3진수로 변환
        ret = dec
        while dec>0:
            s.append(dec%3)
            dec //= 3
        lst = lst3[::-1]
 
        cnt = 0
        for idx in range(min(len(s), len(lst))):
            if s[idx]!=lst[idx]:
                cnt+=1
        cnt += abs(len(s)-len(lst)) # 길이가 다르다면 다른값
 
        if cnt == 1:
            return ret
 
        lst2[i] = (lst2[i] + 1) % 2 # 원래대로 복구
 
 
T = int(input())
for test_case in range(1, T + 1):
    lst2 = list(map(int, input()))
    lst3 = list(map(int, input()))
    ans = solve(lst3)
    print(f'#{test_case} {ans}')
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

```python
# 교수님 풀이
def DFS(n, ci, cj, num):
    if n==7:
        sset.add(num)
        return
 
    for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
        ni,nj = ci+di, cj+dj
        if 0<=ni<4 and 0<=nj<4:
            DFS(n+1, ni, nj, num+str(arr[ni][nj]))
 
T = int(input())
for test_case in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    sset = set()
    for i in range(4):
        for j in range(4):
            DFS(0, i, j, '')
    print(f'#{test_case} {len(sset)}')
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

```python
# 교수님 풀이
T = int(input())
di,dj = (0,-1,1,0,0),(0,0,0,-1,1)
opp = [0,2,1,4,3]
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(K)]
    for _ in range(M):
        # [1] 각각의 미생물 이동 후 경계처리
        for i in range(len(arr)):
            arr[i][0] = arr[i][0]+di[arr[i][3]]
            arr[i][1] = arr[i][1]+dj[arr[i][3]]
            if arr[i][0]==0 or arr[i][0]==N-1 or arr[i][1]==0 or arr[i][1]==N-1:
                arr[i][2]//=2
                arr[i][3] = opp[arr[i][3]]
 
        # [2] 정렬(좌표, 개수) 내림차순
        arr.sort(key=lambda x:(x[0],x[1],x[2]), reverse=True)
 
        # [3] 같은 좌표인 경우, 큰 미생물로 합치기
        i = 1
        while i<len(arr):
            if arr[i-1][0]==arr[i][0] and arr[i-1][1]==arr[i][1]:
                arr[i-1][2] += arr[i][2]
                arr.pop(i)
            else:
                i+=1
 
    ans = 0
    for i in range(len(arr)):
        ans += arr[i][2]
 
    print(f'#{test_case} {ans}')
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

```python
# 교수님 풀이
#1 단순무식하지만, 꼼꼼하게 따져보면 제일 쉽게 접근하는 방법일수도 있습니다
def solve_loop():
    sol = 0
    for si in range(N):
        for sj in range(N):
            for k in range(1,2*N):
                cnt = 0
                for i in range(si-k+1, si+k):
                    for j in range(sj-k+1+abs(i-si), sj+k-abs(i-si)):
                        if 0<=i<N and 0<=j<N and arr[i][j]:
                            cnt += 1
                if k*k+(k-1)*(k-1)<=cnt*M and sol<cnt:
                    sol=cnt
    return sol
 
#2 루프보다 효율적 => K를 늘려가면서 추가되는 부분만 카운트하기 때문에...
def BFS(si, sj):
    q = []
    v = [[0]*N for _ in range(N)]
    sol = cnt = old = 0
 
    q.append((si,sj))
    v[si][sj]=1
    if arr[si][sj]:
        cnt+=1
 
    while q:
        ci,cj = q.pop(0)
        if old != v[ci][cj]:
            old = v[ci][cj]
            if cost[v[ci][cj]]<=cnt*M and sol<cnt:
                sol = cnt
 
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj]==0:
                q.append((ni,nj))
                v[ni][nj]=v[ci][cj]+1
                if arr[ni][nj]:
                    cnt += 1
    return sol
 
def solve_bfs():
    sol = 0
    for si in range(N):
        for sj in range(N):
            t = BFS(si, sj)
            if sol<t:
                sol=t
    return sol

#3 테이블에 저장해놓고 활용하는 가장 좋은 풀이법입니다
def solve_tbl():
    home = []
    sol = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                home.append((i,j))
 
    for si in range(N):
        for sj in range(N):
            cnts = [0]*40
            for ci,cj in home:
                dist = abs(si-ci)+abs(sj-cj)+1
                cnts[dist]+=1
            for i in range(1,40):
                cnts[i]+=cnts[i-1]
 
            for k in range(1,40):
                if cost[k]<=cnts[k]*M and sol<cnts[k]:
                    sol = cnts[k]
    return sol
 
cost = [0]+[k * k + (k - 1) * (k - 1) for k in range(1, 40)]
T = int(input())
# T = 10
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # ans = solve_loop()
    # ans = solve_bfs()
    ans = solve_tbl()
    print(f'#{test_case} {ans}')
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

```python
# 교수님 풀이
def DFS(n, ci, cj, v):
    global si, sj, ans
    if n==2 and ans>=len(v)*2:
        return
    if n>3: # 종료조건
        return
    if ci==si and cj==sj and n==3 and ans<len(v):  # 정답 갱신
        ans = len(v)
        return
 
    for k in range(n, n+2):
        ni,nj = ci+di[k], cj+dj[k]
        if 0<=ni<N and 0<=nj<N and arr[ni][nj] not in v:
            v.append(arr[ni][nj])
            DFS(k, ni, nj, v)
            v.pop()
 
di,dj = (1,1,-1,-1,1),(-1,1,1,-1,-1)
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = -1
    for si in range(0, N-2):
        for sj in range(1,N-1):
            DFS(0, si, sj, [])
    print(f'#{test_case} {ans}')
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

```python
# 교수님 풀이
def DFS(n, ssum):
    global ans
    if n>12:
        if ans>ssum:
            ans = ssum
        return
 
    DFS(n+1, ssum+lst[n]*day)   # 일일권
    DFS(n+1, ssum+mon)          # 월간
    DFS(n+3, ssum+mon3)         # 분기
    DFS(n+12, ssum+year)        # 년간
 
T = int(input())
for test_case in range(1, T + 1):
    day, mon, mon3, year = map(int, input().split())
    lst = [0]+list(map(int, input().split()))
    # ans = 12345678
    # DFS(1, 0)
    # print(f'#{test_case} {ans}')
    D = [0]*13
    for i in range(1, 13):
        mmin = D[i-1]+lst[i]*day
        mmin = min(mmin, D[i-1]+mon)
        if i>=3:
            mmin = min(mmin, D[i - 3] + mon3)
        if i>=12:
            mmin = min(mmin, D[i - 12] + year)
        D[i]=mmin
    print(f'#{test_case} {D[12]}')
```

