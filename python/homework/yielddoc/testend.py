import random, queue
from collections import namedtuple

event = namedtuple('event', 'time,id,event')


class Simulator:

    def __init__(self, taxi_num=3):
        self.taxi_events = queue.PriorityQueue()
        self.taxi_num = list()
        for i in range(taxi_num):
            taxi_id = i + 1
            taxi_start_time = random.randint(1, 20)
            taxi_trps = random.randint(10, 20)
            taxi_tmp = self.taxi_event(time=taxi_start_time, id=taxi_id, trps=taxi_trps)
            self.taxi_num.append(taxi_tmp)

    def taxi_event(self, time=0, id=1, trps=50):
        time = yield event(time, id, 'leave home')
        for i in range(trps):
            time = yield event(time, id, 'pick people')
            time = yield event(time, id, 'drop people')
        yield event(time, id, 'go home')

    def run_taxi(self):

        for i in self.taxi_num:
            event = next(i)
            self.taxi_events.put(event)

        while True:
            if self.taxi_events.qsize()==0:
                break
            event = self.taxi_events.get()
            t, id, e = event
            time = t + random.randint(3, 6)
            print('出租车号:{} 在第{}分钟{}'.format(id, t, e))
            try:
                event = self.taxi_num[id - 1].send(time)
            except StopIteration:
                continue
            self.taxi_events.put(event)
        print('事件已经结束')


if __name__ == '__main__':
    sim = Simulator()
    sim.run_taxi()
