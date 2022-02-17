# String

## 컴퓨터에서의 문자

- 네트워크의 종류에 따라 정보를 달리 해석하여 표준안이 필요 => ASCII가 문자 인코딩 표준으로 지정
- 확장 아스키 : 표준 문자 이외의 악센트 문자, 도형 문자, 특수 문자, 특수 기호 등 부가적인 문자 추가 가능
- 미국 뿐 아니라 각 나라에서도 자국의 문자를 표현하기 위해 코드체계 필요 => 유니코드
- 유니코드는 바이트 순서를 표준화하지 못해 파일이 UCS-2, UCS-4인지 인식하여 구현해야 함 => 적당한 외부 인코딩이 필요 => UTF(유니코드 인코딩)
- UTF-8(in web) - MIN: 8bit, MAX: 32bit



## 문자열 처리

#### Python에서..

- char 타입이 없음
- 문자열기호 `''`, `""` 등을 이용
- `+`연결 - 문자열+문자열 : 이어 붙여주는 역할
- `*` 반복 - 문자열*수 : 수만큼 문자열 반복
- 메소드 : replace(), split(), isalpha(), find()
- immutable함



#### 문자열 뒤집기

- str형태의 s에 대하여 s.reverse()가 작동하지 않는다 => list에서만 사용가능
- s = s[::-1]와 같이 써야함
- 리스트로 바꾼 후 뒤집어 join을 써도 됨



#### 문자열 비교

```python
s1 = list(input())
s2 = input()
```

input : 123

output:

['1', '2', '3']

123

```python
s1 = 'abc'
s2 = 'abc'
s3 = 'def'
s4 = s1
s5 = s1[:2] + 'c'
print(s1 == s2)
print(s1 is s2)
print(s5)
print(s1 == s5)
print(s1 is s5)
```

True

True

abc

True

False



#### 문자열 크기 비교(ascii)

> 맨 앞의 문자부터 비교

```python
a = 'abc'
b = 'ab'
c = 'de'
d = 'Abc'

print(a<b)
print(a>b)
print(a<c)
print(a>c)
print(a<d) # 소문자가 더 큼
```

False

True

True

False

False



#### 문자열 숫자를 정수로 변환

- c언어의 `atoi()` : char to int
- 파이썬에서는 `int()`로 가능

```python
def atoi(s):
    i = 0
    for x in s:
        i = i*10 + ord(x) - ord('0') # ord() => 아스키 코드로 변환(반대는 chr())
    return i
```



## 패턴 매칭

#### 고지식한 알고리즘(Brute Force)

```python
P = 'is'
T = 'This is a book~!'
M = len(P)
N = len(T)

def BruteForce(p, t):
    i = 0
    j = 0
    while j < M and i < N:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
    if j == M:
        return i - M
    else:
        return -1

print(BruteForce(P, T))
```



#### KMP 알고리즘

> 불일치가 발생한 텍스트 스트링 앞 부분에 어떤 문자가 있는지를 미리 알고 있으므로, 불일치가 발생한 앞 부분에 대해 다시 비교하지 않고 매칭을 수행

- 시간  복잡도 : O<sub>n</sub>



##### 좀 더 자세히..

> T = 'zzzabcdabcdabcefabcd', P = 'abcdabcef'라고 해보자. 
>
> T속에서 P가 있다면 어디서부터 시작되는지 확인하고 싶다.

- 고지식한 알고리즘 시
  - T안에서 a, b, c, d, a, b, c, e, f 다 확인하고를 맨 처음부터 끝까지 계속 확인해야 함
  - 결국 드는 시간은 len(T)*len(P) 즉, 시간복잡도 : O(MN)이 된다
  - 그렇다면 비교횟수를 줄일 수는 없을까??

