from abc import ABC, abstractmethod


class MyDb:
    db = None

    async def send_to_db(self, **kwargs):
        pass

    def get_from_db(self):
        pass

    async def check_user_in_db(self):
        pass

    @staticmethod
    def check_null(lst):
        if len(lst) == 0:
            return False
        else:
            return True

    @staticmethod
    def _gen_p_col(p: list):
        s = str()
        for i in p:
            s = s + i + ", "
        s = s[:-2]
        return s

    @staticmethod
    def _gen_p_val(p: list):
        s = ""
        for i in p:
            if isinstance(i, str):
                s = s + f"\"{i}\"" + ", "
            else:
                s = s + f"{i}" + ", "
        s = s[:-2]
        return s

    @staticmethod
    def __convert_data(tup: tuple):
        tup = list(tup)
        uid = []
        for i in tup:
            uid.append(*i)
        return uid

    @staticmethod
    def unpack_data(data):
        unpacked_data = []
        for it, items in enumerate(data):
            for item in items:
                unpacked_data.append(items[item])
        return unpacked_data
