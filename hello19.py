import random

print ('숫자를 입력하세요.')
b = input()
b = int(b)

c = random.randint(1, b)
print ('1부터 ' + str(b) + '까지에서 무작위로 선택된 값은 ' + str(c) + '입니다.')
