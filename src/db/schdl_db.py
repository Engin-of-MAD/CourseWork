import pymysql.cursors
from pymysql.cursors import DictCursor

from .db import MyDb


class SchdlDB(MyDb):

    def __init__(self):
        super().__init__()

        self.db = pymysql.connect(database="schdl",
                                  user="root",
                                  host="localhost",
                                  password="qwerty123F!",
                                  cursorclass=DictCursor)

    def get_from_db(self):
        sql = "SELECT * FROM schedule"
        curr = self.db.cursor()
        curr.execute(sql)
        data = curr.fetchall()
        return data

    def send_to_db(self, **kwargs):
        curr = self.db.cursor()
        colums: list = list()
        values: list = list()
        for key in kwargs:
            values.append(kwargs[key])
            colums.append(key)
        col = self._gen_p_col(colums)
        val = self._gen_p_val(values)
        curr.execute(f"INSERT week_schedule({col}) VALUES({val})")
        self.db.commit()

    def check_user_in_db(self, msg: int = None):
        uid = str(msg)

        sql_q = f"SELECT st_tg_id FROM week_schedule WHERE st_tg_id = {uid}"

        curr = self.db.cursor()
        curr.execute(sql_q)
        db = curr.fetchall()
        db = dict(*db)
        state = None

        for key in db:
            if uid == db[key]:
                state = True
            else:
                state = False
        return state

    def decode(self, data):
        for row, row_data in enumerate(data):
            for index, item in enumerate(row_data):

                if item == "lessons":
                    label = row_data[item]
                    if label is None:
                        row_data[item] = "Нет данных"
                    else:
                        sql = f"select name_lesson from lessons.lessons where ls_id = {label}"
                        curr = self.db.cursor()
                        curr.execute(sql)
                        tmp_data = curr.fetchall()
                        # print(tmp_data[0]['name_lesson'])
                        row_data[item] = tmp_data[0]['name_lesson']
                        # print(row_data)

                if item == "day":
                    label = row_data[item]
                    if label is None:
                        row_data[item] = "Нет данных"
                    else:
                        sql = f"select day from days.days where id_day = {label}"
                        curr = self.db.cursor()
                        curr.execute(sql)
                        tmp_data = curr.fetchall()
                        # print(tmp_data)
                        # print(tmp_data[0]["day"])
                        row_data[item] = tmp_data[0]['day']
                        # print(row_data)

                if item == "type_lessons":
                    label = row_data[item]
                    if label is None:
                        row_data[item] = "Нет данных"
                    else:
                        sql = f"select type_lesson from lessons.types_lessons where tpls_id = {label}"
                        curr = self.db.cursor()
                        curr.execute(sql)
                        tmp_data = curr.fetchall()
                        # print(tmp_data)
                        # print(tmp_data[0]['type_lesson'])
                        row_data[item] = tmp_data[0]['type_lesson']
                        # print(row_data)

                if item == "aud_id":
                    label = row_data[item]
                    if label is None:
                        row_data[item] = "Нет данных"
                    else:
                        sql = f"select aud from auds.auds where aud_id = {label}"
                        curr = self.db.cursor()
                        curr.execute(sql)
                        tmp_data = curr.fetchall()
                        # print(tmp_data)
                        row_data[item] = tmp_data[0]['aud']
                        # print(row_data)

                if item == "tchr_id":
                    label = row_data[item]
                    if label is None:
                        row_data[item] = "Нет данных"
                    else:
                        sql = f"select * from posts.post where post_id = {label}"
                        curr = self.db.cursor()
                        curr.execute(sql)
                        tmp_data = curr.fetchall()
                        # print(tmp_data)

                if item == "stud_id":
                    label = row_data[item]
                    if label is None:
                        row_data[item] = "Нет данных"
                    else:
                        sql = f"select * from users.students"
                        curr = self.db.cursor()
                        curr.execute(sql)
                        tmp_data = curr.fetchall()
                        # print(tmp_data)
                        # print(row_data)

                if item == "time":
                    label = row_data[item]
                    if label is None:
                        row_data[item] = "Нет данных"
                        # print(row_data)
        return data
