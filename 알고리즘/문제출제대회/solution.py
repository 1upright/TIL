def dfs(i, j, flag, s, cnt):
    global res
    if cnt == N+2:
        if res < s:
            res = s
            return

    if i and not flag:
        if j < N-1:
            dfs(i-1, j+1, 1, s+arr[i-1][j+1], cnt+1)
        if j >= 1:
            dfs(i-1, j-1, 1, s+arr[i-1][j-1], cnt+1)

    if i < N-1:
        dfs(i+1, j, flag, s+arr[i+1][j], cnt+1)

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    res = 0
    for j in range(N):
        dfs(0, j, 0, arr[0][j], 1)
    print(f'#{tc} {res}')