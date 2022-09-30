import MyException
import Student
import StudentDao
import utils


def input_stu(s_id=None) -> Student:
    """
    输入学生信息
    :param s_id: 如果传入学生则是修改学生信息，否则为新添加学生
    :return: 返回输入学生的对应学生对象
    """
    while True:
        try:
            if not s_id:  # 判断是修改还是新增操作
                s_id = input("请输入学号(小于20位的整数)：")
                if not utils.isId(s_id):
                    s_id = None
                    raise MyException.IdException(s_id)

            name = input("请输入姓名：")
            if not utils.isName(name):
                raise MyException.NameException(name)

            sex = input("请输入性别(男，女)默认为男：")
            if not sex:
                sex = "男"
            if sex not in ("男", "女"):
                raise MyException.SexException(sex)

            age = input("请输入年龄：")
            if (not age.isdigit()) or int(age) < 0 or int(age) > 120:
                raise MyException.SexException(sex)

            s_class = input("请输入班级：")
            s_zy = input("请输入专业：")

            return Student(int(s_id), name, sex, int(age), s_class, s_zy)
        # 异常处理
        except Exception as e:
            print(f"{e},请重新输入")


def add_stu():
    """
    添加学生模块
    :return:
    """
    while True:
        print("\n**************************添加学生信息**************************\n")
        user_change = input("回车继续，其他退出:")
        if user_change != "":
            return

        stu = input_stu()  # 获取学生信息
        print(stu)

        if utils.isOk("确认添加吗？（Y/N）:"):
            result = StudentDao.add(stu)  # 获取执行结果
            if result:
                print("添加成功！！！")
            else:
                print("该学号已经存在！！！")
        else:
            print("取消执行操作")


def print_all():
    """
    输出所有学生信息
    :return:
    """
    while True:
        print("\n**************************查看所有学生信息**************************\n")
        stus = StudentDao.query_all()[1]
        if stus:  # 如果数据库中有信息，则输出
            user_input = input("输入回车继续，其他退出：")
            if user_input == "":
                print(f"学号\t\t\t姓名\t\t性别\t年龄\t\t班级\t\t\t专业")
                for stu in stus:
                    for data in stu:
                        print(data, end="\t")
                    print("\n")
                print(f"总共{len(stus)}条数据")
            else:  # 退出当前系统
                return
        else:  # 数据库中没有信息
            print("—————————————————————————")
            print("|     当前没有学生信息     |")
            print("—————————————————————————")


def query_stu():
    """
    按照姓名查找学生信息
    :return:
    """
    while True:
        print("\n**************************查找学生信息**************************\n")
        name = input("请输入要查找的学生姓名(回车退出当前页面)：")
        if name == "":
            return
        stus = StudentDao.query_by_name(name)[1]
        if stus:  # 判断是否查询到学生信息
            for stu in stus:
                print(f"学号:{stu[0]}，姓名:{stu[1]}，性别:{stu[2]}，年龄:{stu[3]}，班级:{stu[4]}，专业:{stu[5]}")
        else:
            print("—————————————————————————")
            print("|     没有对应学生信息     |")
            print("—————————————————————————")


def update_stu():
    """
    更新学生信息
    :return:
    """
    while True:
        print("**************************修改学生信息**************************")
        id_input = input("请输入要修改的学生学号(回车退出当前页面)：")

        if id_input == "":
            return

        stu = StudentDao.query_by_id(id_input)[1]

        if stu:  # 如果学生存在则进行选择
            print(stu)
            stu = input_stu(id_input)

            if utils.isOk(f"确认修改为{stu}吗？（Y/N）:"):  # 确认执行操作
                result = StudentDao.update(stu)
                if result[0]:
                    print("修改成功！！！")
                else:
                    print("修改失败！！！")
            else:
                print("取消修改操作")

        else:
            print("—————————————————————————")
            print("|     没有对应学生信息     |")
            print("—————————————————————————")


def del_stu():
    """
    删除学生
    :return:
    """
    while True:
        print("\n**************************删除学生信息**************************\n")
        id_input = input("请输入要删除的学生学号(回车退出当前页面)：")
        if id_input == "":
            return
        stu = StudentDao.query_by_id(id_input)[1]
        if stu:  # 判断是否有对应学号的学生
            print(stu)
            if utils.isOk(f"确定要删除{id_input}吗？(Y/N)"):
                if StudentDao.delete(id_input)[0]:
                    print("删除成功！！！！")
                else:
                    print("删除失败！！！！")
            else:
                print(f"取消删除{id_input}!!!")
        else:
            print("—————————————————————————")
            print("|     没有对应学生信息     |")
            print("—————————————————————————")