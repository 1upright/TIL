# Stack2

## DFS 알고리즘

> 시작 정점의 한 뱡향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색해 가다가 더 이상 갈 곳이 없게 되면, 가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아와서 다른 방향의 정점으로 탐색을 계속 반복하여 결국 모든 정점을 방문하는 순회 방법

- 가장 마지막에 만났던 갈림길의 정점으로 되돌아가 다시 탐색해야하므로 후입선출 구조의 스택 사용

- 예시) 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7 => 1-2-4-6-5-7-3
  - 인접행렬 만들고 스택 쌓아가면서 가다가 갈 곳이 없으면 그 전 갈림길로 되돌아오길 반복



## 계산기

> 문자열로 된 계산식이 주어질 때, 이 계산식의 값을 계산하려면?

- 중위표기식을 후위표기식으로 변환
- 스택을 이용하여 해당식을 읽는다
  1. 입력 받은 중위 표기식에서 토큰을 읽는다
  2. 토큰이 피연산자이면 토큰을 출력
  3. 토큰이 연산자(괄호포함)인 경우
     - 이 토큰이 스택의 top에 저장되어 있는 연산자보다 우선순위가 높으면 or 스택의 top에 저장된 연산자가 없을 경우 => push
     - 토큰이 스택의 top에 저장되어 있는 연산자보다 우선순위가 낮거나 같은 경우 => 연산자의 우선순위가 토큰의 우선순위보다 작을 때까지 스택에서 pop한 후 토큰의 연산자를 push
  4. 토큰이 오른쪽 괄호 `)`이면 스택의 top에 왼쪽 괄호 `(`가 올 때까지 스택에 pop 연산을 수행하고 pop한 연산자를 출력 => 이 때 만난 `(`를 pop만 하고 출력하지 않는다
  5. 중위 표기식에  더 읽을 것이 없다면 중지하고, 더 읽을 것이 있다면 1부터 다시 반복한다
  6. 스택에 남아 있는 연산자를 모두 pop하여 출력
     - 스택 밖의 `(`는 우선 순위가 가장 높고, 스택 안의 `(`는 우선 순위가 가장 낮다



#### 연산자의 우선순위(점수)

- icp (in-coming priority, stack의 밖에 있고 새로 들어올 때)
  - `(` : 3
  - `*`, `/` : 2
  - `+`, `-` : 1
- isp (in-stack priority, stack의 안에서 읽혀 나올 때)
  - `(` : 0
  - `*`, `/` : 2
  - `+`, `-` : 1



#### 연습문제1

> 식을 후위 표기법으로 출력

- ex) 2 + 3 * 4 / 5 => 2 3 4 * 5 / +

```python
# append, pop을 이용
exp = input()
stack = []
res = []
icp = {'+': 1, '-': 1, '*': 2, '/': 2}
for x in exp:
    if '0' <= x <= '9':
        res.append(x)
    else:
        if stack and icp[stack[-1]] >= icp[x]:
            res.append(stack.pop())
        stack.append(x)
while stack:
    res.append(stack.pop())
print(*res)

## top의 방법을 이용
exp = input()
stack = [0]*len(exp)
res = ''
top = -1
icp = {'+': 1, '-': 1, '*': 2, '/': 2}

for i in range(len(exp)):
    if '0' <= exp[i] <= '9':
        res += exp[i]
    else:
        if top > -1 and icp[stack[top]] >= icp[exp[i]]:
            res += stack[top]
            top -=1
        top += 1
        stack[top] = exp[i]
while top > -1:
    res += stack[top]
    top -= 1
print(res)
```



#### 연습문제2

> 주어진 식을 후위 표기식으로 바꾼 후에 그것을 계산하는 프로그램 만들기(연산자는 '+'와 '*'만)

- ex) 3+4+5*6+7 => 44

