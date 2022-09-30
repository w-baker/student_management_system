class Student:
    def __init__(self, s_id: int, name: str, sex: str, age: int, s_class, zy):
        self.__s_id = s_id
        self.__name = name
        self.__sex = sex
        self.__age = age
        self.__s_class = s_class
        self.__zy = zy

    def get_id(self):
        return self.__s_id

    def get_name(self):
        return self.__name

    def get_sex(self):
        return self.__sex

    def get_age(self):
        return self.__age

    def get_class(self):
        return self.__s_class

    def get_zy(self):
        return self.__zy

    def __str__(self):
        return f"[学号：{self.__s_id}，" \
               f"姓名：{self.__name}，" \
               f"性别：{self.__sex}，" \
               f"年龄：{self.__age}，" \
               f"班级：{self.__s_class}，" \
               f"专业：{self.__zy}" \
               f"]"