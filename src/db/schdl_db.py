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
                        sql = f"select concat(First_Name, ' ', Last_Name) as fio from users.employee " \
                              f"where post_id = 1 and id_employee = {label}"
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
                        sql = f"select concat(First_Name, ' ', Last_Name) as fio from users.students " \
                              f"where stud_id = {label}"
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

    def send_data(self, data: dict):
        if data["lesson"] != None and data["teacher"] != None and data["day"] != None and data[
            "student"] != None and data["type_lesson"] != None and data[
            "aud"] != None and data["date_time"] != None:
            sql = f"insert into schdl.schedule (lessons, tchr_id, day, " \
                  f"stud_id, type_lessons, aud_id, time) " \
                  f"values({data['lesson']}, {data['teacher']}, {data['day']}," \
                  f" {data['student']}, {data['type_lesson']}, {data['aud']}, '{data['date_time']}')"

            curr = self.db.cursor()
            curr.execute(sql)
            self.db.commit()

        else:
            raise ValueError

    def code_row(self, data):
        for item in data:
            if item == "lesson":
                label = data[item]
                if label is not None or label != "NULL":
                    sql = f"select ls_id from lessons.lessons where name_lesson = '{label}'"
                    curr = self.db.cursor()
                    curr.execute(sql)
                    tmp_data = curr.fetchone()
                    if tmp_data is None:
                        tmp_data = "NULL"
                    else:
                        data[item] = tmp_data["ls_id"]
                else:
                    data[item] = "NULL"

            if item == "teacher":
                label = data[item]
                if label is not None or label != "NULL":
                    if isinstance(label, str):
                        first_name, last_name = label.split()
                        sql = f"select distinct id_employee from users.employee " \
                              f"where First_Name = '{first_name}' and Last_Name = '{last_name}'"
                        curr = self.db.cursor()
                        curr.execute(sql)
                        tmp_data = curr.fetchone()
                        if tmp_data is None:
                            tmp_data = "NULL"
                        else:

                            data[item] = tmp_data["id_employee"]
                else:
                    data[item] = "NULL"

            if item == "day":
                label = data[item]
                if label is not None or label != "NULL":
                    sql = f"select id_day from days.days where day = '{label}' "
                    curr = self.db.cursor()
                    curr.execute(sql)
                    tmp_data = curr.fetchone()
                    if tmp_data is None:
                        tmp_data = "NULL"
                    else:
                        data[item] = tmp_data["id_day"]
                else:
                    data[item] = "NULL"

            if item == "student":
                label = data[item]
                if label is not None or label != "NULL":
                    if isinstance(label, str):
                        first_name, last_name = label.split()
                        sql = f"select stud_id from users.students where First_Name = '{first_name}' and Last_Name = '{last_name}'"
                        curr = self.db.cursor()
                        curr.execute(sql)
                        tmp_data = curr.fetchone()
                        if tmp_data is None:
                            tmp_data = "NULL"
                        else:
                            data[item] = tmp_data["stud_id"]
                else:
                    data[item] = "NULL"

            if item == "type_lesson":
                label = data[item]
                if label is not None or label != "NULL":
                    sql = f"select tpls_id from lessons.types_lessons where type_lesson = '{label}'"
                    curr = self.db.cursor()
                    curr.execute(sql)
                    tmp_data = curr.fetchone()
                    if tmp_data is None:
                        tmp_data = "NULL"
                    else:
                        data[item] = tmp_data["tpls_id"]

                else:
                    data[item] = "NULL"

            if item == "aud":
                label = data[item]
                if label is not None or label != "NULL":
                    sql = f"select aud_id from auds.auds where aud = '{label}'"
                    curr = self.db.cursor()
                    curr.execute(sql)
                    tmp_data = curr.fetchone()
                    if tmp_data is None:
                        tmp_data = "NULL"
                    else:
                        data[item] = tmp_data["aud_id"]
                else:
                    data[item] = "NULL"

        return data

    def decode_row(self, row_data):
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

        return row_data

    def update_row(self, data, index_row):
        curr = self.db.cursor()
        state = 0
        for item in data:
            if data[item] is not None:
                state += 1

        if state == 7 and index_row != None:
            print("check")

            sql = f"update schdl.schedule " \
                  f"set " \
                  f"lessons = {data['lesson']}," \
                  f"tchr_id = {data['teacher']}," \
                  f"`day`  = {data['day']}," \
                  f" stud_id = {data['student']}," \
                  f"type_lessons = {data['type_lesson']}," \
                  f"aud_id = {data['aud']}," \
                  f"time = '{data['date_time']}'" \
                  f"where sch_id = {index_row}"
            curr.execute(sql)
            self.db.commit()

    def get_from_db_schdl_row(self, index):
        curr = self.db.cursor()
        sql = f"select * from schdl.schedule where sch_id = {index}"
        curr.execute(sql)
        data = curr.fetchone()
        return data
