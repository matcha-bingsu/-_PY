# 연습문제: 파일 경로에서 파일명만 가져오기

path = 'C:\\Users\\dojang\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe'
filename = path.split('\\')[-1]
print(filename)