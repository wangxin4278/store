#键值对
'''
dict1={"01":"北京","02":"上海","03":"邯郸"}
a=dict1.keys()#获取键
print(a)
'''


'''dict2={"01":{"011":"北京"}
       ,"02":{"022":"上海"}}
print(dict2)
print(dict2.get("01"))
'''


'''name=input("请输入输入数字:")
if name=="01":
       print(dict2["01"])
       name=input("请输入一个数字")
       if name=="001":
              print(dict2["01"]["011"])
'''

dict1={
       "1号线":{
              "东区":{"门牌号1":"01"},
              "南区":{"门牌号2":"02"},
              "西区":{"门牌号3":"03"},
              "北区":{"门牌号4":"04"}
       },
       "2号线":{
              "东区":{"门牌号1":"01"},
              "南区":{"门牌号2":"02"},
              "西区":{"门牌号3":"03"},
              "北区":{"门牌号4":"04"}
       },
       "3号线":{
              "东区":{"门牌号1":"01"},
              "南区":{"门牌号2":"02"},
              "西区":{"门牌号3":"03"},
              "北区":{"门牌号4":"04"}
       },
       "4号线":{
              "东区":{"门牌号1":"01"},
              "南区":{"门牌号2":"02"},
              "西区":{"门牌号3":"03"},
              "北区":{"门牌号4":"04"}
       }
}