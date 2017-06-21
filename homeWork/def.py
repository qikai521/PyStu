def gcd(x,y):
    yueshu = 2
    while True :
       if (x%yueshu == 0 and y%yueshu == 0):
           print("最大公约数是：",yueshu);
           break
       elif (yueshu > min(x,y)):
           print("无最大公约数")
           break



#判断字符串出现在另一个字符串的次数
def getShowCount(str1,str2):
    showCount = 0
    str1Length = len(str1)
    str2Length = len(str2)
    for each in range(str2Length - 1):
        if str1 == str2[each:str1Length+each]:
            showCount += 1
    print("出现了%d次" %showCount)

# str1 = "j"
# str2 = "asjghdfkjghjdkfhkdftriuhasbjfflas"
# str3 = str2[2:6]
# getShowCount(str1,str2)



#判断传入的字符串参数是否为回连
def isHuilian(str):
    strLength = len(str)
    centerIndex = int(strLength//2)
    print(strLength)
    if strLength%2 == 0:
        centerIndex = int(strLength // 2)
        copyStr = str[0:centerIndex]
        print("copyStr = ",copyStr)
        for i in range(0,centerIndex):
            nowChar = str[i];
            print("nowChar = ",nowChar)
            copyStr = copyStr[:centerIndex] + nowChar + copyStr[centerIndex:]
    else:
        centerIndex = int(strLength // 2 +1)
        copyStr = str[0:centerIndex]
        print("copyStr = ",copyStr)
        for i in range(0,centerIndex -1):
            nowChar = str[i];
            print("nowChar = ",nowChar)
            copyStr = copyStr[:centerIndex] + nowChar + copyStr[centerIndex:]
    if copyStr == str:
        print("is回连")
    else :
        print("不是")
# isHuilian("asdaodsa")



# 统计英文字母  空格 数字 其他字符
def logCount(*param):
    length = len(param)
    for i in range(length):
        letters = 0
        space = 0
        digit = 0
        others = 0
        for each in param[i]:
            if each.isalpha():
                letters += 1
            elif each.isdigit():
                digit += 1
            elif each == " ":
                space += 1
            else:
                others +=1
    print("英文数量：%d  ==== 数字: %d  空格 :%d  其他：%d "%(letters ,digit ,space ,others))

# logCount("asdaskhjdh7821eb43uiyiebf ! @ #DF",'213',"fgh","   ")


def funcX():
    x = 5
    def funcY():
        nonlocal x
        x += 1
        return x
    return funcY

a = funcX()
print(a())
print(a())
print(a())

