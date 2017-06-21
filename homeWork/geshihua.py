print("{{1}}".format("不打印", "打印"))
print("{a} love {b}.{c}".format(a="I", b="FishC", c="com"))

# 进制转换
# num = input("请输入一个需要转换的十进制数字")
q = True
while q:
    num = input('请输入一个整数(输入Q结束程序)：')
    if num != 'Q':
        num = int(num)
        print('十进制 -> 十六进制 : %d -> 0x%x' % (num, num))
        print('十进制 -> 八进制 : %d -> 0o%o' % (num, 23))
        print('十进制 -> 二进制 : %d -> a' % num, bin(num))
    else:
        q = False
