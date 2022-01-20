# Practice_02



### 1)`abs()` 직접 구현하기

> 절댓값은 숫자형 자료(int, float)가 들어오면 절댓값을 반환하고, 복소수형 자료(complex)가 들어오면 해당하는 자료의 크기를 반환합니다.
>
> 파이썬 내장 함수 `abs()`를 직접 구현한 `my_abs()`를 작성하시오.

[출력 예시]

```python
my_abs(3+4j) #=> 5.0
my_abs(-0.0) #=> 0.0
my_abs(-5) #=> 5
```

```python
def my_abs(x):
    if type(x) == int or type(x) == float:
        if x > 0:
            return x
        elif x < 0:
            return -x
        else:
            return x ** 0
    elif type(x) == complex:
        return (x.real**2 + x.imag**2) ** 0.5
    
### 슬라이싱 방법도 있지만 개인적으로 깔끔하진 않은듯..
```



### 2) `all()` 직접 구현하기

> `all()`은 인자로 받는 iterable(range, list)의 모든 요소가 참이거나 비어있으면 True를 반환합니다.
>
> 파이썬 내장 함수 `all()`을 직접 구현한 `my_all()`을 작성하시오.

[출력 예시]

```python
my_all([]) #=> True
my_all([1, 2, 5, '6']) #=> True
my_all([[], 2, 5, '6']) #=> False
```

```python
def my_all(elements):
    result = True
    for i in elements:
        if bool(i) == False:
            result = False
    return result

### 다른 방법 - 수정 전
def my_all(elements):
    is_true = True #4. 이것도 걍 없애고 맨밑에 리턴 트루 시켜
    for element in elements: 
        if element: #3. 여기 if문은 그냥 패슨데 표현식을 부정으로 바꾸면 짧아질듯?
            is_true = True #2. 어차피 is_true = True는 위에 있는데 없애자
        else:
            is_true = False #1.
            break #1. 그냥 return False로 합쳐 
    return is_true

### 다른 방법 - 다 줄이고 보니..
def my_all(elements):
    for element in elements: 
        if not element:
            return False
    return True
```



### 3) `any()` 직접 구현하기

> `any()`는 인자로 받는 iterable(range, list)의 요소 중 하나라도 참이면 True를 반환하고, 비어있으면 False를 반환합니다.
>
> 파이썬 내장 함수 `any()`을 직접 구현한 `my_any()` 함수를 작성하시오.

[출력 예시]

```python
my_any([1, 2, 5, '6']) #=> True
my_any([[], 2, 5, '6']) #=> True
my_any([0]) #=> False
```

```python
# 쓰고 보니 제일 특이한 풀이
def my_any(elements):
    tool = 1
    result = False
    for i in elements:
        tool *= (bool(i) - 1)
        if tool == 0:
            result = True
    return result

### my_all() 만들기 인용
def my_any(elements):
    for element in elements: 
        if element:
            return True
    return False

'''
"if bar == 1:"
== 
"if bar == True:"
==
"if bar:"
임을 잘 이용하자
깔끔한 코드를 완성할 수 있을 것.
'''
```



### 4) 불쌍한 달팽이

> 달팽이는 낮 시간 동안에 기둥을 올라간다. 하지만 밤에는 잠을 자면서 어느 정도의 거리만큼 미끄러진다. (낮 시간 동안 올라간 거리보다는 적게 미끄러진다.)
> 
> 달팽이가 기둥의 꼭대기에 도달하는 날까지 걸리는 시간을 반환하는 함수 `snail()`을 작성하시오.
>
> 함수의 인자는 다음과 같다.
>
> 1. 기둥의 높이(미터)
> 2. 낮 시간 동안 달팽이가 올라가는 거리(미터)
> 3. 달팽이가 야간에 잠을 자는 동안 미끄러지는 거리(미터)

예시) 자연수 number를 입력 받아, 각 자릿수의 합을 계산하여 출력하시오.

```python
snail(100, 5, 2) #=> 33
```

```python
def snail(height, day, night):
    result = 0
    day_count = 0
    while result < height:
        day_count += 1
        result += day
        if result >= height:
            return day_count
        result -= night

### height를 깎는 방법
def snail(height, day, night):
    result = 0
    day_count = 0
    while result < height:
        day_count += 1
        result += day
        if result >= height:
            return day_count
        result -= night
        
### 참신했던 풀이
def snail(height, day, night):
    if day >= height:
        return 1   
    return height // (day-night) # 하지만 예외가 있음. 다듬으면 괜찮을지도?
```



### 5) 자릿수 더하기

> 자연수 number를 입력 받아, 각 자릿수의 합을 계산하여 출력하시오.

예시)

```python
sum_of_digit(1234) #=> 10
sum_of_digit(4321) #=> 10
```

```python
def sum_of_digit(number):
    result = 0
    for i in str(number): #
        result += int(i) #파이썬에서만 통하는 수법일지도?
    return result

### 출제자의 의도(다른 언어에서도 돌아가게 하려면)
def sum_of_digit(number):
    result = 0
    while number:
        result += number % 10
        number = number // 10
    return result
```

