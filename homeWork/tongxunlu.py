print("|---  欢迎进入通讯录程序 ---|")
print("|---  1:查询联系人资料  ---|")
print("|---  2.插入新的联系人 ---|")
print("|---  3.删除已有联系人 ---|")
print("|---  4.退出通讯录程序 ---|")

code = int(input("请输入相关的代码:"))
txlDic = dict()
while True:
    if code == 1:
        name = str(input("请输入您要查找的姓名:"))
        if name in txlDic:
            phone = str(txlDic[name])
            print("姓名：%s == 联系电话:%s"%(name,phone))
        else:
            print("查无此人")
    elif code == 2:
        name = str(input("请输入您要插入的姓名:"))
        if name in txlDic:
            print(name+"已存在 '-----> %s:%s"%(name,txlDic[name]))
        else:
            phone = str(input("请输入相应的电话号码:"))
            txlDic[name] = phone
    elif code == 3:
        name = str(input("请输入您要删除的姓名:"))
        if name in txlDic:
            txlDic.pop(name)
            if name in txlDic:
                print("删除未成功")
            else:
                print("删除成功")
        else:
            print("该联系人不存在")
    elif code == 4:
        break;
    code = int(input("请输入相关的代码:"))
print("|---  4.感谢您的使用 ---|")

