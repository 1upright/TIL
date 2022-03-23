# start

## 비트 연산

- `&` : 비트단위로 AND 연산
- `|` : 비트단위로 OR연산
- `^` : 비트단위로 XOR 연산
- `~` : 단항 연산자로서 피연산자의 모든 비트를 반전
- `<<` : 피연산자의 비트 열을 왼쪽으로 이동
- `>>` : 피연산자의 비트 열을 오른쪽으로 이동

```python
def Bbit_print(i):
    output = ''
    for j in range(7, -1, -1):
        output += '1' if i&(1<<j) else '0'
    print(output)
        
for i in range(-3, 4):
    print('%3d = ' % i, end='')
    Bbit_print(i)
```

 -3 = 11111101
 -2 = 11111110
 -1 = 11111111
  0 = 00000000
  1 = 00000001
  2 = 00000010
  3 = 00000011

```python
a &= ~(1<<3|1<<5)
# 오른쪽 값 == 3번 비트가 1인 값과 5번 비트가 1인 값의 리버스 == 3번, 5번 비트만 0인 값
# a의 b3, b5를 클리어해라
```



#### 엔디안

> 컴퓨터 메모리와 같은 1차원 공간에 여러 개의 연속된 대상을 배열하는 방법

- 빅 엔디안 : 보통 큰 단위가 앞에 나옴
- 리틀 엔디안 : 작은 단위가 앞에 나옴
- 엔디안 바꾸기

```python
def ce(n):
    p = []
    for i in range(0, 4):
        p.append((n >> (24 - i*8)) & 0xff)
```

```python
def ce1(n):
	return (n << 24 & 0xff000000) | (n << 8 & 0xff0000) | (n >> 8 & 0xff00) | (n >> 24 & 0xff)
```

- 0xff : 비트 연산의 마스킹 - 둘씩 끊어서 ff면 채워지고 00이면 비워진다



#### 연습문제 1

> 0과 1로 이루어진 1차 배열에서 7개 byte를 묶어 10진수로 출력

- input

0000000111100000011000000111100110000110000111100111100111111001100111

```python
num = input()
N = len(num)
for i in range(N//7):
    print(int(num[i*7:i*7+7], 2), end=' ')
```

```python
arr = list(map(int, input()))
n = 6
dec = 0
for x in arr:
    dec += x*(2**n)
    n -= 1
    if n==-1:
        n = 6
        print(dec, end=' ')
        dec = 0
```



#### 연습문제 2

> 16진수 문자 => 2진수 문자 => 7bit씩 묶어 10진수로 출력

```python
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = input()
    print(f'#{tc}', end=' ')
    s = ''
    for i in range(N):
        s += f'{int(a[i],16):04b}' # 네자리씩 넣기(이 코드의 핵심)
    for i in range(N*4//7):
        print(int(s[i*7:i*7+7], 2), end=' ')
    print()
```

```python
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    h = input()
    s = ''
    for n in h:
        s += str(bin(int(n,16))[2:].zfill(4)) # 네자리씩 넣기 2
 
    print(f'#{tc}', end=' ')
    for i in range(len(s)//7):
        print(int(int(s[i*7:(i+1)*7],2)), end=' ')
    print()
```



## 실수

> 실수 표현을 위해 부동 소수점(floating-point) 표기법 사용

#### 실수의 표현

- 가수부 : 실수의 유효 자릿수들을 부호화된 고정 소수점으로 표현한 것
- 지수부 : 실제 소수점의 위치를 지수 승으로 표현한 것
- 단정도 실수의 가수 부분
  - 정수부의 첫번째 자리가 1이 되도록 오른쪽으로 시프트
  - 소수점 이하를 23비트로 만든다
  - 소수점 이하만을 가수 부분에 저장
  - 지수 부분은 시프트 한 자릿수 만큼 증가 또는 감소
- 단정도 실수의 지수 부분
  - 지수부에는 8비트가 배정
  - 숫자로는 0-255까지 나타낼 수 있지만 음수 값을 나타내기 위해 excess 표현법 사용
    - 지수부의 값을 반으로 나누어 그 값을 0으로 간주하고 음수지수와 양수지수를 표현하는 방법
- 컴퓨터는 실수를 근사적으로 표현한다



#### struct

> 생략

```python
import struct

a = 0x0102030a
b = struct.pack('I', a)
c, = struct.unpack('I', b)
print(b)
print(f'{c:032b}')

a = 9.187500
bits, = struct.unpack('I', struct.pack('f', a))
print(f'{bits:032b}')
```



#### 연습문제 3

> 16진수 문자로 이루어진 1차 배열에서 암호비트패턴을 찾아 차례대로 출력, 암호는 연속되어 있음

```python
code = [13, 19, 59, 49, 35, 55, 11, 61, 25, 47]
code = ['001101','010011','111011','110001','100011','110111','001011','111101','011001','101111']
a = '0DEC'
a = '0269FAC9A0'
s = ''
for x in a:
    s += bin(int(x, 16))[2:].zfill(4)
i = 1
while i <= len(s)-6:
    tar = s[i:i+6]
    if tar in code:
        print(code.index(tar))
        i += 6
    else:
        i += 1
```



#### 연습문제 4 - [단순 2진 암호 코드](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15FZuqAL4CFAYD)

```python
# 풀이 1
dic = {
        '0001101': '0',
        '0011001': '1',
        '0010011': '2',
        '0111101': '3',
        '0100011': '4',
        '0110001': '5',
        '0101111': '6',
        '0111011': '7',
        '0110111': '8',
        '0001011': '9'
    }

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    for _ in range(N):
        a = input()
        if a != '0'*M:
            s = a
    s = list(s)

    while 1:
        if s[0] == '0':
            s.pop(0)
        else:
            break
    s.reverse()
    while 1:
        if s[0] == '0':
            s.pop(0)
        else:
            break
    for _ in range(7-len(s)%7):
        s.append('0')
    s.reverse()

    ss = ''
    for x in s:
        ss += x

    res = 0
    tot = 0
    for i in range(len(ss)//7):
        x = dic[ss[i*7:i*7+7]]
        if i % 2:
            res += int(x)
        else:
            res += int(x)*3
        tot += int(x)

    if res%10:
        ans = 0
    else:
        ans = tot

    print(f'#{tc} {ans}')
    
# 풀이 2
dic = {
        '0001101': '0',
        '0011001': '1',
        '0010011': '2',
        '0111101': '3',
        '0100011': '4',
        '0110001': '5',
        '0101111': '6',
        '0111011': '7',
        '0110111': '8',
        '0001011': '9'
    }

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    s = ''
    for _ in range(N):
        a = input()
        if not s:
            if a != '0'*M:
                s = a
    for i in range(M):
        if s[i] == '1':
            start = i
            break
    for i in range(M-1, -1, -1):
        if s[i] == '1':
            end = i
            break
    start -= 6-(end-start)%7

    res = 0
    tot = 0
    for i in range((end-start+1)//7):
        x = dic[s[i*7+start:i*7+7+start]]
        if i % 2:
            res += int(x)
        else:
            res += int(x)*3
        tot += int(x)

    if res % 10:
        ans = 0
    else:
        ans = tot

    print(f'#{tc} {ans}')
```

