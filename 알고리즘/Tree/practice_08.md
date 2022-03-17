# practice_08

## 1) 이진탐색

> 노드의 개수가 N인 완전 이진 트리에서 N//2번 노드에 저장된 값은?

```python
def in_order(v):
    global last
    if v<=N:
        in_order(v*2)
        last += 1
        tree[v] = last
        in_order(v*2+1)
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0]*(N+1)
    last = 0
    in_order(1)
    print(f'#{tc} {tree[1]} {tree[N//2]}')
```



## 2) 이진힙

> 입력된 값을 이진 최소힙에 저장하고, 마지막 노드의 조상 노드에 저장된 값들의 합

```python
def enq(n):
    global last
    last += 1
    tree[last] = n
    c = last
    p = c//2
    while p>=1 and tree[p]>tree[c]:
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c//2
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    tree = [0]*(N+1)
    last = 0
    for x in nums:
        enq(x)
    res = 0
    while N > 1:
        N //= 2
        res += tree[N]
    print(f'#{tc} {res}')
```



## 3) 노드의 합

> N == 노드의 개수, M == 리프 노드의 개수, L  == 출력할 값의 노드 번호
>
> 다음 줄부터 x == 리프 노드의 번호, y == x번 노드에 저장될 값

```python
T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0]*(N+1)
    for _ in range(M):
        x, y = map(int, input().split())
        tree[x] = y
    for i in range(N-M, 0, -1):
        tree[i] = tree[i*2]
        if i*2<N:
            tree[i] += tree[i*2+1]
    print(f'#{tc} {tree[L]}')
```





출처 : [SW Expert Academy](https://swexpertacademy.com/main/main.do)