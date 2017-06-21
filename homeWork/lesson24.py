def hanoi(n,x,y,z):
    if n == 1:
        print(x,'--->',z)
    else:
        hanoi(n-1,x,z,y)#将n-1个盘子从x挪到y上面
        print(x,'--->',z)#将x上的挪到z上
        hanoi(n-1,y,x,z)#将y上的n-1个盘子挪到z上
hanoi(int(input("盘数=")),'x','y','z')

