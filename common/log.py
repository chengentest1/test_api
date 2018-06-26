"""
1. 配置log输出格式 time - loglevel - file - func - line - msg
2. 支持输出到log文件及屏幕
3. 支持返回一个logger,让其他模块调用
"""
import sys
sys.path.append("..")

from common.config import Config, pro_path
import time
import logging
import os


class Log():

    @classmethod
    def config_log(cls):
        cf = Config()
        log_dir = os.path.join(pro_path, cf.get_runtime("log_dir"))
        today = time.strftime("%Y%m%d", time.localtime(time.time()))
        log_file = os.path.join(log_dir, today+".log")

        # 获取一个标准的logger, 配置loglevel
        cls.logger = logging.getLogger()
        cls.logger.setLevel(eval("logging." + cf.get_runtime("log_level").upper()))

        # 建立不同handler
        fh = logging.FileHandler(log_file, mode="a")
        ch = logging.StreamHandler()

        # 定义输出格式
        ft = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
        fh.setFormatter(ft)
        ch.setFormatter(ft)

        # 把定制handler 添加到我们logger
        cls.logger.addHandler(fh)
        cls.logger.addHandler(ch)

    @classmethod
    def get_logger(cls):
        cls.config_log()
        return cls.logger

if __name__ == "__main__":
    l= Log.get_logger()
    l.info("abc")
    l.debug("hello, debug")
 
