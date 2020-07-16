print ('단을 입력하세요 (1~9)')
dan = input()
dan = int(dan)

num = 1

while num <= 9 :
    print ( dan , '*',  num , '=' , dan*num )
    num = num + 1
