# practice_11

## 1) 이진수

> 16진수 2진수로 변환(앞자리 0 표시해서)

```python
T = int(input())
for tc in range(1, T+1):
    N, a = input().split()
    s = ''
    for x in a:
        s += bin(int(x, 16))[2:].zfill(4)
    print(f'#{tc} {s}')
```

```python
T = int(input())
for tc in range(1, T+1):
    N, a = input().split()
    s = ''.join([f'{int(x, 16):04b}' for x in a])
    print(f'#{tc} {s}')
```

```python
# 교수님 풀이 - 비트 연산
T = int(input())
for tc in range(1, T+1):
    N, num = input().split()
    s = ''
    for x in num:
        i = int(x,16)
        for j in range(3, -1, -1):
            s += '1' if i & (1<<j) else '0'
    print(f'#{tc} {s}')
```

```python
# 응용
T = int(input())
for tc in range(1, T+1):
    N, a = input().split()
    print(f'#{tc}', end=' ')
    for x in a:
        i = int(x, 16)
        for j in range(4):
            print(1, end='') if i&(8>>j) else print(0, end='')
    print()
```



## 2) 이진수2

> 소수점 아래 12자리 이내인 이진수로 표현(0.뒤에부터 출력)(12자리 넘어가면 overflow)

```python
T = int(input())
for tc in range(1,T+1):
    N = float(input())
    s = ''
    for i in range(1, 13):
        if N:
            if N >= 1/2**i:
                N -= 1/2**i
                s += '1'
            else:
                s += '0'
        else:
            break
    if N:
        res = 'overflow'
    else:
        res = s
    print(f'#{tc} {res}')
```



## 3) [암호코드 스캔](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15JEKKAM8CFAYD)

```python
def trans(s):
    global result
    i = len(s)-1
    code = []
    while i >= 0:
        if s[i] == '1':
            cnt = [0]*3
            while s[i] == '1':
                cnt[2] += 1
                i -= 1
            while s[i] == '0':
                cnt[1] += 1
                i -= 1
            while s[i] == '1':
                cnt[0] += 1
                i -= 1
            x = min(cnt)
            r = cnt[0]//x*100 + cnt[1]//x*10 + cnt[2]//x
            i -= 7*x - sum(cnt)
            code.append(pwd[r])
 
            if len(code) == 8:
                left = code[7]+code[5]+code[3]+code[1]
                right = code[6]+code[4]+code[2]+code[0]
                if not (left*3+right)%10:
                    if code not in result_code:
                        result_code.append(code)
                        result += left+right
                code = []
        else:
            i -= 1
 
pwd = {211:0,
       221:1,
       122:2,
       411:3,
       132:4,
       231:5,
       114:6,
       312:7,
       213:8,
       112:9}
 
T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    nums = list(set(input().strip() for _ in range(N)))
    result_code = []
    result = 0
    for a in nums:
        s = ''
        for x in a:
            s += bin(int(x, 16))[2:].zfill(4)
        s = s.rstrip('0')
        if s:
            trans(s)
    print(f'#{tc} {result}')
```
