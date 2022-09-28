"""
import threading
import time


class ClockThread(threading.Thread):
    def __init__(self, interval):
        super().__init__()
        self.daemon = True
        self.interval = interval

    def run(self):
        x = 11
        while x > 1:
            x -= 1
            print(f'Number: {x}')
            time.sleep(self.interval)


t = ClockThread(0.5)
t.start()
t.join()"""

"""
import threading
import time

def handler(started=0, finished=0):
    result = 0
    for i in range(started, finished):
        result += i
    results.append(result)

results = []

task1 = threading.Thread(
    target=handler,
    kwargs={'finished': x for x in range(1, 3)}
)
task2 = threading.Thread(
    target=handler,
    kwargs={'finished': x for x in range(3, 5)}
)

task1.start()
task2.start()

task1.join()
task2.join()


print('Value: ', handler())"""

"""import threading

def doubler(x):
    x = 11
    while x > 1:
        x -= 1
    print(threading.currentThread().getName() + '\n')

    print(f'Number: {x}')



if __name__ == '__main__':
    for i in range(2):
        my_thread = threading.Thread(target=doubler, args=(i,))
        my_thread.start()
        my_thread.join()"""



"""
class ClockThread(threading.Thread):
    def __init__(self, interval):
        super().__init__()
        self.daemon = True
        self.interval = interval

    def run(self):
        x = 11
        while x > 1:
            x -= 1
            print(f'Number: {x}')
            time.sleep(self.interval)

    if __name__ == '__main__':
        for i in range(2):
            my_thread = threading.Thread(target=, args=(i,))

            my_thread.start()
            my_thread.join()


t = ClockThread(0.5)"""

#print(threading.currentThread().getName() + '\n')

"""
import threading
import time

class Work(threading.Thread):
    def __init__(self, interval):
        super().__init__()
        self.interval = interval

    def run(self,):
        x = 11
        while x > 6:
            x -= 1
            print(f'({threading.currentThread().getName()}) Number: {x}')
            time.sleep(self.interval)


class Wor(threading.Thread):
    def __init__(self, interval):
        super().__init__()
        self.interval = interval

    def run(self,):
        x = 6
        while x > 1:
            x -= 1
            print(f'({threading.currentThread().getName()}) Number: {x}')
            time.sleep(self.interval)

for x in range(0,1):
    t1 = Work(0.3)
    t2 = Wor(0.3)
    t1.start()
    t1.join()
    t2.start()
    t2.join()
"""

import threading
import time

class Work(threading.Thread):
    def __init__(self, interval):
        super().__init__()
        self.interval = interval

    def run(self,):
        x = 11
        while x > 1:
            x -= 1
            print(f'({threading.currentThread().getName()}) Number: {x}')
            time.sleep(self.interval)



t1 = Work(0.5)
t2 = Work(0.2)

t1.start()
t2.start()
t1.join()
t2.join()
