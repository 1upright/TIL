# Stack

> 물건을 쌓아 올리듯 자료를 쌓아 올린 형태의 자료구조



## 구현

- 자료구조 : 자료를 선형으로 저장할 저장소

  - 배열 사용 가능
  - 마지막 삽입된 원소의 위치를 top

- 연산

  - 삽입 : 저장소에 자료 저장 (push)

  ```python
  def push(item):
      s.append(item)
      
  ## 다른 구현(더 빠른?)
  def push(item, size):
      global top
      top += 1
      if top == size:
          print('overflow!')
      else:
          stack[top] = item
  
  size = 10
  stack = [0]*size
  top = -1
  
  push(10, size)
  top += 1        # push(20)
  stack[top] = 20 #
  ```

  - 삭제 : 저장소에서 자료 꺼냄 - 삽입한 자료의 역순으로 꺼냄(pop)

  ```python
  def pop():
      if len(s) == 0:
          # underflow
          return
      else:
          return s.pop(-1)
  
  ## 자세히
  def pop():
      global top
      if top == -1:
          print('underflow')
          return 0
      else:
          top -= 1
          return stack[top+1]
  print(pop())
  
  if top > -1:
      top -= 1
      print(stack[top+1])
  ```

  - 공백인지 아닌지 확인 (isEmpty)
  - top에 있는 item 반환 (peek)



## 응용

- 연습문제 : 괄호검사

> ()()((())) 과 같이 나와있는 문자 중 괄호의 짝이 맞는지(여는 괄호, 닫는 괄호 모두 있는지) 검사

```python
T = int(input())
for tc in range(1, T+1):
    s = input()

    stack = [0]*1000
    top = -1
    ans = 1
    for x in s:
        if x == '(':
            top += 1 # push
            stack[top] = x
        elif x == ')':
            if top == -1: # 닫는 괄호가 남은 경우
                ans = 0
                break
            else:
                top -= 1
    else:
        if top != -1: # 여는 괄호가 남은 경우
            ans = 0
    print(ans)
```



## 재귀 호출

> 자기 자신을 호출하여 순환 수행되는 것



#### 예시) 피보나치

- 재귀호출 방법

```python
def fibo(n):
    if n < 2:
        return m
    else:
        return fibo(n-1) + fibo(n-2)
```



#### Memoization

> 컴퓨터 프로그램을 실행할 때 이전에 계산한 값을 메모리에 저장해서 매번 다시 계산하지 않도록 하여 전체적인 실행속도를 빠르게 하는 기술

- 앞의 예에서 피보나치수를 구하는 함수는 "엄청난 중복호출이 존재"한다는 단점이 있다
  - fibo(n)의 값을 계산하자마자 저장하면 실행시간을 O<sub>(n)</sub>으로 줄일 수 있다

- 적용 예시

```python
def fibo(n):
    global memo
    if n>=2 and memo[n] == 0:
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

N = 10
memo = [0]*(N+1)
memo[0] = 0
memo[1] = 1
print(fibo(N))
print(memo)
```

55

[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]



- 실제로 n의 크기가 50정도만 넘어가도 보통의 피보나치 수열은 실행시간이 굉장히 오래걸리지만 memoization을 사용하면 n이 1000이 넘어가도 실행이 가능(참고 : 파이썬은 1200쯤에서 재귀를 실행하는데 한계가 있음)



## DP(Dynamic Programming)

> 동적 계획. 그리디 알고리즘과 같이 최적화 문제를 해결하는 알고리즘
>
> 입력 크기가 작은 부분 문제들을 모두 해결한 후에 그 해들을 이용하여 보다 큰 크기의 부분 문제들을 해결하여, 최종적으로 원래 주어진 입력의 문제를 해결하는 알고리즘

1. 문제를 부분 문제로 분할
   - Fibonacci(n) 함수는 Fibonacci(n-1)과 Fibonacci(n-2)의 합
   - Fibonacci(n-1) 함수는 Fibonacci(n-2)과 Fibonacci(n-3)의 합
   - ....
   - Fibonacci(2) 함수는 Fibonacci(1)과 Fibonacci(0)의 합
   - Fibonnaci(n)은 Fibonacci(n-1), Fibonacci(n-2) .... Fibonacci(1), Fibonacci(0)의 부분집합으로 나뉜다
2. 부분 문제로 나누는 일을 끝냈으면 가장 작은 부분 문제부터 해를 구한다
3. 그 결과를 테이블에 저장하고 테이블에 저장된 부분 문제의 해를 이용하여 상위 문제의 해를 구한다

- 적용 예시

```python
N = 10
fibo = [0]*(N+1)
fibo[0] = 0
fibo[1] = 1
for i in range(2, N+1):
    fibo[i] = fibo[i-1] + fibo[i-2]
print(fibo)

### 함수화
def fibo(n):
    f = [0, 1]
    
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
        
    return f[n]
```

- memoization을 재귀적 구조에서 사용하는 것보다 반복적 구조로 DP를 구현한 것이 성능 면에서 보다 효율적이다 => 재귀적 구조는 내부에 시스템 호출 스택을 사용하는 오버헤드가 발생하기 때문
