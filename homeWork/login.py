users = dict()
def regisUsr():
    uid = str(input("请输入用户名："))
    while True:
        if uid not in users:
            passWord = str(input("请输入密码:"))
            users[uid] = passWord
            print("注册成功")
            break;
        else:
            print("该用户已经存在请重新输入:")
            uid = str(input("请输入用户名："))


def login():
        uid = str(input("请输入用户名:"))
        if uid in users:
            while True:
                inPass = input("请输入密码:")
                if inPass == users[uid]:
                    print("登录成功")
                    break
                else:
                    print("密码错误，请重新登录。")
                    continue
        else:
            print("该用户不存在，请注册")
            regisUsr();

regisUsr()
login()