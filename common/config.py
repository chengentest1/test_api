"""
1. 从配置文件中获取各个段信息
2. 返回一个项目的绝对路径
"""
import os
import configparser
# 相对导入包的问题
pro_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
class Config(object):
    def __init__(self, filename="default.conf"):
        self.cf = configparser.ConfigParser()
        self.cf.read(os.path.join(pro_path,"conf",filename))
        
    def get_runtime(self, option):
        return self.cf.get("runtime", option)

    def get_server(self, option):
        return self.cf.get("server", option)

    def get_db_test(self, option):
        return self.cf.get("db_test", option)

    def get_email(self, option):
        return self.cf.get("email",option)
if __name__ == "__main__":
    c = Config()
    print(c.get_runtime("log_level"))
    #print(c.get_server("test"))
