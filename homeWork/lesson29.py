
def method1():
    fileName = str('/Users/qikai/Desktop/%s' % (str(input("请输入文件名字:"))))
    print(fileName)
    file = open(fileName, 'w')

    content = input("请输入内容【单独输入'：w'保存退出】:")
    while True:
        if content == ":w":
            print("保存成功")
            file.close()
            break
        else:
            file.write(content + '\n')
            content = input("")

# method1()



#编写一个程序，比较用户输入的两个文件，如果不同，显示出所有不同处的行号与第一个不同字符串的位置
def comparedTwoFile(fileName1,fileName2):
    file1 = open(str("/Users/qikai/Desktop/%s"%str(fileName1)),'r')
    list1 = list(file1.readlines())

    file2 = open(str("/Users/qikai/Desktop/%s"%str(fileName2)),'r')
    list2 = list(file2.readlines())

    for index in range(len(list1)):
        str1 = list1[index]
        str2 = list2[index]
        if str1 != str2:
            for index2 in range(len(str1)):
                if str1[index2] != str2[index2]:
                    print("第%d行 不一样，从第%d个单词开始"%((index+1),(index2+1)))
                    break
            continue;
    file1.close()
    file2.close()
# comparedTwoFile("something.txt","something2.txt")


def printWithHang():
    file = open("/Users/qikai/Desktop/%s"%(str(input("请输入您要打开的文件:"))),'r')
    rangStr = str(input("请输入您要打印的行数【x:y】:"))
    strList = rangStr.split(":",1)
    beginIndex = int(strList[0])-1
    endIndex = int(strList[1])-1
    list1 = list(file.readlines())
    for index in range(beginIndex,endIndex):
        print(list1[index])
    file.close()
# printWithHang()

#实现全部替换的功能
def tihuan():
    fileName = str("/Users/qikai/Desktop/%s" % (str(input("请输入您要打开的文件:"))))
    file = open(fileName, 'r')
    word1 = str(input("请输入被替代的文字:"))
    word2 = str(input("请输入替代的文字:"))
    fileStr = file.read()
    newStr = fileStr.replace(word1,word2)
    file.close()

    file = open(fileName,'w')
    file.write(newStr)
    file.close()

tihuan()
