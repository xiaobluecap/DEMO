


def avg():
    count=0
    total=0
    avg=0


    while True:
        val=yield avg
        count +=1
        total +=val
        avg=total/count
        print(avg)



def pipo():

    yield from avg()


def loop():
    pip=pipo()
    next(pip)
    while True:
        num=input('请输入数字')
        try:
            num=float(num)
        except Exception:
            continue
        if num == '':
            num = input('输入不能为空，请输入要计算的数字')
            num = float(num)

        pip.send(num)


loop()