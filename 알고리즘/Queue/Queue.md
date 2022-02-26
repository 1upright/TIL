# Queue

> 뒤에서는 삽입만 하고, 앞에서는 삭제만 이루어지는 구조



## 연산

- createQueue : 공배 상태의 큐를 생성하는 연산
  - front = rear = -1
- enQueue : 큐의 뒤쪽에 원소를 삽입하는 연산
  - rear += 1, Q[rear]에 원소 삽입
  - append로 구현 가능하지만 속도가 느려짐
- deQueue : 큐의 앞쪽에서 원소를 삭제하고 반환하는 연산
  - front += 1, Q[front] 반환
  - 파이썬에서는 직접 pop하는게 아니고 front만 옮겨가는 느낌으로 구현
  - pop(0)로 구현 가능하지만 속도가 느려짐
- isEmpty() : 큐가 공백상태인지를 확인하는 연산
  - front == rear일 때
- isFull() : 큐가 포화상태인지를 확인하는 연산
  - front == n-1(n : 배열의 크기, n-1 : 배열의 마지막 인덱스)
  - 큐가 끝나지 않았는데 isFull()이 True가 된 경우 발생 =>큐를 너무 작게 설정했거나 코드를 잘못짜서 쓸데없이 많이 집어넣었기 때문 => 큐를 늘리거나 원인을 찾아 코드 수정 필요
- Qpeek() : 큐의 가장 앞에 있는 원소를 검색하여 삭제 없이 반환하는 연산
  - Q[front+1] 반환



#### 연습

> 세 개의 데이터 1, 2, 3을 차례로 큐에 삽입하고 세 개의 데이터를 차례로 꺼내서 출력

```python
front = -1
rear = -1
Q = [0]*10
for i in range(1, 4):
    rear += 1
    Q[rear] = i

for i in range(3):
    front += 1
    print(Q[front])
```



#### 연습문제 - 암호생성기

> 8개의 숫자를 받아 "첫 번째 숫자 1 감소 후 맨 뒤로 ~  다섯 번째 숫자 5 감소 후 맨 뒤로"를 계속 반복하여 맨 뒤 숫자가 0 이하인 경우 그 숫자를 0으로 바꾼 후 출력

```python
def decode(l):
    while 1:
        for i in range(1, 6):
            t = l.pop(0)
            l.append(t-i)
            if l[-1] <= 0:
                l[-1] = 0
                return l

for _ in range(10):
    tc = int(input())
    nums = list(map(int, input().split()))
    print(f'#{tc}', end=' ')
    print(*decode(nums))
```



#### 선형 큐 이용시의 문제점

- 잘못된 포화상태 인식
  - 원소의 삽입과 삭제를 계속할 경우, 배열의 앞부분에 활용될 수 있는 공간이 있음에도 rear = n-1인 상태 즉, 포화상태로 인식하여 더 이상 삽입을 수행하지 않음
  - 해결방법 1 : 매 연산이 이루어질 때마다 저장된 원소들을 배열 앞부분으로 모두 이동?
    - 원소 이동에 많은 시간이 소요되어 효율성이 급격히 떨어짐
  - 해결방법 2 : 1차원 배열을 사용하되, 배열의 처음과 끝이 연결되어 원형 형태의 큐로 사용



## 원형 큐

#### 구조

- front와 rear의 위치가 배열 마지막 인덱스인 n-1을 가리킨 후, 그 다음엔 처음 인덱스인 0으로 이동하도록 함
- 이를 위해 나머지 연산자 mod 사용



#### 구현

```python
# 삽입 연산
def enQueue(item):
    glboal rear
    if isFull(): # 디버깅용
        print('Queue_Full')
    else:
        rear = (rear + 1) % len(cQ)
        cQ[rear] = item
        
# 삭제 연산
def deQueue():
    global front
    if isEmpty():
        print('Queue_Empty')
    else:
        front = (front + 1) % len(cQ)
        return cQ[front]
```



## 우선순위 큐

