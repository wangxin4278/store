#类    一个简单的车行图纸
class Car:
    #变量
    num=0#轮胎数量
    color = ""#颜色
    brand = ""#品牌
    #创建功能
    def run(self):
        print(self.brand,"品牌的车在大马路上留来留去","颜色为",self.color)
#创建对象，变量名=类名()
#相当于车钥匙
c = Car()

c.num=4
c.color="蓝色"
c.brand="本田"

#调用
c.run()


#人
'''
姓名，年龄，性别
吃\喝\学习，玩游戏
'''
class People:
    __username = ""
    __age = 0
    __sex = ""
    #封装隐藏__  set用于赋值   get用于取值
    def setUsername(self,username):
        self.__username=username

        #取值
    def getUsername(self,):
        return self.__username

    def setAge(self,age):
        if age >120 or age <0:
            print("年龄错误")
        else:
            self.__age=age

    def eat(self,eatName):
        print(self.__username,"喜欢吃",eatName)

    def drink(self,drinkName):
        print(self.__username,"喜欢喝",drinkName)

    def study(self,hour):
        print(self.__username,"已经学习了",hour,"小时")

    def playGame(self,game):
        print(self.__username,"喜欢玩",game)

    def Agef(self):
        print("我叫",self.__username,"我今年已经",self.__age,"岁了")


c=People()
c.setUsername("阿雷")
#c.username=""
#c.age=16
c.setAge(12)
c.sex="男"
c.eat("鸡排")
c.drink("美年达")
c.study("-9")
c.playGame("王者荣耀")
print(c.getUsername())
c.Agef()

#水杯
'''
高度，容积，颜色，材质
能存放液体
'''
class Cup:
    #高度
    __Heand = 0
    #容积
    __Heands = 0
    #颜色
    __close = ""
    #材质
    __mate = ""
    #赋值
    def setHeand(self,heand):
        if heand <= 0:
            print("水杯太低了")
        else:
            self.__Heand = heand
    #   取值
    def getHeand(self):
        return self.__Heand

    def setHeands(self,heands):
        if heands < 0:
            print("容量不可以是为0")
        else:
            self.__Heands = heands
    def getHeands(self):
        return self.__Heands

    def setClose(self,close):
        self.__close = close
    def getclose(self):
        return self.__close
    def setMate(self,mate):
        if mate == "塑料":
            self.__mate = mate
        elif mate == "玻璃":
            self.__mate = mate
        elif mate == "陶瓷":
            self.__mate = mate
        elif mate == "钢铁":
            self.__mate = mate
        else:
            print("水杯没有这个材料")
    def getmate(self):
        return self.__mate

    def show(self):
        print("这个杯子的高度为",self.__Heand,"容量是",self.__Heands,"ML","颜色是",self.__close,"材质是",self.__mate)

c = Cup()
c.setHeand(100)
c.setHeands(300)
c.setClose("白色")
c.setMate("塑")
c.show()

