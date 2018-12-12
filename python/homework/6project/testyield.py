numint = list()

strList = list()


def fun_isdigit(num):
    try:
        return float(num)
    except ValueError:
        return False


def isStr(string):
    try:
        return string.isspace()
    except ValueError:
        return False


def testYield():
    while True:
        val = yield

        number = fun_isdigit(val)

        if number is False:
            oneder = isStr(val)
            if oneder is True:
                raise Exception
            else:
                strList.append(val)
        else:
            numint.append(val)


if __name__ == '__main__':
    t = testYield()
    next(t)
    try:
        while True:
            value = input('请输入数字或字符串')
            t.send(value)
    except Exception:
        print('这是数字列表{}'.format(numint))
        print('这是字符串列表{}'.format(strList))
