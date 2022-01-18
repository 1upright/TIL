# Practice_01



### 1) 갯수 구하기

> 주어진 리스트의 요소는 학생 이름으로 구성되어 있다. 학생들의 수를 출력하시오.

[출력 예시]

3

```python
students = ['김철수', '이영희', '조민지']

# 아래에 코드를 작성하시오.

## 첫 풀이
print(len(students))

## len 사용 없이
i = 0
for student in students:
    i += 1
print(i)
```



### 2) 득표수 구하기

> 주어진 리스트는 반장 선거 투표 결과이다. 이영희의 총 득표수를 출력하시오.

[출력 예시]

4

```python
students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']

# 아래에 코드를 작성하시오.
num = 0
for student in students:
    if student == '이영희':
        num += 1
print(num)
```



### 3) 최댓값 구하기

> 주어진 리스트의 요소 중에서 최댓값을 출력하시오.

[출력 예시]

22

```python
numbers = [7, 10, 22, 4, 3, 17]

# 아래에 코드를 작성하시오.

## 첫 풀이
print(max(numbers))

## max 사용 없이
maxvalue = numbers[0]
for i in numbers:
    if i > maxvalue:
        maxvalue = i

print(maxvalue)

### 다른 방법
maxvalue = numbers[0]
for i in range(1, len(numbers)):
    if maxvalue < numbers[i]:
        maxvalue = numbers [i]
print(maxvalue)
```



### 4) 최솟값 구하기

> 주어진 리스트의 요소 중에서 최솟값을 출력하시오.

[출력 예시]

3

```python
numbers = [7, 10, 22, 4, 3, 17]

# 아래에 코드를 작성하시오.

## 첫 풀이
print(min(numbers))

## min 사용 없이
minvalue = numbers[0]
for i in numbers:
    if i < minvalue:
        minvalue = i
print(minvalue)

### 다른 방법(조건 표현식)
min_num = numbers[0]

for j in numbers :
    min_num = j if j < min_num else min_num

print(min_num)
```



### 5) 최댓값과 등장 횟수 구하기

> 주어진 리스트의 요소 중에서 최댓값과 등장 횟수를 출력하시오.

[출력 예시]

22 3

```python
numbers = [7, 10, 22, 7, 22, 22]

# 아래에 코드를 작성하시오.
maxvalue = numbers[0]
for i in numbers:
    if i > maxvalue:
        maxvalue = i
        
j = 0
for num in numbers:
    if num == maxvalue:
        j += 1
        
print(maxvalue, j)

### 다른 방법
maxi, cnt = float('-inf'), 1
for i in numbers:
    if maxi <= i:
        if maxi == i:
            cnt += 1
        else:
            cnt = 1
        maxi = i
print(maxi, cnt)
```



### 6) 5의 개수 구하기

> 주어진 리스트의 요소 중에서 5의 개수를 출력하시오.

[출력 예시]

3

```python
numbers = [7, 17, 10, 5, 4, 3, 17, 5, 2, 5]

# 아래에 코드를 작성하시오.
i = 0
for num in numbers:
    if num == 5:
        i += 1
print(i)

### 다른 방법
numbers_cnt = [i for i in numbers if i == 5]

print(len(numbers_cnt))

```



### 7) 'a'가 싫어

> 입력으로 짧은 영단어 word가 주어질 때, 해당 단어에서 'a'를 모두 제거한 결과를 출력하시오.

[입력 예시]
apple

[출력 예시]
pple

```python
word = input()

# 아래에 코드를 작성하시오.
for char in word:
    if char == 'a':
        continue
    print(char, end = '')
    
### 다른 풀이1 - 리스트 만들어서 활용하고 문자열로 만들기
word = list(word)
result = []
for i in word:
    if i != 'a':
        result.append(i)
print(''.join(result))

### 다른 풀이2 - 새로운 리스트 만들어서 활용
new_word = list()
for i in word:
    if i != 'a':
        new_word.append(i)
print(*new_word, sep='')

### 다른 풀이3 - a를 공백으로 바꾼다
while 'a' in word:
    word = word.replace('a', '')
print(word)

### 다른 풀이4 - list comprehension
word_remove_a = [alp for alp in word if alp != 'a']
print("".join(word_remove_a))

### 다른 풀이5 - 깔끔
new_word = ''

for alphabet in word:
    if alphabet != 'a':
        new_word += alphabet
        
print(new_word)

### 다른 풀이6 - continue 후 덧붙이기
result = ''

for i_word in word :
    if i_word == 'a' :
        continue
    else :
        result += i_word

print(result)
```



### 8) 단어 뒤집기

> 입력으로 짧은 영어단어 word가 주어질 때, 해당 단어를 역순으로 뒤집은 결과를 출력하시오.

[입력 예시]
apple

[출력 예시]
elppa

```python
word = input()

# 아래에 코드를 작성하시오.

## 첫 풀이
print(word[::-1])

## 슬라이싱 사용 없이
for i in range(len(word)):
    print(word[len(word) - i - 1], end='')
    
### 다른 풀이 - 인덱스 조절
for alpha in range(len(word)):
    print(word[-alpha-1],end="")
    
### 다른 풀이 - 문자열 만들어나가기(거꾸로 채워나가기)
new_word = ''

for alphabet in word:
    new_word = alphabet + new_word
    
print(new_word)
```

