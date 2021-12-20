# 심사문제: 높은 가격순으로 출력하기

prices = list(map(int,input().split(';')))
prices.sort(reverse = True)
for price in prices:
    print('%9s' % format(price,','))
