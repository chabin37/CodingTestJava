num=int(input("거스름돈 액수를 입력하세요: "))
if num==0:
    print("프로그램을 종료합니다")
else:
    m500=num//500#500원갯수
    m100=(num%500)//100#100원갯수
    m50=(num%100)//50#50원갯수
    m10=(num%50)//10
    sum=m500+m100+m50+m10
    print(f"최소 동전 개수: {sum}")
    print(f"각 동전의 개수: 500원({m500}), 100원({m100}), 50원({m50}), 10원({m10})")