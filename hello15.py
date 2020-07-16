num1 = input('첫 번째 정수를 입력하시오: ')
num2 = input('두 번째 정수를 입력하시오: ')
num1 = int(num1)
num2 = int(num2)

if num1 > num2 :
    print ('큰 수: ', num1)
    print ('작은 수; ', num2)
elif num1 < num2 :
    print ('큰 수: ', num2)
    print ('작은 수: ', num1)
else :
    print ('두 수는 같습니다.')
