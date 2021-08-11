import random
print("===================================")
print("|------中国工商银行账户管理系统---------|")
print("|-------1、开户              -------|")
print("|-------2、存钱              -------|")
print("|-------3、取钱              -------|")
print("|-------4、转账              -------|")
print("|-------5、查询              -------|")
print("|-------6、退出              -------|")
print("====================================")

bank={}#创建一个字典
bank_name="中国工商银行起码路支行"#写死的银行地址
#添加用户
def bank_adduser(account,username,password,country,province,street,door):#参数
    if len(bank)>10:#仓库最多100个账户
        return 3#返回一个相当于ban_adduser=3 返回值3
    elif username in bank:#看看账户在不在bank字典里面
        return 2#返回值2
    bank[username]={
        "account":account,
        #键一个名字:值来自传入的参数:account
        "password":password,
        "country":country,
        "province":province,
        "street":street,
        "door":door,
        "money":0,
        "brnk_name":bank_name # 直接调用全局参数
    }
    return 1

def useradd():
    #输入的参数
    username=input("请输入用户名:")
    password=input("请输入密码:")
    print("请输入您的详细信息")
    country = input("请输入您国家")
    province=input("请输入省份:")
    street=input("请输入街道:")
    door=input("请输入您的门牌号:")
    account=random.randint(10000000,99999999)#随机生成8位账号
    status=bank_adduser(account,username,password,country,province,street,door)
    print(status)#status对应bank_adduser的参数
    if status==3:#如果bank_adduser返回的值return 3就执行下面的代码
        print("对不起，银行用户已满")
    elif status==2:
        print("对不起，用户已开户，不可以重复")
    elif status==1:
        print("恭喜正常开户，以下为您的信息")
        info='''
            ------------个人信息------------
            用户名:%s
            账号：%s
            密码：%s
            国籍：%s
            省份：%s
            街道：%s
            门牌号：%s
            余额：%s
            开户行名称：%s
        '''
        print(info % (username, account,password, country, province, street, door,bank[username]["money"],bank_name))#info % ()对应的是status
#存钱
def bank_money(num_1,password):
    for i in bank.keys():#获取键中的值
        num_1=int(bank[i]["account"])
        print("账号为%d"%num_1)
        if password==int(bank[i]["password"]):
            print("密码为%d"%password)
            return True
        else:
            return False

def addmoney():
    account=input("请输入账号:")
    password=int(input("请输入密码:"))
    status_2=bank_money(account,password)
    if status_2==True:
        for i in bank.keys():
            money = int(input("输入想要存入的钱数:"))
            int(bank[i]["money"])
            bank[i]["money"]=bank[i]["money"]+money
            print("金额剩余%d"%bank[i]["money"])
            break
    else:
        print("账号或密码错误")
#取钱
def moneysadd():
   for i in bank.keys():
       account=input("请输入账号:")
       password=input("请输入密码:")
       if password==bank[i]["password"]:
           moneyss=int(input("请输入取款金额"))
           print("账号为{}\n密码为{}".format(bank[i]["account"],bank[i]["password"]))
           if moneyss>bank[i]["money"]:
               print("输入金额超过存款金额:")
           elif moneyss<=bank[i]["money"]:
               bank[i]["money"]=bank[i]["money"]-moneyss
               print("取款成功现有金额为%d元"%(bank[i]["money"]))
               break
           else:
               print("错误格式")
       elif password !=bank[i]["password"]:
           print("密码错误")
       else:
           print("没有此类用户")

#转账
def zhuanzhang1(account,accounts,password,money):
    if account not in bank:
        return 1
    if password !=password :
        return 2
    if money < money:
        return 3
    if account in bank:
        bank[account]["money"] -= int(money)
        #bank["name"]["money"]
        return 0

def zhuanzhang():
    account = input("请输入转出账号") #"name"
    accounts = input("请输入转入账号")
    password = input("请输入密码")
    money =  input("请输入金额")
    statuss = zhuanzhang1(account,accounts,password,money)
    if statuss == 0:
        print("转账成功")
    if statuss == 1:
        print("账号不存在")
    if statuss == 2:
        print("密码错误")
    if statuss == 3:
        print("余额不足")
        info ='''
        ------------转账信息------------
        转出账号：%s
        转入账号：%s
        转账金额：%s
        '''
        print(info % (account,accounts,money))


#查询功能
def cha_moeny():
    for i in bank.keys():
        account=input("请输入账号:")
        password=input("请输入密码:")
        account=bank[i]["account"]
        if password==bank[i]["password"]:
            print("""
                ----------个人信息------
                用户名：{}
                账号：{}
                密码：{}
                详细地址
                    国家：{}
                余额：{}
                ------------------------
            """.format(i,bank[i]["account"],bank[i]["password"],bank[i]['country'],bank[i]['money']))
            break
        elif password!=bank[i]["password"]:
            print("密码不正确")
        else:
            print("没有该账户")



while True:
    num=input("请输入您要办的业务：")
    if num == "1":
        useradd()
        print(bank)
    elif num == "2":
        addmoney()
        print("存钱")
    elif num == "3":
        moneysadd()
        print("取钱")
    elif num == "4":
        zhuanzhang()
        print("转账")
    elif num == "5":
        cha_moeny()
        print("查询")
    elif num == "6":
        print("再见")
        break
    else:
        print("别瞎搞")
        break
