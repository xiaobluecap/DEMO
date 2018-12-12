def avgNum():
    count = 0
    tatol = 0
    avg = 0

    while True:
        val = yield avg

        count += 1
        tatol = tatol + val
        avg = tatol / count


if __name__ == '__main__':
    avg = avgNum()
    next(avg)
    while True:
        num = input('请输入数字')
        try:
            num = float(num)
        except Exception:
            continue
        number = avg.send(num)

        print(number)
