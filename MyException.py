class IdException(Exception):  # 输入学号异常
    def __init__(self, s_id):
        self.s_id = s_id

    def __str__(self):
        return f"输入学号异常--->{self.s_id}"


class NameException(Exception):  # 姓名异常
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"姓名输入异常--->{self.name}"


class SexException(Exception):  # 性别异常
    def __init__(self, sex):
        self.sex = sex

    def __str__(self):
        return f"输入性别异常--->{self.sex}"