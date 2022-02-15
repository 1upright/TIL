# practice_02



## 1) 색칠하기

10X10 격자에 x1, y1, x2, y2, color(빨강 = 1, 파랑 = 2)를 N번 받아서 (x1, y1)부터 (x2, y2)까지 해당 색깔로 칠한 후 보라색 칸의 개수 구하기

```python
T = int(input())
for tc in range(1,T+1):
    arr = [[0]*10 for _ in range(10)]
    N = int(input())
    for _ in range(N):
        x1, y1, x2, y2, color = map(int, input().split())
        if color == 1:
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    arr[i][j] += 1
        else:
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    arr[i][j] += 2
        cnt = 0 # 여기서부터 cnt += 1까지 한칸 앞으로 땡겼으면 실행 속도를 줄일 수 있었음
        for i in range(10):
            for j in range(10):
                if arr[i][j] == 3:
                    cnt += 1
    print(f'#{tc} {cnt}')
```



## 2) 특별한 정렬

> 1 2 3 4 5 6 7 8 9 10 => 10 1 9 2 8 3 7 4 6 5

```python
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N):
        if i % 2:
            minidx = i
            for j in range(i+1, N):
                if arr[minidx] > arr[j]:
                    minidx = j
            arr[i], arr[minidx] = arr[minidx], arr[i]
        else:
            maxidx = i
            for j in range(i+1, N):
                if arr[maxidx] < arr[j]:
                    maxidx = j
            arr[i], arr[maxidx] = arr[maxidx], arr[i]

    new_arr = []
    for i in range(10):
        new_arr.append(arr[i])
    print(f'#{tc}', end=' ')
    print(*new_arr)
```



## 3) 이진탐색

> page, A, B 받고 A, B가 page에 대해서 이진탐색(업다운 게임)을 했을 때 누가 빨리 page를 찾을까?

```python
def binary(n, key):
    l = 1
    r = n
    cnt = 0
    while l <= r:
        c = int((l+r)/2)
        if c == key:
            cnt += 1
            return cnt
        elif c > key:
            cnt += 1
            r = c
        else:
            cnt += 1
            l = c
    return False
 
T = int(input())
for tc in range(1, T+1):
    page, A, B = map(int, input().split())
    if binary(page, A) > binary(page, B):
        print(f'#{tc} B')
    elif binary(page, A) < binary(page, B):
        print(f'#{tc} A')
    else:
        print(f'#{tc} 0')
```



## 4) 부분집합의 합

> 1~12까지의 원소를 가진 집합의 부분집합 중에서 원소의 개수는 N이고 원소의 합은 K인 것은 몇개일까?

```python
A = list(range(1, 13))
 
T = int(input())
for tc in range(1,T+1):
    N, K = map(int, input().split())
 
    cnt = 0
    for i in range(1, 1<<12):
        subset = []
        my_sum = 0
        for j in range(12):
            if i & (1<<j):
                subset.append(j+1)
                my_sum += j+1
        if len(subset) == N and my_sum == K:
            cnt += 1
    print(f'#{tc} {cnt}')
    
    
## 더 깔끔했을 코드
T = int(input())
for tc in range(1,T+1):
    N, K = map(int, input().split())

    cnt = 0
    for i in range(1, 1<<12):
        my_len = 0
        my_sum = 0
        for j in range(12):
            if i & (1<<j):
                my_len += 1
                my_sum += j+1
        if my_len == N and my_sum == K:
            cnt += 1
    print(f'#{tc} {cnt}')
```



## 5) [ladder1](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14ABYKADACFAYh&categoryId=AV14ABYKADACFAYh&categoryType=CODE&problemTitle=ladder&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

```python
for _ in range(10):
    tc = int(input())
    arr = [[0]*102] + [[0]+ list(map(int, input().split())) + [0] for _ in range(100)] + [[0]*102]
    si = 100 # 종점의 i는 100
    for j in range(102):
        if arr[100][j] == 2: # 종점의 sj 설정
            sj = j

    while 1: # break 나올때까지
        if not arr[si-1][sj]: # 위에가 0이면 sj 저장 후 종료
            result = sj
            break

        elif arr[si][sj+1]: # 우측에 1 있으면
            while arr[si][sj+1]: # 우측에 0나오기 전까지 계속
                sj += 1
            si -= 1 # 한 줄 올라감

        elif arr[si][sj-1]:
            while arr[si][sj-1]:
                sj -= 1
            si -= 1

        else: # 그 외에는 계속 올라감
            si -= 1

    print(f'#{tc} {result-1}')
```

