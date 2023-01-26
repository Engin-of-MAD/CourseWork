from .db import MyDb

import pymysql.cursors
from pymysql.cursors import DictCursor


class DataListDB:

    def __init__(self):
        super().__init__()
        self.db = pymysql.connect(
            database="posts",
            user="root",
            host="localhost",
            password="qwerty123F!",
            cursorclass=DictCursor
        )

    def get_from_db_teachers(self):
        sql = "select concat(First_Name, ' ' ,Last_Name) as fio from users.employee where post_id = 1"
        curr = self.db.cursor()
        curr.execute(sql)
        data = curr.fetchall()
        data = self.unpack_data(data)
        return data

    def get_from_db_type_lesson(self):
        sql = "select type_lesson from lessons.types_lessons"
        curr = self.db.cursor()
        curr.execute(sql)
        data = curr.fetchall()
        data = self.unpack_data(data)
        return data

    def get_from_db_lesson(self):
        sql = "select name_lesson from lessons.lessons"
        curr = self.db.cursor()
        curr.execute(sql)
        data = curr.fetchall()
        data = self.unpack_data(data)
        return data

    def get_from_db_aud(self):
        sql = "select aud from auds.auds"
        curr = self.db.cursor()
        curr.execute(sql)
        data = curr.fetchall()
        data = self.unpack_data(data)
        return data

    @staticmethod
    def unpack_data(data):
        unpacked_data = []
        for it, items in enumerate(data):
            for item in items:
                unpacked_data.append(items[item])
        return unpacked_data
