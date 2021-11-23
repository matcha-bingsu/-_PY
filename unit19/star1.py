#별의 개수는 세로 방향인 줄의 위치에 비레하므로 조건식도 i에 맞추어 계산

for i in range(5):
    for j in range(5):
        if j <= i:
            print('*', end='')
    print()
