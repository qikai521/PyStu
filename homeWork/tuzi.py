def shengtuzi(month):
    lastCount = 0;
    nowCount = 0;
    for index in range(month):
        if index == 0:
            lastCount = 0
            nowCount = 1
        else:
            temp = nowCount
            nowCount = nowCount + lastCount
            lastCount = temp
    print('%d个月之后会产出%d对兔子'%(month,nowCount))
shengtuzi(11)

# 递归的方式实现生兔子

def shengtuzi2(month):
    if month <= 2:
        return 1
    else:
        return shengtuzi2(month -1) + shengtuzi2( month -2)

print(shengtuzi2(11))