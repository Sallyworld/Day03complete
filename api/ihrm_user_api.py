import requests

class IhrmUserApi(object):
    @classmethod
    def add_emp(cls, header, json_data):
        url="http://ihrm-test.itheima.net/api/sys/user"
        resp = requests.post(url=url,headers=header,json=json_data)
        return resp

    @classmethod
    def query_emp(cls, header, emp_id):
        url="http://ihrm-test.itheima.net/api/sys/user" + emp_id
        resp = requests.get(url=url,headers=header)
        return resp

    @classmethod
    def modify_emp(cls, header, emp_id, modify_data):
        url="http://ihrm-test.itheima.net/api/sys/user" + emp_id
        resp = requests.put(url=url,headers=header,json=modify_data)
        return resp

    @classmethod
    def delete_emp(cls, header, emp_id):
        url="http://ihrm-test.itheima.net/api/sys/user" + emp_id
        resp = requests.delete(url=url,headers=header)
        return resp

if __name__ =="__main__":
    header={"Content-Type":"application/json", "Authorization": "Bearer b040daed-39c1-4302-8777-f950770c8a26"}
    data_add = {"username":"业务员01","mobile":"13219728798","workNumber":"1111"}
    resp=IhrmUserApi.add_emp(header=header,json_data=data_add)
    print("添加",resp.json())

    emp_id="2383429347"
    resp=IhrmUserApi.query_emp(header,emp_id)
    print("查询",resp.json())

    modify_data="业务员00001"
    resp=IhrmUserApi.modify_emp(header,emp_id,modify_data)
    print("修改",resp.json())

    resp=IhrmUserApi.delete_emp(header,emp_id)
    print("删除", resp.json())