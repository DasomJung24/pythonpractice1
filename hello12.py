print ('몸무게와 키를 차례대로 입력하세요.')
weight = float(input())
height = float(input())
BMI = weight / height
if BMI > 25 :
    print ('비만입니다.')
    print ('운동으로 감량이 필요합니다.')
else :
    print ('정상입니다.')
    print ('꾸준한 운동으로 유지시켜 주세요.')
