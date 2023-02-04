# 导入pymysql库
import pymysql

# 建立连接
conn = pymysql.connect(
        host="服务器地址",
        user="用户名",
        password="密码",
        database="数据库名",
        charset="utf8mb4"
    )

# 关闭连接
conn.close()