# practice_05



## 1) 반복문자 지우기

> CAAABBA => CABBA => CAA => C => 1출력

```python
T = int(input())
for tc in range(1, T+1):
    s = input()
 
    stack = []
    top = -1
 
    for x in s:
        if top == -1 or stack[top] != x:
            stack.append(x)
            top += 1
             
        elif stack[top] == x:
            stack.pop()
            top -= 1
 
    print(f'#{tc} {len(stack)}')
```

- stack = [0]*len(s)으로 해놓고 시작해도 된다
- append/pop으로 했을 경우 top이 필요없었을지도? (-1번째로 주면 그게 top이니까)



## 괄호검사

> (), {} 가 제대로 짝을 이루었는지, ({)}와 같이 되진 않았는지 검사

```python
T = int(input())
for tc in range(1, T+1):
    s = input()

    stack = []
    top = -1
    ans = 1
    for x in s:
        if x == '(' or x == '{':
            top += 1
            stack.append(x)

        elif x == ')':
            if top == -1:
                ans = 0
                break
            elif stack[top] == '{':
                ans = 0
                break
            else:
                top -= 1
                stack.pop()

        elif x == '}':
            if top == -1:
                ans = 0
                break
            elif stack[top] == '(':
                ans = 0
                break
            else:
                top -= 1
                stack.pop()

    else:
        if top != -1:
            ans = 0

    print(f'#{tc} {ans}')
    
## 함수로 return해서 끝내는게 하나하나 break 안해도 되고 깔끔하다
def checker(st):
    stack = [0]*len(st)
    top = -1

    for x in st:
        if x == '{' or x == '(':
            top += 1
            stack[top] = x
        elif x ==')' or x=='}':
            if top == -1:
                return 0
            else:
                if x=='}' and stack[top]=='(':
                    return 0
                elif x==')' and stack[top]=='{':
                    return 0
            top -= 1

    if top != -1:
        return 0
    return 1

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc} {checker(input())}')
```



## 종이붙이기

> 10X10, 20X10 종이들이 무수히 많이 있다.
>
> 20XN 직사각형이 있을 때, 종이들을 빈틈없이 붙이는 방법의 수

```python
def paper(n):
    global memo
    if n>=2 and memo[n] == 0:
        memo[n] = paper(n-1) + 2*paper(n-2)
    return memo[n]

memo = [0]*31
memo[1] = 1
memo[2] = 3

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc} {paper(N//10)}')
    
## 홀짝 나눠서 규칙 찾으신 분도 있었다 - 증명은 못하겠음
for i in range(int(input())):
    n = int(input()) // 10
    if n % 2:
        cum = [1]
        for k in range(n//2):
            cum.append(4 * cum[k] + 1)
    else:
        cum = [3]
        for k in range(n//2 - 1):
            cum.append(4 * cum[k] - 1)
    print(f'#{i+1} {cum[-1]}')
```

