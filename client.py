import StudentService as stuSer

def client():
    while True:
        print("\n**************************信息管理系统**************************\n")
        user_change = input("1.录入学生信息\n"
                            "2.查看所有学生信息\n"
                            "3.查询学生信息\n"
                            "4.修改学生信息\n"
                            "5.删除学生\n"
                            "0.退出\n"
                            "请输入对应序号：")
        if user_change == "1":
            stuSer.add_stu()
        elif user_change == "2":
            stuSer.print_all()
        elif user_change == "3":
            stuSer.query_stu()
        elif user_change == "4":
            stuSer.update_stu()
        elif user_change == "5":
            stuSer.del_stu()
        elif user_change == "0":
            exit(0)
        else:
            print("————————————————————————————")
            print("|     输入错误，请重新输入     |")
            print("————————————————————————————")