- KMP 알고리즘(pythonic한 이해)
  - (P의 길이+1)만큼 lps배열을 만든다 (`lps = [0]*(len(P)+1)`)
  - for i in range(1, len(P))... lps[i]에다 **"문자열 P의 첫번째부터 i번째까지의 문자열 중에서 접두사(prefix) == 접미사(suffix)가 될 수 있는 것 중 그 길이가 최대인 값"**을 집어넣는다
    - 그게 뭔데?
      - 가령 abacaba를 보면 접두사 == 접미사가 되는 것 중 길이가 최대인 것은 aba이므로 그 값은 3이 된다
      - 문자열 P의 첫번째부터 i번째까지의 문자열들을 보자
        - ['a', 'ab', 'abc', 'abcd', 'abcda', 'abcdab', 'abcdabc', 'abcdabce', 'abcdabcef']
      - "그 값"들을 나열해보자
        - [0, 0, 0, 0, 1, 2, 3, 0, 0]
  - lps[0] = -1을 넣어준다(상징적으로 P의 첫문자 a 이전이 lps[0] = -1로 간다고 채워넣은 것 -> 실제로는 파이썬으로 인덱스로 조작을 쉽게 하기 위해 넣은듯?)
    - [-1, 0, 0, 0, 0, 1, 2, 3, 0, 0] == lps(Longest proper prefix which is suffix)
  - **T[i]의 i를 늘려가면서 P[j=0]과 같을 때를 시작점으로 놓고 i와 j를 1씩 늘려가면서 계속 같은지 확인** ······ ①
    - 만약 j가 len(P)만큼 갔는데 계속 똑같다면 P를 찾은 것!
    - 만약 다른 부분을 마주쳤다? 이럴 때를 위해 lps를 준비했다!
      - lps[j]를 확인하여(prefix == suffix가 얼마나 되는지 확인하여) 해당 j를 lps[j]로 바꾼 후(이 때, i의 값은 그대로) 다시 ①로 돌아가 i와 j를 늘려가면서 확인!
  - 위 과정을 반복하다가 P를 찾았을 경우 그 때의 i가 바로 T 속에서 P가 끝나는 지점일 것!
  - 그렇다면 i - len(P)는 패턴이 시작되는 지점일 것
  - 이 방법의 시간 복잡도는 O(M+N)



- 그렇다면 KMP 알고리즘을 파이썬으로 구현하려면?(pseudo code)

```pseudocode
``` 1. lps 만들기 ```

lps = [0] * (len(P) + 1)
j <- 0
lps[0] <- -1

for i : 1 -> len(P)
	lps[i] = j
	if P[i] == P[j] ```만약 P[i]와 P[j]가 같다면 i는 어차피 증가하니까 j도 늘려주면서 그 다음 lps 늘어난 j를 넣어줄거임```
		j <- j+1
	else ```다르면 j는 0으로 초기화```
		j <- 0
		
lps[len(P)] <- j ```다 마치고난 후 마지막 lps에도 j값 넣어줌```

```lps 완성```

``` 2. T안에서 P를 찾아 그 인덱스를 출력 ```
i <- 0
j <- 0
while i<len(T) and j<=len(P)
	if T[i] == P[j] ```같다면 하나씩 늘려가며 확인```
		i <- i+1
		j <- j+1
	if T[i] != P[j] ```다른 부분을 마주쳤다면 j를 lps[j]로 바꿔줌```
		j <- lps[j]
	if j == -1 ```j가 맨 처음이거나 그전 시행에서 lps[j] = 0인 바람에 -1로 초기화 되었다면```
		i <- i+1
		j <- j+1 ```어? T[i] == P[j] 일때랑 똑같네?```
		
	```그러다가 언제든```
	if j == M
		print(i-M) * (나오는만큼)
		j = lps[j] ```계속 이어줘```
```



- 실제로 파이썬으로 구현해보자

