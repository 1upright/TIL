# Practice_04

## 1) 종합소득세 계산하기

> A라는 나라에서는 종합소득세는 과세표준 금액 구간에 따라 다른 세율이 적용된다.
>
> 즉, 1,300만원을 벌었을 경우 `1,200*0.06 + 100*0.15`를 계산한 결과가 납부해야 하는 세액이다.
>
> 납부해야하는 세금의 결과를 반환하는 함수 `tax()`를 작성하시오.

과세표준액 / 세율

1,200이하 : 6%

1,200 ~ 4,600 : 15%

4,600 ~ : 24%

```python
[예시]
tax(1200) #=> 72.0
tax(4600) #=> 582.0
tax(5000) #=> 678.0
```



```python
def tax(won):
    pass
    if won <= 1200:
        result = won * 0.06
    elif 1200 < won <= 4600:
        result = 72 + (won - 1200) * 0.15
    elif 4600 < won <= 8800:
        result = 582 + (won - 4600) * 0.24
    return result
```



## 2) 카쉐어링 요금 계산하기

> 카쉐어링 서비스는 요금을 다음과 같이 계산한다.
>
> 1. 대여는 10분 단위로 가능하다.
> 2. 대여 요금 : 10분당 1,200원
> 3. 보험료 : 30분당 525원 (50분을 빌리면, 1시간으로 계산)
> 4. 주행 요금 : km당 170원 (주행 요금은 100km가 넘어가면, 넘어간 부분에 대하여 할인이 50% 적용)
>
> 예) 160km를 달렸으면, 170*100 + 85 *60
>
> 양의 정수인 대여시간(분)과 주행거리를 받아 계산 결과를 반환하는 함수 `fee()`를 작성하시오.

참고 함수 [`math.ceil`]

예시)

```python
fee(600, 50) #=> 91000
fee(600, 110) #=> 100350
```

```python
def fee(minute, distance):
    pass
    import math
    borrow = math.ceil(minute / 10) * 1200
    insurance = math.ceil(minute / 30) * 525
    if distance <= 100:
        driving = distance * 170
    else:
        driving = 17000 + (distance - 100) * 85
    money = borrow + insurance + driving
    return money
```



## 3. 문자열 탐색

> 문자열 요소로만 이루어진 리스트를 넣었을 때, 문자열 길이가 2 이상이고 주어진 문자열의 첫번째와 마지막 문자가 같은 문자열의 수를 카운트하는 함수 `start_end()`를 작성하시오.

예시)

```python
start_end(['level', 'asdwe', 's', 'abceda', 'gsdwrtfg']) #=> 3
```



```python
def start_end(words):
    cnt = 0
    for word in words:
        if len(word) >= 2 and word[0] == word[-1]:
            cnt += 1
    return cnt
```



## 4. Collatz 추측

> 1937년 Collatz란 사람에 의해 제기된 이 추측은, 주어진 수가 1이 될때까지 다음 작업을 반복하면, 모든 수를 1로 만들 수 있다는 추측이다. 그 원리는 아래와 같다.
>
> 1. 입력된 수가 짝수라면 2로 나눈다.
>
> 2. 입력된 수가 홀수라면 3을 곱하고 1을 더한다.
>
> 3. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복한다.
>
>    예를 들어, 입력된 수가 6이라면 6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1 이 되어 총 8번 만에 1이 된다.
>
> 위 작업을 몇 번이나 반복해야하는지 반환하는 함수 `collatz()`를 작성하시오 (단, 작업을 500번을 반복해도 1이 되지 않는다면 –1을 반환하시오.)

예시)

```python
collatz(6) #=> 8
collatz(16) #=> 4
collatz(27) #=> 111
collatz(626331) #=> -1
```

```python
def collatz(num):
    count = 0
    if num == 1:
        return 0
    else:
        while num != 1:
            if num % 2:
                num = num * 3 + 1
                count += 1
            else:
                num /= 2
                count += 1
            if count >= 500:
                return -1
        return count
```



## 5. 딕셔너리 뒤집기

>  딕셔너리는 기본적으로 key와 value로 이뤄져있다.
>
> 딕셔너리를 입력받아 value와 key를 뒤집은 결과를 반환하는 함수 `dict_invert()`를 작성하시오.

예시)

```python
dict_invert({1: 10, 2: 20, 3: 30}) #=> {10: [1], 20: [2], 30: [3]}
dict_invert({1: 10, 2: 20, 3: 30, 4: 30}) #=> {10: [1], 20: [2], 30: [3, 4]}
dict_invert({1: True, 2: True, 3: True}) #=> {True: [1, 2, 3]}
```



```python
def dict_invert(my_dict):
    new_dict = {}
    for k,v in my_dict.items():
        if v not in new_dict:
            new_dict[v] = [k]
        else:
            new_dict[v].append(k)
    return new_dict

# 다른 풀이 - 찬영형님꺼
def dict_invert(my_dict):
    result = {}
    for key, value in my_dict.items():
        result[value] = result.get(value, []) + [key]
    return result
```



## 6. Doggy

> 개의 속성과 행위를 정의하는 Doggy 클래스 만들기

