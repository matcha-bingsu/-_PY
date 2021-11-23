#심사문제: 산 모양으로 별 출력하기

num = int(input())

for i in range(num):
    for j in range(num):
        if j >= num-i-1:
            print('*',end='')
        else:
            print(' ',end='')
    for j in range(num):
        if j < i:
            print('*',end='')
        else:
            print(' ',end='')
    print()