```python
def kmp(t, p):
    N = len(t)
    M = len(p)
    lps = [0] * (M + 1)

    j = 0  # 일치한 개수 == 비교할 패턴 위치
    lps[0] = -1
    for i in range(1, M):
        lps[i] = j  # p[i]이전에 일치한 개수
        if p[i] == p[j]:
            j += 1
        else:
            j = 0
    lps[M] = j
    print(lps)

    i = 0 # 비교할 텍스트 위치
    j = 0 # 비교할 패턴 위치
    while i < N and j <= M:
        if j == -1 or t[i] == p[j]: # 첫글자라 불일치했거나, 일치하면
            i += 1
            j += 1
        else: # 불일치
            j = lps[j]
        if j == M: # 패턴을 찾을 경우(cnt개념이었던 j와 p의 길이가 같아짐)
            print(i - M, end = ' ') # 패턴의 인덱스 출력(t의 i-M번 인덱스부터 p가 시작됨)
            j = lps[j]
    print()

t = 'zzzabcdabcdabcefabcd'
p = 'abcdabcef'
kmp(t, p)
t = 'AABAACAADAABAABA'
p = 'AABA'
kmp(t, p)
t = 'AAAAABAAABA'
p = 'AAAA'
kmp(t, p)
```

[-1, 0, 0, 0, 0, 1, 2, 3, 0, 0]
7 
[-1, 0, 1, 0, 1]
0 9 12 
[-1, 0, 1, 2, 3]
0 1 



#### 보이어-무어 알고리즘

- 대부분의 상용 소프트웨어에서 채택하고 있는 알고리즘
- 실제로는 더 복잡하게 구현되는 알고리즘이니 간단하게 알아두기
- P의 오른쪽 끝에 있는 문자가 T안에서의 문자와 불일치하며, 그 T의 문자가 P 내에 존재하지 않는 경우 패턴의 길이만큼 이동하면서 확인
- 시간 복잡도 : O<sub>n</sub>

예시)

![보이어무어](String.assets/%EB%B3%B4%EC%9D%B4%EC%96%B4%EB%AC%B4%EC%96%B4.PNG)

T = a pattern matching algorithm

P = rithm

1. T의 다섯번째 문자인 t와 P의 다섯번째인 m을 비교
2. 불일치하고 rith 중에 t가 겹치므로 2칸 이동
3. e와 m이 불일치하고 rith 중에 e가 없으므로 5칸 이동
4. a와 m이 불일치하고 rith 중에 a가 없으므로 5칸 이동
5. 끝까지 진행



## 연습문제(Brute Force)

#### 연습문제 1) [연속한 1의 개수](https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AXALDUIq97oDFASI)

```python
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    numbers = input()
    cnt = 0
    max_cnt = 0
    for num in numbers:
        if int(num):
            cnt += 1
            if cnt > max_cnt:
                max_cnt = cnt
        else:
            cnt = 0

    print(f'#{tc} {max_cnt}')
```



#### 연습문제 2)[점점 커지는 당근의 개수](https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AW_nY2m6OLADFARY&categoryId=AW_nY2m6OLADFARY&categoryType=CODE)

```python
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    C = list(map(int, input().split()))
    max_cnt = 1
    cnt = 1
    for i in range(1, N):
        if C[i] > C[i-1]:
            cnt += 1
            if cnt > max_cnt:
                max_cnt = cnt
        else:
            cnt = 1
    print(f'#{tc} {max_cnt}')
```



#### 연습문제 3) [고대 유적](https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AXAd8-d6MRoDFARP)

```python
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 0
    for i in range(N):
        cnt = 0
        for j in range(M):
            if arr[i][j]:
                cnt += 1
                if cnt >= max_cnt:
                    max_cnt = cnt
            else:
                cnt = 0

    for j in range(M):
        cnt = 0
        for i in range(N):
            if arr[i][j]:
                cnt += 1
                if cnt >= max_cnt:
                    max_cnt = cnt
            else:
                cnt = 0

    print(f'#{tc} {max_cnt}')
```



## 문자열 암호화

#### 시저 암호

- 키값 n이 있을 때 n만큼 평행 이동시켜 암호화를 행함



## 그외 연습문제

#### [GNS](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14jJh6ACYCFAYD)

```python
alien = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

T = int(input())
for _ in range(T):
    n = list(map(str, input().split()))
    arr = list(map(str, input().split()))
    N = int(n[1])
    cnt = [0]*10
    result = []

    for i in range(N):
        for j in range(10):
            if arr[i] == alien[j]:
                cnt[j] += 1

    for i in range(10):
        for j in range(cnt[i]):
            result.append(alien[i])

    print(n[0])
    print(*result)
```