> 우선순위를 가진 항목들을 저장하는 큐

- FiFO 순서가 아닌 우선순위 높은 순서대로 먼저 나간다
- 적용 분야 : 시뮬레이션 시스템, 네트워크 트래픽 제어, 운영체제 테스크 스케줄링
- 구현 : 원소를 삽입할 때 우선순위를 비교하여 적절한 위치에 삽입하는 구조, 가장 앞에 최고 우선순위 원소가 위치
- 문제점 : 배열을 사용하므로, 삽입/삭제 연산 시 원소의 재배치 발생 => 메모리, 시간 낭비 큼



## 버퍼(Queue의 활용)

> 데이터를 한 곳에서 다른 한 곳으로 전송하는 동안 일시적으로 그 데이터를 보관하는 메모리 영역

- 버퍼링 : 버퍼를 활용하는 방식 또는 버퍼를 채우는 동작
- 자료 구조 : 순서대로 입출력 및 전달되어야 하므로 FIFO 방식의 자료구조인 큐가 활용됨



#### 마이쮸 시뮬레이션

- 1번이 줄서서 한 개의 마이쮸 가져가고 다시 줄을 서고 새로 2번이 다시 줄을 섬
- 1번이 줄서서 두 개의 마이쮸 가져가고 다시 줄을 서고 새로 3번이 다시 줄을 섬
- 2번이 줄서서 한 개의 마이쮸 가져가고 다시 줄을 서고 새로 4번이 다시 줄을 섬
- 1번이 줄서서 세 개의 마이쮸 가져가고 다시 줄을 서고 새로 5번이 다시 줄을 섬
- 계속 진행하면 20개의 마이쮸 중에 마지막 것을 누가 가져갈까?

```python
N = 20
front = -1
rear = -1
Q = [0]*(N*2)
visited = [0]*N # (idx+1)번 사람은 몇 개의 마이쮸를 가져가야하는지
num = 1 # 사람의 번호
tot = 0 # 가져간 마이쮸의 총합

while tot < N:
    rear += 1 # enQueue
    Q[rear] = num # '줄'에 원소 삽입
    visited[num-1] += 1 # 받아갈 마이쮸의 개수

    front += 1 # deQueue
    tot += visited[Q[front]-1] # 마이쮸 가져감

    rear += 1 # enQueue
    Q[rear] = Q[front] # 방금 전 마이쮸 가져간 애가 다시 줄을 섬
    visited[Q[front]-1] += 1 # 받아갈 마이쮸의 개수

    num += 1 # 다음 번호의 등장
print(Q[front])
```

2



```python
# 교수님 방식 1 - N이 커지면 실행시간에 문제 있음
p = 1  # 처음 줄 설 사람 번호
q = []
N = 1000000  # 초기 마이쮸 개수
m = 0   # 나눠준 개수
v = 0

while m<N:
    #input()
    q.append((p, 1, 0))     # 처음 줄 서는 사람
    #print(q)
    v, c, my  = q.pop(0)
    #print(f'큐에 있는 사람 수 {len(q)+1}, 받아갈 사탕 수{c}, 나눠준 사탕 수{m}')
    m += c
    q.append((v, c+1, my+c))    # 마이쮸를 받고 다시 서는 사람
    p += 1                  # 처음 줄서는 사람 번호
print(f'마지막 받은 사람 : {v}')

# 교수님 방식 2 - deque 모듈 이용
from collections import deque
p = 1  # 처음 줄 설 사람 번호
q = deque()
N = 1000000  # 초기 마이쮸 개수
m = 0   # 나눠준 개수
v = 0

while m<N:
    #input()
    q.append((p, 1, 0))     # 처음 줄 서는 사람
    #print(q)
    v, c, my  = q.popleft()
    #print(f'큐에 있는 사람 수 {len(q)+1}, 받아갈 사탕 수{c}, 나눠준 사탕 수{m}')
    m += c
    q.append((v, c+1, my+c))    # 마이쮸를 받고 다시 서는 사람
    p += 1                  # 처음 줄서는 사람 번호
print(f'마지막 받은 사람 : {v}')
```



