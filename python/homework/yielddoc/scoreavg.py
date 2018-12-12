data = {
	    'A班': [90, 89, 60, 68],
	    'B班': [90, 13, 43, 13, 53],
	    'C班': [12, 86, 43, 34, 89, 98, 89]
	}



def avg():
    count=0
    tatol=0
    avg=0

    while True:
        val=yield avg
        if not val:
            break
        count +=1
        tatol +=val
        avg=tatol/count
    print(avg)

def pipo():
    while True:
        yield from avg()


def loop():
    av=pipo()
    next(av)


    for k,scores in data.items():
        for score in scores:
            av.send(score)
        av.send(None)




loop()


