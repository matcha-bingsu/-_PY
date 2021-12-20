# 심사문제: 특정 단어 개수 세기
import string
cnt = 0

para = input().split(' ')
for i in range(0,len(para)):
    para[i] = para[i].strip(string.punctuation)
    if para[i] == 'the':
        cnt += 1
print(cnt)

"""
paragraph = input().split()
count = 0
for words in paragraph:
    if (words.strip(',.')=='the'):
        count += 1
print(count)
"""