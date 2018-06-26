"""
1. 从配置文件中读取数据库配置
2. 连接数据库
3. 执行sql并返回所有结果
"""
import sys
import pymysql
sys.path.append("..")
from common.config import Config


class DB(object):
    def __init__(self):
        c = Config()
        self.conn = pymysql.connect(host=c.get_db_test("host"),
                                    port=int(c.get_db_test("port")),
                                    db=c.get_db_test("db"),
                                    user=c.get_db_test("user"),
                                    passwd=c.get_db_test("passwd"),
                                    charset="utf8")

        self.cur = self.conn.cursor()

    def do_sql(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchall()

    def __del__(self):
        self.cur.close()
        self.conn.close()


if __name__ == "__main__":
    db = DB()
    print(db.do_sql("select * from user"))
