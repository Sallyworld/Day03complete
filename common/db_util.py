import pymysql

class DBUtil(object):
    conn = None

    @classmethod
    def __get_conn(cls):
        if cls.conn is None:
            cls.conn = pymysql.connect(host='',port="",user="student",password="iHRM_student_2021", database="test_db", charset="utf8")
            return cls.conn

    @classmethod
    def __close_conn(cls):
        if cls.conn is not None:
            cls.conn.close()
            cls.conn=None

    # 常用方法：查询一条
    @classmethod
    def select_one(cls,sql):
        cursor = None
        res = None
        try:
            cls.conn = cls.__get_conn()
            cursor = cls.conn.cursor()
            cursor.execute(sql)
            res=cursor.fetchone()
        except Exception as err:
            print("查询sql错误：", str(err))
        finally:
            cursor.close()
            cls.__close_conn()
            return res

    # 常用方法：增删改
    @classmethod
    def modify_one(cls,sql):
        cursor = None
        try:
            cls.conn = cls.__get_conn()
            cursor = cls.conn.cursor()
            cursor.execute(sql)
            print("影响的行数：", cls.conn.affected_rows())
            cls.conn.commit()
        except Exception as err:
            cls.conn.rollback()
            print("增删改SQL执行失败：", str(err))
        finally:
            cursor.close()
            cls.__close_conn()


if __name__ =="__main__":
    res = DBUtil.select_one("select * from t_book:")
    print("查询的结果为：", res)

    DBUtil.modify_one("update t_book set is_delete =1 where id = 1111")


