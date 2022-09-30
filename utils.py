def isOk(str1):
    """
    确认执行操作工具
    :param str1: 提示输出的语句
    :return:
    """
    while True:
        print(str1, end="")
        user_change = input("")
        if user_change == "Y":
            return True
        elif user_change == "N":
            return False
        else:
            str1 = "输入错误，请重新输入:"


def isId(s_id):
    if len(s_id) < 20 and s_id.isdigit():
        return True
    else:
        return False


def isName(name):
    """
    判断名字是否正确，名字只能为字母和数字
    :param name: 需要判断的字符串
    :return: True:名字正确，False:名字错误
    """
    for char in list(name):
        if '\u4e00' <= char <= '\u9fff':  # 当前字符为汉字
            pass
        elif char.isalpha():  # 当前字符为字母
            pass
        else:  # 其余情况
            return False
    return True