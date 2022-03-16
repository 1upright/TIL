# Tree

## 용어 정리

> 상위 원소에서 하위 원소로 내려가면서 확장되는 나무모양의 비선형 구조

- 노드 : 트리의 원소
- 간선 : 노드를 연결하는 선. 부모 노드와 자식 노드를 연결
- 루트 노드 : 트리의 시작 노드(최상위 노드)
- 부모 노드 : 상위 레벨의 노드
- 자식 노드 : 하위 레벨의 노드
- 형제 노드 : 같은 부모 노드의 자식 노드들
- 조상 노드 : 간선을 따라 루트 노드까지 이르는 경로에 있는 모든 노드듣ㄹ
- 서브 트리 : 부모 노드와 연결된 간선을 끊었을 때 생성되는 트리
- 자손 노드 : 서브 트리에 있는 하위 레벨의 노드들
- 차수
  - 노드의 차수 : 노드에 연결된 자식 노드의 수
  - 트리의 차수 : 트리에 있는 노드의 차수 중에서 가장 큰 값
  - 단말 노드 : 차수가 0인 노드
- 높이
  - 노드의 높이 : 루트에서 노드에 이르는 간선의 수. 노드의 레벨
  - 트리의 높이 : 트리에 있는 노드의 높이 중에서 가장 큰 값. 최대 레벨





## 이진 트리

> 모든 노드들이 2개의 서브트리를 갖는 특별한 형태의 트리
>
> 각 노드가 자식 노드를 최대한 2개까지만 가질 수 있는 트리

#### 종류

- 포화 이진 트리 
  - 모든 레벨에 노드가 포화상태로 차 있는 이진 트리
  - 높이가 h일 때, 최대의 노드 개수인 (2<sup>h+1</sup>-1)의 노드를 가진 이진 트리
    - 높이가 3일 때 15개의 노드
  - 루트를 1번으로 하여 2<sup>h+1</sup>-1까지 정해진 위치에 대한 노드 번호를 가짐
- 완전 이진 트리
  - 높이가 h이고 노드 수가 n개일 때(h+1 <= n < 2<sup>h+1</sup>-1), 포화 이진 트리의 노드 번호 1번부터 n번까지 빈 자리가 없는 이진 트리
- 편향 이진 트리
  - 높이 h에 대한 최소 개수의 노드를 가지면서 한쪽 방향의 자식 노드만을 가진 이진 트리.
  - 노드 수 = h+1



#### 순회(traversal)

> 트리의 각 노드를 중복되지 않게 전부 방문하는 것
>
> 트리는 비선형 구조로, 선후 연결 관계를 알 수 없어 특별한 방법이 필요

- 전위순회(preorder) : 부모노드 방문 후, 자식노드를 좌,우 순서로 방문
- 중위순회(inorder) : 왼쪽 자식노드, 부모노드, 오른쪽 자식노드 순으로 방문
- 후위순회(postorder) : 자식노드를 좌,우 순서로 방문한 후, 부모노드 방문
- 구현

```python
def pre_order(v):
    if v:	# 0번 정점이 없으므로... 0번은 자식이 없는 경우를 표시
        print(v)	# visit(v)
        pre_order(ch1[v])
        pre_order(ch2[v])
```

```python
def in_order(v):
    if v:
        pre_order(ch1[v])
        print(v)
        pre_order(ch2[v])
```

```python
def pre_order(v):
    if v:
        pre_order(ch1[v])
        pre_order(ch2[v])
        print(v)
```



#### 표현

- 루트의 번호를 1번으로 하고 레벨 n에 있는 노드에 대하여 왼쪽부터 오른쪽으로 2<sup>n</sup>부터  2<sup>n+1</sup>-1까지 번호를 차례로 부여
  - 노드 번호가 i인 노드의 부모 노드 번호는 i//2가 됨
  - 노드 번호가 i인 노드의 자식 노드 번호는 `2*i`와 `2*i+1`가 됨
  - 레벨 n의 노드 시작번호는 2<sup>n</sup>

![이진트리](Tree.assets/%EC%9D%B4%EC%A7%84%ED%8A%B8%EB%A6%AC.PNG)



#### 파이썬에서의 연습

##### 자식노드들 보여주기

```python
'''
4
1 2 1 3 3 4 3 5
'''
E = int(input())
arr = list(map(int, input().split()))
V = E + 1

ch1 = [0]*(V+1)
ch2 = [0]*(V+1)
for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    if ch1[p] == 0:
        ch1[p] = c
    else:
        ch2[p] = c
print(ch1)
print(ch2)
```

[0, 2, 0, 4, 0, 0]

[0, 3, 0, 5, 0, 0]



##### 자식노드 정보를 이용하여 전위, 중위, 후위 순회 구현

```python
'''
4
1 2 1 3 3 4 3 5
'''
def pre_order(v):
    if v:
        print(v, end=' ')
        pre_order(ch1[v])
        pre_order(ch2[v])

def in_order(v):
    if v:
        in_order(ch1[v])
        print(v, end=' ')
        in_order(ch2[v])

def post_order(v):
    if v:
        post_order(ch1[v])
        post_order(ch2[v])
        print(v, end=' ')

E = int(input())
arr = list(map(int, input().split()))
V = E + 1

ch1 = [0] * (V + 1)
ch2 = [0] * (V + 1)
for i in range(E):
    p, c = arr[i * 2], arr[i * 2 + 1]
    if ch1[p] == 0:
        ch1[p] = c
    else:
        ch2[p] = c

pre_order(1)
print('')
in_order(1)
print('')
post_order(1)
```

1 2 3 4 5

2 1 4 3 5

2 4 5 3 1



#### 완전이진트리

