from collections import namedtuple
import random, queue

Event = namedtuple('Event', 'time,id,event')


class Taxi(object):

    # 初始化taxi
    def __init__(self, taxi_num):

        self.taxi_events = queue.PriorityQueue()
        self.taxi_nums = list()

        for i in range(taxi_num):
            taxi_id = i + 1
            start_time = random.randint(1, 30)
            taxi_traps = random.randint(50, 100)
            taxi_num = self.taxi_event(time=start_time, id=taxi_id, trap=taxi_traps)
            self.taxi_nums.append(taxi_num)

    def taxi_event(self, time=0, id=1, trap=50):
        time = yield Event(time, id, 'leave home')
        for i in range(trap):
            time = yield Event(time, id, 'pick people')
            time = yield Event(time, id, 'drop people')
        yield Event(time, id, 'go home')

    def taxi_run(self):

        for i in self.taxi_nums:
            event=next(i)
            self.taxi_events.put(event)

        while True:
            if self.taxi_events.qsize() == 0:
                break
            event = self.taxi_events.get()
            t, id, e = event
            print('出租车号:{} 在第{}分钟{}'.format(id, t, e))
            time = t + random.randint(5, 10)
            try:
                event = self.taxi_nums[id - 1].send(time)
            except StopIteration:
                continue
            self.taxi_events.put(event)


if __name__ == '__main__':
    taxi = Taxi(5)
    taxi.taxi_run()