```python
# append, pop으로 풀기
for tc in range(1, 11):
    N = int(input())
    exp = input()
    stack = []
    res = []
    icp = {'+': 1, '*': 2}
    for x in exp:
        if '0' <= x <= '9':
            res.append(x)
        else:
            if stack and icp[stack[-1]] >= icp[x]:
                res.append(stack.pop())
            stack.append(x)
    while stack:
        res.append(stack.pop())

    for x in res:
        if x == '+':
            stack.append(int(stack.pop())+int(stack.pop()))
        elif x == '*':
            stack.append(int(stack.pop())*int(stack.pop()))
        else:
            stack.append(x)
    print(f'#{tc} {stack[0]}')

# top 이용해서 풀기
for tc in range(1, 11):
    N = int(input())
    exp = input()
    stack = [0]*len(exp)
    res = ''
    top = -1
    icp = {'+': 1, '*': 2}

    for i in range(N):
        if '0' <= exp[i] <= '9':
            res += exp[i]
        else:
            if top > -1 and icp[stack[top]] >= icp[exp[i]]:
                res += stack[top]
                top -= 1
            top += 1
            stack[top] = exp[i]
    while top > -1:
        res += stack[top]
        top -= 1

    for i in range(N):
        if res[i] == '+':
            a = int(stack[top])
            top -= 1
            b = int(stack[top])
            stack[top] = a + b
        elif res[i] == '*':
            a = int(stack[top])
            top -= 1
            b = int(stack[top])
            stack[top] = a * b
        else:
            top += 1
            stack[top] = res[i]
            
    print(f'#{tc} {stack[top]}')
```



## 백트래킹

> 해를 찾는 도중에 '막히면' 되돌아가서 다시 해를 찾아 가는 기법
>
> 최적화(optimization) 문제과 결정(decision) 문제를 해결할 수 있다

- 가지치기(pruning) 유망하지 않은 노드 포함된 경로는 더 이상 고려하지 않음



#### DFS와의 비교

- 어떤 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않으면 더 이상 그 경로를 따라가지 않음으로써 시도의 횟수를 줄임
- 백트래킹은 불필요한 경로를 조기 차단
- 깊이우선탐색 시 경우의 수가 너무 많음(N!가지의 경우의 수 다루면 처리 불가능)
- 백트래킹 알고리즘을 적용하면 일반적으로 경우의 수가 줄어들지만 이 역시 최악의 경우에는 깊이우선탐색과 같은 시간을 요함



#### 알고리즘 절차

1. 상태 공간 트리의 깊이 우선 검색 실시
2. 각 노드가 유망한지 검사
3. 노드가 유망하지 않으면 그 노드의 부모 노드로 돌아가 검색 계속

- 예시) n-Queen 문제 : 4X4 체스판에 퀸 4개 많이 놓기
  - 첫째 줄에 퀸을 놓는다(1,1)
  - 둘째 줄에 놓을 수 있는 자리에 놓는다(2, 3)
  - 셋째 줄에 놓을 수 있는데가 없음
  - 둘째 줄로 돌아가 다른 자리에 놓는다(2, 4)
  - 셋째 줄에 놓을 수 있는 자리에 놓는다(3, 2)
  - 넷째 줄에 놓을 수 있는데가 없음
  - 셋째, 둘째 줄 모두 없음
  - 첫째 줄의 퀸을 다른 곳에 놓는다(1, 2)
  - ...
  - (1, 2), (2, 4), (3, 1), (4, 3)
    - => 순수한 DFS : 155노드, 백트래킹 : 27노드



#### 부분집합 구하기

```python
def f(i, N):
    if i == N:
        print(bit, end=' ')
        for j in range(N):
            if bit[j]:
                print(a[j], end=' ')
        print()
    else: # bit 세개를 다 못채웠다면 i에 해당하는 자리에 1이나 0을 채우고 i==N될때까지 돌려
        bit[i] = 1
        f(i+1, N) # 이렇게
        bit[i] = 0
        f(i+1, N) # 두갈래로 나눠지기 때문에 2의 N승개 만큼의 부분집합이 출력
    return
a = [1, 2, 3]
bit = [0, 0, 0]
f(0, 3)
```

[1, 1, 1] 1 2 3 

[1, 1, 0] 1 2 

[1, 0, 1] 1 3 

[1, 0, 0] 1 

[0, 1, 1] 2 3 

[0, 1, 0] 2 

[0, 0, 1] 3

[0, 0, 0] 



- 연습문제

> 1~10의 powerset 중 원소의 합이 K인 부분집합을 구하시오

```python
def f(i, n, k):
    if i == n: # 드디어 bit 다 채웠어
        s = 0
        for j in range(n):
            if bit[j]: # 부분집합의 원소들을 더해주는 과정
                s += a[j]
        if s == k: # 그 합이 k와 같다면? 그 부분집합 출력해주는 과정
            for j in range(n):
                if bit[j]:
                    print(a[j], end=' ')
            print()
    else:
        bit[i] = 1
        f(i+1, n, k)
        bit[i] = 0
        f(i+1, n, k)
    return

N = 10
a = list(range(1, N+1))
bit = [0]*N
K = 50
f(0, N, K) # 합이 K인 부분집합을 찾는 함수
```

