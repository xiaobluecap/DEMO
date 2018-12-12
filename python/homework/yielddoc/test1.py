import time

def simple_gent1():
    print('start')
    x=yield 'running'
    print('end')

def simple_gen():
    print('start')


def listtt():
    for i in range(8):
        print(i)
        yield i



if __name__=='__main__':
    # l = listtt()
    # print(type(l))
    # for i in range(8):
    #     next(l)
    #     time.sleep(3)


    sim=simple_gent1()
    t=next(sim)
    print(t)


