# Practice_03



## 1) 복잡한 리스트의 합

> 2차원 리스트를 반복하는 방법을 알아봅시다.
>
> 주어진 아래의 리스트를 반복하여 숫자의 합을 반환하시오.

```python
# [입력 예시]

numbers = [
    [1, 4],
    [10, 5],
    [20, 30]
]

# [출력 예시]
sum_list([[1, 4], [10, 5], [20, 30]]) # 70
```



#### 1-1) for 문 활용

```python
def sum_list(numbers):
    result = 0
    for num_list in numbers:
        result += sum(num_list)
    return result
```



#### 1-2) index로 접근

```python
def sum_list_index(numbers):
    result = 0
    for i in range(len(numbers)):
        result += sum(numbers[i])
    return result
```



#### 1-3) while문 활용

```python
## 처음 했던 풀이(오답)

# def sum_list_while(numbers):
#     i = 0
#     result = 0
#     while numbers[i]: ## 여기서 리스트의 길이보다 큰 i가 들어가면 index에러 발생!
#         result += sum(numbers[i])
#         i += 1
#     return result

## 수정
def sum_list_while(numbers):
    i = 0
    result = 0
    while i <= len(numbers) - 1:
        result += sum(numbers[i])
        i += 1
    return result

### 다른 풀이 - pop()활용
def sum_list_while(numbers):
    total = 0
    while numbers:
        total += sum(numbers.pop())
    return total
```



## 2) 시험 점수(학생별/과목별 출력)

>2차원 배열
>
>A반 학생들의 점수는 students 리스트와 같다.
>
>- A학생(국어 100점, 수학 80점, 영어 100점)
>- B학생(국어 90점, 수학 90점, 영어 60점)
>- C학생(국어 80점, 수학 80점, 영어 80점)

```python
students = [
 [100, 80, 100],
 [90, 90, 60],
 [80, 80, 80]
]
```



#### 2-1) 학생별 출력

- 리스트를 반복하여 학생별 총합 순서대로 출력
- `sum` 함수 사용 금지

[예시 출력]

280

240

240

```python
## 내풀이
for student in students:
    total_score = 0
    for score in student:
        total_score += score
    print(total_score)

### 다른 풀이 - 의도된 풀이
for i in range(len(students)):
    result = 0
    for j in range(len(students[i])):
        result += students[i][j]
    print(result)
```



#### 2-2) 과목별 출력

- 리스트를 반복하여 과목별 총합을 순서대로 출력
- `sum`함수 사용 금지

[예시 출력]

270

250

240

```python
## 내풀이
korean, math, english = zip(*students)
subjects = (korean, math, english)

for subject in subjects:
    total_score = 0
    for score in subject:
        total_score += score
    print(total_score)
    
### 다른 풀이1 - zip언패킹 더 간단히 쓰는 법
for scores in zip(*students):
    total = 0
    for score in scores:
        total += score
    print(total)
    
### 다른 풀이2 - 의도된 풀이
for i in range(len(students)):
    result = 0
    for j in range(len(students[i])):
        result += students[j][i]
    print(result) # 학생이 한 명 더 있다면 돌아가지 않는 코드(3*3과 같이 정사각형이 X)
```