1 2 3 4 6 7 8 9 10 
1 4 5 6 7 8 9 10 
2 3 5 6 7 8 9 10 



- 가지치기 추가

> 2의 N승 번 반복하는거 너무 비효율적이야 => 그렇다면 실행시간 줄이려면?



**고려사항들..**

1. 합을 더하다가 구하려고 하는 합을 넘어가버리면 break해버리기
2. i-1까지의 부분집합에서 i로 넘어갈 때, 합 s에다가 "i가 1이면 s+a[i]를," "i가 0이면 s를" 넘겨준다면 효율적이지 않을까?
   - 이럴라면 함수 f에서 s까지 받아줘야 함 => f(i, n, k, s)
3. 여태까지 구한 합이 s이고, 남은 구간의 합이 rs일 때, s + rs가 구하려는 합보다 작다면? 더 이상 진행할 필요가 없지 않니?
   - 이럴라면 함수 f에서 res까지 받아줘야 함 => f(i, n, k, s, rs)

```python
def f(i, n, k, s, rs): # S는 i-1원소까지 고려한 합
    
    if s == k: # 추가 1-2. S == K라면 그 값 출력하고, 더 이상 더할 필요가 없음!
        for j in range(n):
                if bit[j]:
                    print(a[j], end=' ')
            print()
    
    elif i == n: # 부분집합이 완성됐는데 그 합이 K까지 도달되지 못한 경우(앞에 if문 때문에 못한 애들이 여기에)
        return
    
    elif s > k: # 추가 1. S가 원하는 합보다 넘어가면 끝내버림(더이상은 더해도 K가 될 수 없으니)
        return
    
    elif s + rs < k: # 추가 3. S + RS가 원하는 합보다 작으면 끝내버림(다 더해도 K가 될 수 없으니)
        return
    
    else: # 추가 2. 1이냐 0이냐 보고 다르게 함수 적용
        bit[i] = 1
        f(i+1, n, k, s+a[i], rs - a[i])
        bit[i] = 0
        f(i+1, n, k, s, rs - a[i])
	return

N = 10
a = list(range(1, N+1))
bit = [0]*N
K = 10
RS = sum(a)
f(0, N, K, 0, RS)
```

1 2 3 4 

1 2 7 

1 3 6 

1 4 5 

1 9 

2 3 5 

2 8 

3 7 

4 6 

10 



