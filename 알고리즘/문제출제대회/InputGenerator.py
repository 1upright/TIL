from random import randrange
# eval_input.txt에 T(50)과 미리 sample_input.txt에 포함된 TC들과 코너케이스를 담은 TC들을 포함한 총 10개의 TC들을 넣어 두었다.
f = open('./eval_input.txt', 'a', encoding='utf-8')

# 남은 40개 줄에 랜덤으로 만들어진 TC들을 집어 넣는 코드
for _ in range(40):
    N = randrange(2, 101)
    arr = [[] for _ in range(N)]
    for i in range(N):
        for _ in range(N):
            arr[i].append(str(randrange(0, 10)))

    f.write(f'{N}\n')
    for i in range(N):
        f.write(f'{" ".join(arr[i])}\n')