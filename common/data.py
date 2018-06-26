"""
1. 从Excel中读取接口的数据
2. 读取Sql命令
"""
import xlrd
import sys
import os
sys.path.append("..")
from common.config import pro_path


class Data(object):
    def __init__(self, filename):
        data_file_path = os.path.join(pro_path,"data",filename)   
        self.wb = xlrd.open_workbook("../data/test_user_data.xlsx")

    def get_case(self,sheet_name, case_name):
        sh = self.wb.sheet_by_name(sheet_name)
        for i in range(1, sh.nrows):
            if sh.cell(i,0).value == case_name:
                return sh.row_values(i)

        print("用例名未找到")
        return None

    def get_sql(self, sql_name):
        sh = self.wb.sheet_by_name("SQL")
        for i in range(sh.nrows):
            if sh.cell(i,0).value == sql_name:
                return sh.cell(i,1).value
        print("sql未找到")
        return None

if __name__ == "__main__":
    d = Data("test_user_data.xlsx")
    print(d.get_case("reg","test_reg_normal"))
    print(d.get_sql("checkUser"))
