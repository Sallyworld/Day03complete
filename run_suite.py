import logging
import unittest
from HTMLTestRunner import HTMLTestRunner
from common.logging_use import init_log_config
from config import BASE_DIR
from scripts.test_ihrm_login import TestIhrmLogin
from scripts.test_ihrm_user import TestAddUser

init_log_config(BASE_DIR + "/log/ihrm.log")
suite=unittest.TestSuite()
logging.info("测试套件实例，创建成功！")
suite.addTest(unittest.makeSuite(TestIhrmLogin))
suite.addTest(unittest.makeSuite(TestAddUser))
runner=HTMLTestRunner("./report/ihrm.html", description="描述",title="标题")
runner.run(suite)
logging.info("ihrm.html 测试报告成功生成！")