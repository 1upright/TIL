# TIL

> Today I Learned. 배운 것을 매일 기록하자.



## 목차

- [Markdown](./Markdown)
- [Git](./Git)
- [원격저장소(Github)](./원격저장소(Github))
- 파이썬
  - [파이썬기초](./파이썬/파이썬기초)
  - [제어문(조건문/반복문)](./파이썬/제어문)
  - [함수](./파이썬/함수)
  - [모듈](./파이썬/모듈)
  - [json](./파이썬/json)
  - [메소드(데이터구조)](./파이썬/메소드)
  - [디버깅(예외처리)](./파이썬/디버깅)



얕은 복사(shallow copy)

```python
original_list = [1, 2, 3]
copy_list = original_list # 같은 통을 바라보게 됨
copy_list = original_list[:] # 복사 가능
copy_list = list(original_list) # 복사 가능

## 하지만
original_list = [1, 2, [0, 1]]
copy_list = original_list[:]

copy_list[2][0] = 'h' # 이러면 (2차원 변경이 생길 경우) original_list도 함께 변경됨 
```



깊은 복사(deep copy)

```python
import copy
a = [1, 2, ['a', 'b']]
b = copy.deepcopy(a)
print(a, b)
b[2][0] = 0
print(a, b)
```

[1, 2, ['a', 'b']] [1, 2, ['a', 'b']]

[1, 2, ['a', 'b']] [1, 2, [0, 'b']]
