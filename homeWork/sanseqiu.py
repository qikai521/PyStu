
for red in range(0,4):
    for yellow in range(0,4):
        for green in range(2,7):
            if (red + yellow + green ==8 ):
                print('red :',red,'yellow : ',yellow ,'green',green);


print([i*i for i in range(10)])
str = ("sad\
,asdasd")
print(str)
#三引号字符串不赋值的情况下，通常当作跨行注释使用，#
'''这是一个三引号字符串用于注释的例子，
例子虽然只是简简单单的一句话，
却毫无遮掩地体现了作者用情至深，
所谓爱至深处情至简！'''

# fileName = open(r'/usr/local')

str1 = '<a href="http://www.fishc.com/dvd" target="_blank">鱼C资源打包</a>'
print(str1[16:29])
print(str1[-46:-32])
print(str1[::3]) #以3递进

