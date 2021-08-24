import pymysql

host="localhost"
user="root"
password="root"
database="company"

# 增、删、改
def update(sql,param):
    con = pymysql.connect(host="localhost", user="root", password="root", database="company")
    cursor = con.cursor()
    cursor.execute(sql, param)
    con.commit()
    cursor.close()
    con.close()

def select(sql,param,mode="all",size=1):
    con = pymysql.connect(host="localhost", user="root", password="root", database="company")
    cursor = con.cursor()
    cursor.execute(sql, param)
    # 提取数据
    if mode == "all":
        return cursor.fetchall()
    elif mode == "one":
        return cursor.fetchone()
    elif mode == "many":
        return cursor.fetchmany(size)
    con.commit()
    cursor.close()
    con.close()











