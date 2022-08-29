import unittest

from parameterized import parameterized

from api.ihrm_user_api import IhrmUserApi
from common.assert_util import assert_util
from common.db_util import DBUtil
from common.get_header import get_header
from common.read_json_util import read_json_data
from config import TEL, BASE_DIR


class TestAddUser(unittest.TestCase):
    path_filename=BASE_DIR + "/data/ihrm_user.json"
    header =None
    @classmethod
    def setUpClass(cls) -> None:
        cls.header=get_header()
    def setUp(self) -> None:
        delete_sql=f"delete from bs_user where mobile = '{TEL}'"
        DBUtil.modify_one(delete_sql)
    def tearDown(self) -> None:
        delete_sql = f"delete from bs_user where mobile = '{TEL}'"
        DBUtil.modify_one(delete_sql)
    @parameterized.expand(read_json_data(path_filename))
    def test01_add_user(self,desc,json_data,status_code,success,code,message):
        resp = IhrmUserApi.add_emp(self.header, json_data)
        print(desc,":", resp.json())
        assert_util(self, resp, 200, True, 10000, "操作成功")

    @parameterized.expand(read_json_data(path_filename))
    def test02_add_user(self,desc,json_data,status_code,success,code,message):
        resp = IhrmUserApi.add_emp(self.header, json_data)
        print(desc,":", resp.json())
        assert_util(self, resp, 200, True, 10000, "操作成功")

    @parameterized.expand(read_json_data(path_filename))
    def test03_add_user(self,desc,json_data,status_code,success,code,message):
        resp = IhrmUserApi.add_emp(self.header, json_data)
        print(desc,":", resp.json())
        assert_util(self, resp, 200, True, 10000, "操作成功")