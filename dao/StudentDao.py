from util.DbUtils import implement
from bean.Student import Student


def query_by_name(name):
    """
    按照姓名获取学生信息
    :param name:要查询的学生姓名
    :return:返回两个值，分别为查询到的数据数和查询结果
    """
    if name:
        sql = "select id,name,sex,age,class,zy from student where name=%s"
        return implement(sql, name)
    else:
        return 0, None


def query_by_id(s_id):
    """
    按照姓名获取学生信息
    :param s_id:要查询的学生学号
    :return:返回两个值，分别为查询到的行数和查询结果
    """
    if s_id:
        sql = "select id,name,sex,age,class,zy from student where id=%s"
        return implement(sql, s_id)
    else:
        return 0, None


def query_all():
    """
    查询已添加的所有数据
    :return:
    """
    sql = "select id,name,sex,age,class,zy from student"
    return implement(sql)


def delete(s_id):
    """
    按照学生删除学生信息
    :param s_id: 需要删除的学生id
    :return: 返回两个值，分别为受影响行数和查询结果
    """
    if s_id:
        sql = "delete from student where id=%s;"
        return implement(sql, s_id)
    else:
        return 0, None


def add(stu: Student):
    """
    添加学生到数据库
    :param stu: 需要添加的学生对象
    :return: 执行结果，0为id已存在，其余为执行成功
    """
    if not query_by_id(stu.get_id())[1]:  # 判断学号是否已经存在，不存在则返回添加影响的行数
        sql = "insert into student (id, name, sex, age, class, zy) values (%s,%s,%s,%s,%s,%s);"
        return implement(sql, stu.get_id(), stu.get_name(), stu.get_sex(), stu.get_age(), stu.get_class(), stu.get_zy())
    else:  # 存在返回0
        return 0


def update(stu: Student):
    """
    更新学生数据
    :param stu:更新后的学生数据
    :return:
    """
    sql = "update student set name=%s,sex=%s,age=%s,class=%s,zy=%s where id=%s;"
    return implement(sql, stu.get_name(), stu.get_sex(), stu.get_age(), stu.get_class(), stu.get_zy(), stu.get_id())