## BFS

> 탐색 시작점의 인접한 정점들을 먼저 모두 차례대로 방문한 후에, 방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문하는 방식

- 인접한 정점들에 대해 탐색한 후, 차례로 다시 너비우선탐색을 진행해야하므로 선입선출 형태의 자료구조인 큐를 활용



#### 예제

![bfs예제](Queue.assets/bfs%EC%98%88%EC%A0%9C.PNG)

- 한 세트
  - dequeue A
  - visited[A]에 방문 표시
  - A의 인접점 enqueue

1. A에 대해 한 세트 진행(B, C, D enqueue)
2. B에 대해 한 세트 진행(E, F enqueue)
3. C에 대해 한 세트 진행(enqueue X)
4. D에 대해 한 세트 진행(G, H, I enqueue)
5. E, F, G, H, I에 대해 한 세트 진행(enqueue X)

- 구현

```python
def BFS(G, v): # 그래프 G, 탐색 시작점 v
	visited = [0]*(n+1)		# n : 정점의 개수
    Q = []					# 큐 생성
    Q.append(v)				# 시작점 v를 큐에 삽입
    while Q:				# 큐가 비어있지 않은 경우
        t = Q.pop(0)		# 큐의 첫번째 원소 반환
        if not visited[t]:		# 방문되지 않은 곳이라면
            visited[t] = True	# 방문한 것으로 표시
            visit(t)			# 정점 t에서 할일
        for i in G[t]:			# t와 연결된 모든 정점에 대해
            if not visited[i]:	# 방문되지 않은 곳이라면
                Q.append(i)		# 큐에 넣기
```



- 하지만 이미 A의 인접점이라 들어갔던 C가 B의 인접점이기도 하다면??
  - T의 인접 정점에 대해 줄선 적이 없으면 줄 세우고, 줄 섬 표시!

```python
def BFS(G, v, n): # 그래프 G, 탐색 시작점 v
	visited = [0]*(n+1)		# n : 정점의 개수
    Q = []					# 큐 생성
    Q.append(v)				# 시작점 v를 큐에 삽입
    visited[v] = 1
    while Q:				# 큐가 비어있지 않은 경우
        t = Q.pop(0)		# 큐의 첫번째 원소 반환
        for i in G[t]:		# t와 연결된 모든 정점에 대해
            if not visited[i]:	# 방문되지 않은 곳이라면
                    Q.append(i)	# 큐에 넣기
                    visited[i] = visited[t] + 1 # n으로부터 1만큼 이동
```



#### 미로탐색

> [미로 문제](https://github.com/1upright/TIL/blob/master/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98/Stack/practice_06.md#3-%EB%AF%B8%EB%A1%9C) BFS로 다시 풀기

```python
def fstart(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j
    return -1, -1

def bfs(i, j, N):
    visited = [[0]*N for _ in range(N)] # 미로의 크기만큼 생성
    q = []              # 큐 생성
    q.append((i, j))    # 시작점 enqueue
    visited[i][j] = 1   # 시작점 방문표시
    while q:
        i, j = q.pop(0)     # dequeue
        if maze[i][j] == 3: # visit(t)에서 할 일 처리
            return visited[i][j] - 2    # 출발, 도착 칸 제외한 칸 수
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:    # i, j에 인접한 칸에 대해
            ni, nj = i+di, j+dj         # 주변 칸 좌표: 미로를 벗어나지 않고, 인접(벽이 아님)
            if 0<=ni<N and 0<=nj<N and maze[ni][nj]!=1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1 # 그 전에 있던 장소에서 한칸 더 이동했어
    return 0    # 도착지를 찾지 못한 경우


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    sti, stj = fstart(N)
    ans = bfs(sti, stj, N) # 미로의 거리가 나옴(미로의 거리 문제 나오면 ans 출력하면 됨)
    print(f'#{tc} {int(bool(ans))}')
```


