import queue, random
from collections import namedtuple

event = namedtuple('event', 'time,id,event')


class noTaxi:
    def __init__(self, num=3):
        self.msg_queue = queue.PriorityQueue()
        self.taxi_list = list()

        for i in range(num):
            id = i + 1
            start_time = random.randint(3, 7)
            trips = random.randint(50, 90)
            taxinum = self.taxi_event(time=start_time, id=id, trip=trips)
            self.taxi_list.append(taxinum)

    def taxi_event(self, time=0, id=1, trip=50):
        time = yield event(time, id, '开始上班')

        for i in range(trip):
            time = yield event(time, id, '载客')

            time = yield event(time, id, '下客')

        yield event(time, id, '打开下班')

    def taxiLoop(self):
        for i in self.taxi_list:
            event = next(i)
            self.msg_queue.put(event)
        while True:
            if self.msg_queue.qsize() == 0:
                break
            event = self.msg_queue.get()
            t, id, e = event
            self.taxi_print(event)
            nexttime = t + random.randint(3, 6)
            try:
                event = self.taxi_list[id - 1].send(nexttime)
            except StopIteration:
                continue
            self.msg_queue.put(event)
        print('事件完成')

    def taxi_print(self, event):
        t, id, e = event
        print('在{}分钟的时候，第{}出租车{}'.format(t, id, e))


if __name__ == '__main__':
    t = noTaxi()
    t.taxiLoop()
