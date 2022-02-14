# List2

## 2차원 배열

#### 선언

```python
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
```



#### 0으로 감싸기

```python
arr = [[0]*(N+2)] + [[0]+list(map(int, input().split))+[0] for _ in range(N)] + [[0]*(N+2)]
```



#### 배열 순회

> nXm 배열의 n*m개의 모든 원소를 빠짐없이 조사하는 방법

```python
# 행 우선 순회
for i in range(n):
    for j in range(m):
        arr[i][j]
        
# 열 우선 순회
for i in range(n):
    for j in range(m):
        arr[j][i]
        
# 지그재그 순회
for i in range(n):
    for j in range(m):
        arr[i][j + (m-1-2*j)*(i%2)]
```



#### 델타를 이용한 2차 배열 탐색

- 예제) NxN 배열에서 각 요소와 이웃한 요소와의 차의 절대값의 합
  - sum(|요소 - 이웃요소|) N*N개의 합
  - 두가지 방법 예시


```python
# 방법 1
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    res = 0
    for i in range(N):
        for j in range(N):
            for di, dj in[(-1,0), (1,0), (0,-1), (0,1)]: # 상, 하, 좌, 우
                ni = i + di
                nj = j + dj
                if 0<=ni<N and 0<=nj<N: # ni, nj가 배열 안에 있다면
                    res += abs(arr[i][j] - arr[ni][nj])
    print(f'#{tc} {res}')
    
# 방법 2
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [-1, 1, 0, 0] # 상, 하, 좌, 우
    dj = [0, 0, -1, 1]

    res = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0<=ni<N and 0<=nj<N:
                    res += abs(arr[i][j] - arr[ni][nj])
    print(f'#{tc} {res}')
```



## 부분집합 생성하기

- `<<` 연산자

  - a<<b : a를 2진수로 바꾼 후 b만큼 왼쪽으로 밀었을 때의 수
  - 예시
    - 1<<n == 2<sup>n</sup> (1<sub>(2)</sub> 를 왼쪽으로 n만큼 밀면 100...<sub>(2)</sub>가 될 것이기 때문)
    - 10<<1 == 10*2 = 20
    - 10>>1 == 10/2 = 5

- `&` 연산자

  - i&(1<<j) : i의 j번째 비트가 1인지 아닌지를 검사
  - 예시

  ```python
  for i in range(5):
      if 21 & (1<<i):
          print(i)
  ```

  0

  2

  4

  (21 == 10101<sub>(2)</sub>이기 때문에 1<sub>(2)</sub>, 100<sub>(2)</sub>,10000<sub>(2)</sub> ... 와 겹친다 => 0, 2, 4가 출력)



- 예제) 10개의 정수를 입력 받아 부분 집합의 합이 0이 되는게 있으면 1, 없으면 0 출력

```python
T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    result = 0
    for i in range(1, 1<<10):
        s = 0
 
        for j in range(10):
            if i & (1<<j):
                s += arr[j]
 
        if s == 0:
            result = 1
 
    print(f'#{tc} {result}')
```



## 검색

#### 순차 검색

> 일렬로 되어 있는 자료를 순서대로 검색

- 정렬되어 있지 않은 경우

```python
def sequential_search(arr, n, key):
    i = 0
    while i < n and arr[i] != key:
        i += 1
    if i < n:
        return i
    else:
        return -1
```

시간 복잡도 : O<sub>(n)</sub>



- 정렬되어 있는 경우(오름차순)

```python
def sequential_search2(arr, n, key):
    i = 0
    while i < n and arr[i] < key:
        i += 1
    if i < n and a[i] == key:
        return i
    else:
        return -1
```

시간 복잡도 : O<sub>(n)</sub>



#### 이진 검색

> 자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행

- 구현

```python
def binary_search(arr, n, key):
    start = 0
    end = N-1
    while start <= end:
        middle = (start+end)//2
        if arr[middle] == key:
            return True
        elif arr[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return False
```

- 재귀함수 이용

```python
def binary_search2(arr, low, high, key):
    if low > high:
        return False
    else:
        middle = (low+high)//2
        if key == arr[middle]:
            return True
        elif key < arr[middle]:
            return binary_search2[arr, low, middle-1, key]
        elif key > arr[middle]:
            return binary_search2[arr, middle+1, low, key]
```



## 인덱스

> 테이블에 대한 동작 속도를 높여주는 자료 구조



#### 선택 정렬

> 주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식

- 시간복잡도 : O<sub>(n)</sub>
- 방법
  1. 주어진 리스트에서 최소값을 찾는다
  2. 리스트의 맨 앞에 위치한 값과 교환
  3. 미정렬 리스트에서 최소값을 찾는다
  4. 리스트의 맨 앞에 위치한 값과 교환
  5. 3, 4 반복

```python
def selection_sort(arr, n):
    for i in range(n-1):
        minidx = i
        for j in range(i+1, n):
            if arr[minidx] > arr[j]:
                minidx = j
        arr[i], arr[minidx] = arr[minidx], arr[i]
    return arr
```
