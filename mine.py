# 심사문제: 지뢰찾기

matrix = []
cnt = 0

row, col = map(int, input().split())

for i in range(row):
    matrix.append(list(input()))

for i in range(row): #세로
    for j in range(col): #가로 
        cnt = 0
        if matrix[i][j] == '*':
            pass
        else:
            if (i - 1) != -1:
                if matrix[i - 1][j] == '*':
                    cnt += 1
                if (j - 1) != -1 and matrix[i - 1][j - 1] == '*':
                    cnt += 1
                if (j + 1) != col and matrix[i - 1][j + 1] == '*':
                    cnt += 1
            if (j - 1) != -1:
                if matrix[i][j - 1] == '*':
                    cnt += 1
                if (i + 1) != row and matrix[i + 1][j - 1] == '*':
                    cnt += 1
            if (j + 1) != col:
                if matrix[i][j + 1] == '*':
                    cnt += 1
                if (i + 1) != row and matrix[i + 1][j + 1] == '*':
                    cnt += 1
            if (i + 1) != row and matrix[i + 1][j] == '*':
                cnt += 1
            matrix[i][j] = cnt 

for i in range(row): #세로
    for j in range(col): #가로
        print(matrix[i][j], end='')
    print()
        

                

