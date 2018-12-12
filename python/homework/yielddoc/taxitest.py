from collections import namedtuple
import queue, random

event = namedtuple('event', 'time,id,event')


class Sim:

    def __init__(self, num=3):

        self.taxi_events = queue.PriorityQueue()
        self.taxi_nums = list()
        self.gen_taxi(num)
        self.gen()

    def gen_taxi(self, num):
        for i in range(num):
            taxi_id = i + 1
            start_time = random.randint(2, 9)
            traps = random.randint(40, 90)
            taxi = self.taxi_event(time=start_time, id=taxi_id, trps=traps)
            self.taxi_nums.append(taxi)

    def taxi_event(self, time, id, trps):

        time = yield event(time, id, '出发')

        for i in range(trps):
            time = yield event(time, id, '载客')

            time = yield event(time, id, '下客')

        yield event(time, id, '回家')

    def echo(self, event):
        t, id, event = event
        print('出租车{}，在{}分钟时{}'.format(id, t, event))

    def gen(self):
        for i in self.taxi_nums:
            event = next(i)
            self.taxi_events.put(event)

    def taxirun(self):

        while True:
            if self.taxi_events.qsize() == 0:
                break
            event = self.taxi_events.get()
            t, id, e = event
            self.echo(event)
            time = t + random.randint(2, 10)
            try:
                event = self.taxi_nums[id - 1].send(time)
                self.taxi_events.put(event)
            except StopIteration:
                print('{}出租车事件完成'.format(id))


if __name__ == '__main__':
    s = Sim()
    s.taxirun()
