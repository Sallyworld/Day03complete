import logging
import unittest

import jsonschema

from api.ihrm_login_api import IhrmLoginApi
from common.assert_util import assert_util

from parameterized import parameterized

from common.read_json_util import read_json_data
from config import BASE_DIR
from common.logging_use import init_log_config


class TestIhrmLogin(unittest.TestCase):
    path_filename=BASE_DIR + "/data/ihrm_login.json"

    @parameterized.expand(read_json_data(path_filename))
    def test01_login_success(self,desc,req_data,status_code,success,code,message):
        resp = IhrmLoginApi.login(req_data)
        print(desc,":",resp.json())
        # assert_util(self, resp, 200, True, 10000, "操作成功")
        schema = {
            "type": "object",
            "properties": {
                "success": {"const": True},
                "code": {"const": 10000},
                "message": {"pattern": "操作成功"},
                "data": {"type": "string"}
            }, "required": ["success", "code", "message", "data"]
        }
        jsonschema.validate(instance=resp.json(), schema=schema)

    @parameterized.expand(read_json_data(path_filename))
    def test02_mobile_none(self,desc,req_data,status_code,success,code,message):
        resp = IhrmLoginApi.login(req_data)
        print(desc,":",resp.json())
        assert_util(self, resp, 200, False, 20001, "用户名或密码错误")

    @parameterized.expand(read_json_data(path_filename))
    def test03_pwd_err(self,desc,req_data,status_code,success,code,message):
        resp = IhrmLoginApi.login(req_data)
        print(desc,":", resp.json())
        assert_util(self, resp, 200, False, 20001, "用户名或密码错误")