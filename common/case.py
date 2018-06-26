"""
1. 加载数据
2. 发送接口
3. 为用例封装一些方法

"""
import sys
sys.path.append("..")
from common.log import Log
from common.config import Config
from common.db import DB
from common.data import Data
import json
import requests


class Case(object):
    def __init__(self):
        self.logger = Log.get_logger()
        self.cf = Config()

    def load_data(self, data_file):
        self.data = Data(data_file)

    def set_env(self, env):
        self.env = env

    def run_case(self, sheet_name, case_name):
        case_data = self.data.get_case(sheet_name, case_name)

        url = self.cf.get_server(self.env) + case_data[1]
        data = case_data[4]
    
        
        if case_data[3].lower() == "form":
            data = json.loads(data)
            headers = {}
        else:
            headers = {"content-type": "application/json"}

        if case_data[2].lower() == "get":
            resp = requests.get(url=url)
        else:
            resp = requests.post(url=url, headers=headers, data=data)

        return resp.text

if __name__ == "__main__":
    c = Case()
    c.set_env("test")
    c.load_data("test_user_data.xlsx")
    r = c.run_case("login", "test_login_normal")
    print(r)
    