- [부분집합의 합](https://github.com/1upright/TIL/blob/master/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98/List/practice_02.md#4-%EB%B6%80%EB%B6%84%EC%A7%91%ED%95%A9%EC%9D%98-%ED%95%A9) 문제를 다시 풀어보자

```python
def f1(i, N, K):
    global cnt
    if i == 12:
        s = 0
        c = 0
        for j in range(12):
            if bit[j]:
                s += arr[j]
                c += 1
        if c == N and s == K:
            cnt += 1
    else:
        bit[i] = 1
        f1(i+1, N, K)
        bit[i] = 0
        f1(i+1, N, K)
    return
 
T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(range(1, 13))
    bit = [0] * 12
    cnt = 0
    f1(0, N, K)
 
    print(f'#{tc} {cnt}')
```



#### 순열

> [1,2,3]의 모든 원소 사용한 순열

```pseudocode
f(i, N)
	if i == N
	
	else
		for j:i -> N-1
			P[i] <-> P[j]
			f(i+1, N)
			P[i] <-> P[j]
```

- 구현

```python
def f(i, N):
    if i == N:
        print(p)
    else:
        for j in range(i, N):
            p[i], p[j] = p[j], p[i]
            f(i+1, N)
            p[i], p[j] = p[j], p[i] # 원상복구
    return

p = [1, 2, 3]
N = 3
f(0, N)
```

- 생성 과정

![순열](Stack2.assets/%EC%88%9C%EC%97%B4.jpg)



## 분할정복 알고리즘

- 분할 : 해결할 문제를 여러 개의 작은 부분으로 나눔
- 정복 : 나눈 작은 문제를 각각 해결
- 통합 : 해결된 해답을 모음

C<sup>n</sup> = C * C * C ... * C

```python
def Power(Base, Exponent):
    if Exponent == 0 or Base == 0:
        return 1
    if Exponent % 2 == 0:
        NewBase = Power(Base, Exponent/2)
        return NewBase * NewBase
    else:
        NewBase = Power(Base, (Exponent-1)/2)
        return (NewBase * NewBase) * Base
```



## 퀵 정렬

> 주어진 배열을 두 개로 분할하고, 각각을 정렬

- 시간 복잡도
  - 평균 : O(nlogn)
  - 최악 : O(n<sup>2</sup>)
  - 평균 복잡도가 낮기 때문에 이름이 "퀵"정렬



#### 합병정렬과의 차이점

- 합병정렬은 그냥 두 부분으로 나눔, 퀵정렬은 분할할 때 기준 아이템(pivot) 중심으로 이보다 작은 것은 왼편, 큰 것은 오른편에 위치시킨다
- 각 부분 정렬이 끝난 후 합병정렬은 '합병'이란 후처리 작업이 필요하나, 퀵정렬은 필요하지 않다



#### 수행 과정 예시

- [69, 10, 30, 2, 16, 8, 31, 22] 배열이 있다
- 원소가 8개므로 네 번째에 있는 원소 2를 첫 번째 피봇으로 선택
- L이 오른쪽으로 이동하며 피봇보다 크거나 같은 원소를 찾고, R은 오른쪽으로 이동하면서 피봇보다 작은 원소를 찾는다
- L은 원소 69를 찾았지만 R은 못찾아서 원소를 갖지 못한 채로 원소 69에서 L과 만나게 된다
- L과 R이 만났으므로 원소 69를 피봇과 교환하여 피봇 원소 2의 위치를 확정한다
- [`2` ,10, 30, 69, 16, 8, 31, 22]
- 오른쪽 집합의 원소가 7개이므로 세 번째 원소 16을 피봇으로 선택
- L이 찾은 30과 R이 찾은 8을 서로 교환한다
- [`2`, 10, 8, 69, 16, 30, 31, 22]
- 다시 16을 피봇으로 놓고 반복하여 L은 69를 찾았지만 R은 못찾아 만났으므로 16의 위치를 확정
- [`2`, 10, 8, `16`, 69, 30, 31, 22]
- 왼쪽 부분 집합에서 10을 피봇으로 놓고 퀵 정렬 수행
- L은 8을 찾았고 R은 못찾았으므로 원소8과 10을 교환하여 피봇 원소 10의 위치 확정
- [`2`, 8, `10`, `16`, 69, 30, 31, 22]
- 왼쪽 부분은 원소가 한 개 이므로 정렬을 수행하지 않는다
- 오른쪽 부분에 다시 30을 피봇으로 두고 퀵정렬 수행
- [`2`, 8, `10`, `16`, 22, 30, 31, 69]
- L과 R이 피봇 원소 30에서 만났으므로 그 자리를 확정
- [`2`, 8, `10`, `16`, 22, `30`, 31, 69]
- 확정된 30의 왼쪽은 원소가 한 개이므로 수행하지 않는다
- 31을 피봇으로 두고 퀵 정렬 수행
- [`2`, 8, `10`, `16`, 22, `30`, `31`, 69]
- 더 이상 정렬할 것이 없으므로 퀵정렬 완성



#### 구현

```python
def quickSort(a, begin, end):
    if begin < end:
        p = partition(a, begin, end)
        quickSort(a, begin, p-1)
        quickSort(a, p+1, end)

def partition(a, begin, end):
    pivot = (begin + end) // 2
    L = begin
    R = end
    while L < R:
        while (L<R and a[L]<a[pivot]): L += 1
        while (L<R and a[R]>=a[pivot]): R -= 1
        if L < R:
            if L == pivot:
                pivot = R
            a[L], a[R] = a[R], a[L]
    a[pivot], a[R] = a[R], a[pivot]
    return R

a = [69, 10, 30, 2, 16, 8, 31, 22]
quickSort(a, 0, 7)
print(a)
```

[2, 8, 10, 16, 22, 30, 31, 69]



## 인접행렬 만들기

```python
'''
input이 이런식으로 주어진다면..

7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

(7까지 들어갈 수 있음, 쌍이 8개)
'''

V, E = map(int, input().split()) # V: 7 E: 8
arr = list(map(int, input().split())) # arr: [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
adj = [[0]*(V+1) for _ in range(V+1)] # adj: [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 1, 0], [0, 0, 0, 0, 1, 1, 0, 1], [0, 0, 0, 1, 0, 0, 1, 0]]
adjList = [[] for _ in range(V+1)] # adjList: [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [6, 3]]

for i in range(E): #i: 0~7
    n1, n2 = arr[i*2], arr[i*2+1]
    adj[n1][n2] = 1 # n1과 n2가 인접해있다는 표시
    adj[n2][n1] = 1 # 방향 표시가 없는 경우 반대쪽도 해줘야 함
        
	adjList[n1].append(n2)
    adjList[n2].append(n1)

print()
```

