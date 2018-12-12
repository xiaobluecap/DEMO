from collections import namedtuple
import random,queue




event=namedtuple('evevt','taix_time,taix_id,event')

def taix_event(taix_time=0):
    time=yield event(taix_time,1,'leave home')
    for i in range(7):
        time = yield event(time, 1, 'pick people')
        time = yield event(time, 1, 'drop people')

    yield event(time, 1, 'go home')








def run_event():
    t1=taix_event()
    t, id, e =next(t1)
    print('出租车号:{} 在第{}分钟{}'.format(id, t, e))
    while True:
        time = t + random.randint(1, 10)
        try:
            t, id, e =t1.send(time)
            print('出租车号:{} 在第{}分钟{}'.format(id, t, e))
        except StopIteration:
            continue



if __name__=='__main__':
    run_event()