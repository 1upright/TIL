# practice_03



## 1) 문자열 비교

> str1 str2 받고 str2 안에 str1과 일치하는 부분이 있는지

```python
# kmp 알고리즘
def kmp(p, t):
    N, M, j = len(t), len(p), 0
    lps = [0]*(M+1)
 
    lps[0] = -1
    for i in range(1, M):
        lps[i] = j
        if p[i] == p[j]:
            i += 1
            j += 1
        else:
            j = 0
    lps[M] = j
 
    i = j = 0
    while i < N and j <= M:
        if t[i] == p[j] or j == -1:
            i += 1
            j += 1
        else:
            j = lps[j]
        if j == M:
            return 1
    return 0
 
T = int(input())
for tc in range(1, T+1):
    print(f'#{tc} {kmp(input(), input())}')
    
## 숏코딩
for t in range(int(input())): print(f'#{t+1} {int(input() in input())}')
```



## 2) 회문

> N, M 받고 NxN 배열 중에 길이가 M인 회문이 있을까? 

```python
def tester(str_):
    for i in range(len(str_)//2):
        if str_[i] != str_[-1-i]:
            return False
    return True
 
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
 
    for i in range(N):
        for j in range(N-M+1):
            check = ''
            for k in range(j, j+M):
                check += arr[i][k]
            if tester(check):
                result = check
 
    for j in range(N):
        for i in range(N-M+1):
            check = ''
            for k in range(i, i+M):
                check += arr[k][j]
            if tester(check):
                result = check
    print(f'#{tc} {result}')
```



## 3) 글자수

> str1, str2 받고 str1의 문자 중 str2에 가장 많은 것 개수

```python
T = int(input())
for tc in range(1, T+1):
    s1 = input()
    s2 = input()
    cnt = [0]*len(s1)
    for i in range(len(s1)):
        for char in s2:
            if s1[i] == char:
                cnt[i] += 1
    max_cnt = cnt[0]
    for val in cnt:
        if val > max_cnt:
            max_cnt = val
    print(f'#{tc} {max_cnt}')
```



## 4) [의석이의 세로로 말해요](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWVWgkP6sQ0DFAUO)

```python
T = int(input())
for tc in range(1, T+1):
    arr = [list(input()) for _ in range(5)]
    max_len = len(arr[0])
     
    for i in range(5):
        if max_len < len(arr[i]):
            max_len = len(arr[i])
    for i in range(5):
        if max_len != len(arr[i]):
            for j in range(max_len - len(arr[i])):
                arr[i].append('!')
 
    words = ''
    for j in range(max_len):
        for i in range(5):
            if arr[i][j] != '!':
                words += arr[i][j]
                 
    print(f'#{tc} {words}')
```



## 5) [쇠막대기 자르기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWVl47b6DGMDFAXm&categoryId=AWVl47b6DGMDFAXm&categoryType=CODE&problemTitle=%EC%87%A0%EB%A7%89%EB%8C%80%EA%B8%B0&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

```python
# 처음에 했던 것 => 런타임 초과
T = int(input())
for tc in range(1, T+1):
    signal = '!' + input()
    cnt = 0 # 레이저가 쇠막대기를 통과할 때마다 카운트해줄 거임
    lazor = 0 # (전체 길이 - 레이저가 만든 괄호) // 2 == 처음 막대기 개수를 구하기 위해 lazor를 셈
 
    for P in range(len(signal)): # signal 안의 괄호들 중
        if signal[P] == '(' and signal[P+1] == ')': # 만약 레이저를 만났다면
            lazor += 1
            op = cl = 0 # 여는괄호랑 닫는괄호 세줄거임
            for i in range(P): # 레이저가 통과한 시점의 왼쪽 괄호들을 보았을 때
                if signal[i] == '(':
                    op += 1
                elif signal[i] == ')':
                    cl += 1
            cnt += op - cl # 여는 괄호와 닫는 괄호의 개수 차 == 레이저가 통과한 쇠막대기의 개수 == 레이저로 인해 분리된 쇠막대기 개수
 
    result = (len(signal)-1 - lazor*2)//2 + cnt
    print(f'#{tc} {result}')
    
    
## 코드를 줄여봤음 => 그래도 런타임 초과
T = int(input())
for tc in range(1, T+1):
    sig = '!' + input()
    cnt = 0
    lazor = 0
 
    for P in range(len(sig)):
        if sig[P] == '(' and sig[P+1] == ')':
            lazor += 1
            for i in range(P):
                if sig[i] == '(':
                    cnt += 1
                elif sig[i] == ')':
                    cnt -= 1
 
    cnt += (len(sig)-1 - lazor*2)//2
    print(f'#{tc} {cnt}')
    
    
### 조건문 안에 조건문 잔뜩 넣지 말고 간단하게 => 성공
T = int(input())
for tc in range(1, T+1):
    sig = list(input()) # 레이저는 바꿔줄거라 리스트로
    cnt = 0 # 총 막대의 수 == 처음 막대의 수 + 레이저가 지진 막대 수
    now = 0
 
    for i in range(len(sig)):
        if sig[i] == '(' and sig[i+1] == ')': # 레이저를 Rr로 바꿈
            sig[i], sig[i+1] = 'R', 'r'
 
    for i in range(len(sig)):
        if sig[i] == '(': ## 레이저가 전부 Rr이 된 상황에서 (는 막대의 시작점 뿐
            cnt += 1
            now += 1
        elif sig[i] == ')':
            now -= 1
        elif sig[i] == 'R': ## 레이저가 지진 막대 수
            cnt += now
 
    print(f'#{tc} {cnt}')
```



## 6) [자기 방으로 돌아가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWNcJ2sapZMDFAV8&categoryId=AWNcJ2sapZMDFAV8&categoryType=CODE&problemTitle=%EC%9E%90%EA%B8%B0+%EB%B0%A9%EC%9C%BC%EB%A1%9C&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

```python
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    hall = [0]*200
 
    for i in range(N):
        for j in range(2):
            arr[i][j] -= 1
            arr[i][j] //= 2
 
    for i in range(N):
        if arr[i][0] > arr[i][1]:
            arr[i][0], arr[i][1] = arr[i][1], arr[i][0]
 
    for i in range(N):
        for j in range(arr[i][0], arr[i][1]+1):
            hall[j] += 1
 
    max_hall = hall[0]
    for i in range(200):
        if hall[i] > max_hall:
            max_hall = hall[i]
    print(f'#{tc} {max_hall}')
```



## 7) 회문2

> 100X100 입력된 배열 중 가장 긴 회문의 길이는?

```python
# 런타임 너무 길긴 함

def tester(str_):
    for i in range(len(str_) // 2):
        if str_[i] != str_[-1 - i]:
            return False
    return True

for _ in range(10):
    tc = int(input())
    arr = [list(input()) for _ in range(100)]

    result1 = result2 = 0

    for M in range(100, 0, -1):
        for i in range(100):
            for j in range(100 - M + 1):
                check = ''
                for k in range(j, j + M):
                    check += arr[i][k]
                if tester(check):
                    result1 = M
                    break

        for j in range(100):
            for i in range(100 - M + 1):
                check = ''
                for k in range(i, i + M):
                    check += arr[k][j]
                if tester(check):
                    result2 = M
                    break

        if result1 or result2:
            break
    if result1 >= result2:
        print(f'#{tc} {result1}')
    if result2 > result1:
        print(f'#{tc} {result2}')
```

