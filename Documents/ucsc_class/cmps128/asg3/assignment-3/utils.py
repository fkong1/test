import time


class State:
    def __init__(self, id, num):
        self.id = id
        self.num = num
        self.clock = [0] * num

    def event(self, message):
        self.clock[self.id] += 1
        return Event(clock=self.clock[:], message=message, timestamp=time.time())

class Event:
    def __init__(self, clock=[], message='', timestamp=time.time()):
        self.clock = clock
        self.message = message
        self.timestamp = timestamp

    def __cmp__(self, other):
        a = self.clock
        b = other.clock
        if len(a) != len(b):
            raise StandardError()
        strict_before = False
        for i in range(len(a)):
            if a[i] < b[i]:  # all less or equal, one strict less
                strict_before = True
            elif a[i] > b[i]:  # has no less, return
                return 1

        return -1 if strict_before else 0
