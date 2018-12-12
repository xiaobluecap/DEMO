def avg():
    total=0
    counter=0


    while True:
        num=yield
        counter +=1
        total +=num
        avg=total / counter
        print(avg)


test=avg()

test.send(None)

while True:
    num = input('请输入要计算的数字')
    try:
        num = float(num)
    except Exception:
        continue
    if num =='':
        num = input('输入不能为空，请输入要计算的数字')
        num = float(num)

    test.send(num)