1. 초기화 메서드는 인자로 개의 이름과 견종을 받아서 인스턴스 변수에 할당한다.
2. 클래스 변수는 태어난 개의 숫자와 현재 있는 개의 숫자를 기록하는 변수로 구성한다.
   - 개가 태어나면 `num_of_dogs`와 `birth_of_dogs`의 값이 각 1씩 증가한다.
   - 개가 죽으면 `num_of_dogs`의 값이 1 감소한다.
3. 개는 각자의 이름과 나이가 있다.
4. `bark()` 메서드를 호출하면 개는 짖을 수 있다.
5. `get_status()` 메서드를 호출하면 `birth_of_dogs`와 `num_of_dogs`의 수를 출력할 수 있다.



예시)

```python
d1 = Doggy('초코', '푸들')
d2 = Doggy('꽁이', '말티즈')
d3 = Doggy('별이', '시츄')

d1.bark() #=> 왈왈!
d2.bark() #=> 왈왈!
d3.bark() #=> 왈왈!

Doggy.get_status() #=> Birth: 3, Current: 3
```



```python
class Doggy:
    num_of_dogs = 0
    birth_of_dogs = 0
    
    def __init__(self, name, classification):
        self.name = name
        self.classification = classification
        Doggy.num_of_dogs += 1
        Doggy.birth_of_dogs += 1
        self.age = 1

    def __del__(self):
        Doggy.num_of_dogs -= 1
        
    def bark(self):
        print('왈왈!')
    
    def get_status():
        print(f'Birth : {Doggy.birth_of_dogs}, Current: {Doggy.num_of_dogs}')
```

![캡처](Practice_04.assets/%EC%BA%A1%EC%B2%98.PNG)



## 7. Pair Maching Program

> 페어 프로그래밍은 하나의 컴퓨터에서 두 사람의 프로그래머가 작업하는 방식을 의미한다.
>
> SSAFY 1학기 정규 과정에서 프로젝트는 페어 프로그래밍을 통해 진행한다. 진정한 프로그래머가 되기 위해 김싸피는 페어를 매칭하기 위한 프로그램을 작성하려고 한다. 클래스를 활용해 작성하며 포함되는 메서드는 아래와 같다.

**구성 요소**

1. 초기화 메서드는 인자로 학생 이름으로 구성된 리스트를 받아서 인스턴스 변수에 할당한다.
2. `pick(n)` 메서드는 학생들 명단에서 인자 n명 만큼 랜덤으로 추출하여 return한다.
3. `match_pair()` 메서드는 학생들 명단을 랜덤으로 2명씩 매칭해 준다. 이때, 학생들 명단의 수가 홀수명이면 단 한팀만 3명으로 구성한다.



예시)

```python
ch = ClassHelper(['김싸피', '이싸피', '조싸피', '박싸피', '정싸피'])

ch.pick(1) #=> ['이싸피']
ch.pick(1) #=> ['김싸피']
ch.pick(2) #=> ['김싸피', '박싸피']
ch.pick(3) #=> ['김싸피', '조싸피', '정싸피']
ch.pick(4) #=> ['박싸피', '이싸피', '김싸피', '정싸피']

ch.match_pair() #=> [['조싸피', '이싸피'], ['김싸피', '정싸피', '박싸피']]
```



```python
import random

class ClassHelper:
    
    def __init__(self, students):
        self.students = students
        
    def pick(self, n):
        return random.sample(self.students, n)
    
    def match_pair(self):
        students = self.students
        random.shuffle(students)
        result = []
        for i in range(len(students) // 2):
            result.append([students.pop(), students.pop()])
        if students:
            result[-1].append(students.pop())
        return result
    
## 다른 방법
import random
class ClassHelper:
    def __init__(self, name):
        self.name = name
        
    def pick(self, n):
        return print(random.sample(self.name, n))
    
    def match_pair(self):
        match = list()
        name = random.sample(self.name, len(self.name))
        if len(name) % 2 == 0:
            for i in range(0, len(name), 2):
                match.append(name[i:i+2])
        else:
            for i in range(0, len(name)-3, 2):
                match.append(name[i:i+2])
            match.append(name[len(name)-3:])
        return print(match)
```

![캡처2](Practice_04.assets/%EC%BA%A1%EC%B2%982.PNG)



## 8. 도형 만들기

```python
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle(Point):
    
    def __init__(self, point1, point2):
        self.point1_x = point1.x
        self.point1_y = point1.y
        self.point2_x = point2.x
        self.point2_y = point2.y
        
    def get_area(self):
        return abs((self.point1_x - self.point2_x) * (self.point1_y - self.point2_y))
    
    def get_perimeter(self):
        return 2 * (abs(self.point1_x - self.point2_x) + abs(self.point1_y - self.point2_y))
    
    def is_square(self):
        if abs(self.point1_x - self.point2_x) == abs(self.point1_y - self.point2_y):
            return True
        else:
            return False
        
### 다른 방법        
	def __init__(self, point1, point2):
         self.point1 = point1.x, point1.y # 튜플 형태
         self.point2 = point2.x, point2.y

     def get_area(self):
         return abs((self.point1[0] - self.point2[0]) * (self.point1[1] - self.point2[1]))
        
### 교수님의 방법
# 날라감
```

