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
                        sql = f"select concat(First_Name, ' ', Last_Name) as fio from users.employee where post_id = 1"
                        curr = self.db.cursor()
                        curr.execute(sql)
                        tmp_data = curr.fetchall()
                        row_data[item] = tmp_data[0]["fio"]
                        # print(row_data)

                if item == "stud_id":
                    label = row_data[item]
                    if label is None:
                        row_data[item] = "Нет данных"
                    else:
                        sql = f"select concat(First_Name, ' ', Last_Name) as fio from users.students"
                        curr = self.db.cursor()
                        curr.execute(sql)
                        tmp_data = curr.fetchall()
                        row_data[item] = tmp_data[0]["fio"]
                        # print(row_data)

                if item == "time":
                    label = row_data[item]
                    if label is None:
                        row_data[item] = "Нет данных"
                        # print(row_data)
        return data

    def send_data_in_schdl(self, data: dict):
        if data["lesson"] != None and data["teacher"] != None and data["day"] != None and data["student"] != None and data["type_lesson"] != None and data["aud"] != None and data["date_time"] != None:
            sql = f"insert into schdl.schedule (lessons, tchr_id, day, " \
                  f"stud_id, type_lessons, aud_id, time) " \
                  f"values({data['lesson']}, {data['teacher']}, {data['day']}," \
                  f" {data['student']}, {data['type_lesson']}, {data['aud']}, '{data['date_time']}')"
            print(data)
            curr = self.db.cursor()
            curr.execute(sql)
            print("check")
        else:
            raise ValueError

    def code_row(self, data):
        for item in data:

            if item == "lesson":
                label = data[item]
                if label is not None:
                    sql = f"select ls_id from lessons.lessons where name_lesson = '{label}'"
                    curr = self.db.cursor()
                    curr.execute(sql)
                    tmp_data = curr.fetchall()
                    data[item] = tmp_data[0]["ls_id"]
                else:
                    data[item] = "NULL"

            if item == "teacher":
                label = data[item]
                if label is not None:
                    first_name, last_name = label.split()
                    sql = f"select distinct id_employee from users.employee where First_Name = '{first_name}' and Last_Name = '{last_name}' "
                    curr = self.db.cursor()
                    curr.execute(sql)
                    tmp_data = curr.fetchall()
                    data[item] = tmp_data[0]["id_employee"]
                else:
                    data[item] = "NULL"

            if item == "day":
                label = data[item]
                if label is not None:
                    sql = f"select id_day from days.days where day = '{label}' "
                    curr = self.db.cursor()
                    curr.execute(sql)
                    tmp_data = curr.fetchall()
                    data[item] = tmp_data[0]["id_day"]
                else:
                    data[item] = "NULL"

            if item == "student":
                label = data[item]
                if label is not None:
                    first_name, last_name = label.split()
                    sql = f"select stud_id from users.students where First_Name = '{first_name}' and Last_Name = '{last_name}'"
                    curr = self.db.cursor()
                    curr.execute(sql)
                    tmp_data = curr.fetchall()

                    data[item] = tmp_data[0]["stud_id"]

                else:
                    data[item] = "NULL"

            if item == "type_lesson":
                label = data[item]
                if label is not None:
                    sql = f"select tpls_id from lessons.types_lessons where type_lesson = '{label}'"
                    curr = self.db.cursor()
                    curr.execute(sql)
                    tmp_data = curr.fetchall()
                    data[item] = tmp_data[0]["tpls_id"]
                else:
                    data[item] = "NULL"

            if item == "aud":
                label = data[item]
                if label is not None:
                    sql = f"select aud_id from auds.auds where aud = '{label}'"
                    curr = self.db.cursor()
                    curr.execute(sql)
                    tmp_data = curr.fetchall()
                    data[item] = tmp_data[0]["aud_id"]
                else:
                    data[item] = "NULL"

        return data
