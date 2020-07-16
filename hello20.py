import random

print ('첫 번째 숫자를 입력하세요.')
a = input()
a = int(a)
print ('두 번째 숫자를 입력하세요.')
b = input()
b = int(b)

c = random.randint(a, b)
print (str(a) + '부터 ' + str(b) + '까지에서 무작위로 선택된 숫자는 ' + str(c) + '입니다.')
