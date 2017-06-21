length = 0;
while True:
    if (length%2 == 1 and length %3 == 2 and length%5 == 4 and length%6 ==5  and length%7 == 0):
        print("length == ",length)
        break;
    else:
        print("other")
        length += 1


#password :
nums = '1234567890'
chars = 'qwertyuiopasdfghjklzxcvbnm'
#低级密码要求：
#   1. 密码由单纯的数字或字母组成
#   2. 密码长度小于等于8位
password = input("请输入您要验证的密码:")
while (len(password) == 0 or password.isspace()):
    password = input("请重新输入");
    if len(password > 0):
        break;
if len(password) >= 8 :
    print("密码过长")
else:
    checkCount = 0;
    for word in password:
        checkCount += 1
        if (word in nums) or (word in chars):
            if checkCount == len(password) :
                print("密码格式正确")
            continue;
        else:
            print("密码输入格式错误")
            break;
