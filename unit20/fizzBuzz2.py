#심사문제: 5과 7의 배수,공배수 처리하기

start, stop = map(int,input().split())

for i in range(start, stop+1):
    if i % 5 == 0 and i % 7 == 0:
        print('FizzBuzz')
    elif i % 5 == 0:
        print('Fizz')
    elif i % 7 == 0:
        print('Buzz')
    else:
        print(i)
