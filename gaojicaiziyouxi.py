import random
import time
num1 = random.randint(0, 101)
num = 5000
num0=1
while True:
    num2=int(input("请输入数字:"))
    if(num0<=5):
        if (num2 >= num1):
            num0=num0-1
            print('猜对了现有金额为:', num)
        else:
            num0 = num0 + 1
            num = num - 500
            print('猜错了现有金额为:', num)
    else:
        time.sleep(2000)