- 순회

```python
# 완전이진트리에서의 순회

def pre_order(v):
    global last
    if v<=last:		# 마지막 정점번호 이내
        print(v)	# visit(v)
        pre_order(v*2)		# 왼쪽 자식정점 방문
        pre_order(v*2+1)	# 오른쪽 자식 정점 방문
```



- 각각의 부모 노드, root, c에 대한 조상 노드 찾기

```python
'''
4
2 1 2 4 4 3 4 5
'''
E = int(input())
arr = list(map(int, input().split()))
V = E + 1

# 각각의 부모 노드 찾기
par = [0]*(V+1)
for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    par[c] = p
print(par)

# root 찾기
root = 0
for i in range(1, V+1):
    if par[i] == 0:		# 부모가 없는 i번 정점이 root
        root = i
print(root)

# 조상 찾기
anc = []	# 조상 목록 저장
c = 5		# 조상을 찾을 정점 번호
while par[c] != 0:		# c가 root가 아니면
    anc.append(par[c])
    c = par[c]			# c의 부모(par[c])를 자식으로
print(*anc)
```

[0, 2, 0, 4, 2, 4]

2

4 2



## 힙

> 완전 이진 트리에 있는 노드 중에서 키값이 가장 큰 노드나 키값이 가장 작은 노드를 찾기 위해서 만든 자료구조

![힙](Tree.assets/%ED%9E%99.PNG)

- 최대 힙 : 키값이 가장 큰 노드를 찾기 위한 완전 이진 트리
- 최소 힙 : 키값이 가장 작은 노드를 찾기 위한 완전 이진 트리



#### 힙 삽입

```python
'''
최대 100개의 자연수가 키로 입력..
최대힙
'''

def enq(n):
    global last
    last += 1
    tree[last] = n  # 완전이진트리 유지
    c = last        # 새로 추가된 정점을 자식으로
    p = c//2        # 완전이진트리에서의 부모 정점 번호
    while p >= 1 and tree[p] < tree[c]:    # 자식의 키값이 더 크면 교환
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c//2

# 포화이진트리의 정점번호 1~100
tree = [0]*101
last = 0        # 마지막 정점 번호
enq(3)
enq(2)
enq(4)
enq(7)
enq(5)
enq(1)
print(tree[1])
```

7



#### 힙 삭제

```python
'''
최대 100개의 자연수가 키로 입력..
최대힙
'''

def enq(n):
    global last
    last += 1
    tree[last] = n  # 완전이진트리 유지
    c = last        # 새로 추가된 정점을 자식으로
    p = c//2        # 완전이진트리에서의 부모 정점 번호
    while p>=1 and tree[p]<tree[c]:    # 자식의 키값이 더 크면 교환
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c//2

def deq():
    global last
    tmp = tree[1] # 루트의 key값
    tree[1] = tree[last]    # 마지막 정점 키를 루트에 복사
    last -= 1               # 마지막 정점 삭제
    # 부모 > 자식 규칙 유지
    p = 1
    c = p * 2       # 왼쪽자식노드 번호
    while c <= last:    # 왼쪽자식이 있으면
        if c+1<=last and tree[c]<tree[c+1]:     # 오른쪽 자식노드도 있고 그게 더 크면
            c += 1      # 오른쪽자식 선택
        if tree[p] < tree[c]:
            tree[p], tree[c] = tree[c], tree[p]
            p = c
            c = p*2
        else:
            break
    return tmp

# 포화이진트리의 정점번호 1~100
tree = [0]*101
last = 0        # 마지막 정점 번호
enq(3)
enq(2)
enq(4)
enq(7)
enq(5)
enq(1)
while last>0:
    print(deq(), tree[1])
```

7 5

5 4

4 3

3 2

2 1

1 1



## practice

#### [중위 순회](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV140YnqAIECFAYD)

```python
def in_order(v):
    if v:
        in_order(ch1[v])
        print(data[v-1][1], end='')
        in_order(ch2[v])
 
for tc in range(1, 11):
    N = int(input())
    data = []
    ch1 = [0] * (N+1)
    ch2 = [0] * (N+1)
    for _ in range(N):
        data.append(list(map(str, input().split())))
    for i in range(N):
        if len(data[i]) >= 3:
            ch1[i+1] = int(data[i][2])
        if len(data[i]) >= 4:
            ch2[i+1] = int(data[i][3])
    print(f'#{tc} ',end='')
    in_order(1)
    if tc != 10:
        print('')
        
# 테케가 전부 완전 이진 트리임
def f(v):
    if v <= N:
        f(v*2)
        print(t[v], end='')
        f(v*2+1)
 
for tc in range(1, 11):
    N = int(input())
    t = [0]*(N+1)
    for i in range(N):
        a = input().split()
        t[int(a[0])] = a[1]
    print(f'#{tc}', end=' ')
    f(1)
    print()
```



#### subtree

> 간선의 개수가 E인 트리에서 N을 루트로 하는 서브 트리에 속한 노드의 개수는?

```python
'''
3
5 1
2 1 2 5 1 6 5 3 6 4 
5 1
2 6 6 4 6 5 4 1 5 3 
10 5
7 6 7 4 6 9 4 11 9 5 11 8 5 3 5 2 8 1 8 10
'''
def pre_order(v):
    global cnt
    if v:
        cnt += 1
        pre_order(ch1[v])
        pre_order(ch2[v])
 
T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    V = E + 1
 
    ch1 = [0] * (V + 1)
    ch2 = [0] * (V + 1)
    for i in range(E):
        p, c = arr[i * 2], arr[i * 2 + 1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c
    cnt = 0
    pre_order(N)
    print(f'#{tc} {cnt}')
```

