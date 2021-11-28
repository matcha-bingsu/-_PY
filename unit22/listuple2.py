# 심사문제: 리스트에서 특정 요소만 뽑아내기

a, b = map(int, input().split())
ans = [2 ** i for i in range(a, b + 1) if i != 2 and i != (b - 1)]
print(ans)