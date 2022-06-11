
import random
from apiautotest.src.Utilities.DbUtility import DBUtility

class Pet_DAO:

    def __init__(self):
        self.db_helper=DBUtility()

    def get_pet_by_id(self, pet_id):

        sql = f"select * from Pet where id ='{pet_id}' and is_del = 0;"
        rs_sql = self.db_helper.execute_select(sql)
        return rs_sql

