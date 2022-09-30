"""
2、学生管理系统（连接mysql）。
现需要设计一个学生管理系统，首先，需要通过键盘对学生个人信息进行录入，并将学生的个人信息存储到mysql数据库中，
功能：
    同时系统还需要实现查询所有入库的学生信息
    根据姓名查询某个学生的信息
    修改某个学生的信息（其中学号唯一创建后不得修改）
    删除某个学生的信息。
学生的个人信息包含：
    学号（长度最长为20且为数字字符）
    姓名（只得由中英文字符组成不得包含数字及其他字符）
    性别（只能是男女）
    年龄（正整数）
    班级
    专业。
要求：
    （1）要有系统菜单栏选项
    （2）对输入数据需要进行要有合理的提示及限定不符合逻辑的异常处理情况。
    （3）学生信息需要使用面向对象的编程去实现，合理设计学生对象的属性及行为（方法）。
    （4）管理系统中的每一个功能的操作都要与mysql数据库里的数据表同步。
"""
from client import client

if __name__ == '__main__':
    client.client()
