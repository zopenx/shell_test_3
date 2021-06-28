# import multiprocessing
# import threading
# import time
#
# import psutil
# import os
# import subprocess
# # print(psutil.cpu_count())
# # print(os.cpu_count())
# import random
# from multiprocessing import Process, Value, Array, Manager, Queue
#
#
#
# def run_bash(sleep_time, fib_number):
#     proc = subprocess.Popen('./fib_sh.sh %s %s ' % (sleep_time, fib_number), stdout=subprocess.PIPE, shell=True)
#     # ret_value.value = int(proc.stdout.read())
#     # print(ret_value.value)
#     # lst_values.append(int(proc.stdout.read()))
#     # q.put(int(proc.stdout.read()))
#     return int(proc.stdout.read())
#
#
# class FibonachyBash:
#     def __call__(self, fib_number, sleep_time):
#         r = run_bash(sleep_time, fib_number)
#         print(r)
#
#
# if __name__ == '__main__':
#     for i in range(4):
#         p = Process(target=FibonachyBash(), args=(random.randint(13, 20), random.randint(0,3)))
#         p.start()
#         p.join()


# --------------------
import random
import subprocess
import threading
import time
import datetime
import os

list_all = []


def run_bash(sleep_time, fib_number):
    proc = subprocess.Popen('./fib_sh.sh %s %s ' % (sleep_time, fib_number), stdout=subprocess.PIPE, shell=True)
    return int(proc.stdout.read())


class FiboThread(threading.Thread):
    def __init__(self, lock, number):
        super(FiboThread, self).__init__()
        self.__lock = lock
        self.__number = number

    def run(self):
        while True:
            ret = run_bash(random.randint(0,3), random.randint(13, 20))
            self.__lock.acquire()
            global list_all
            list_all.append(ret)
            # print("Number_Thread: ", self.__number, " value thread:", ret)
            self.__lock.release()


class OutThread(threading.Thread):
    def __init__(self, lock):
        super(OutThread, self).__init__()
        self.__time = datetime.datetime.now()
        self.__lock = lock

    def run(self):
        while True:
            time.sleep(5)
            sum = 0
            self.__lock.acquire()
            global list_all
            for x in list_all:
                sum+=x
            new_time = datetime.datetime.now()
            delta = new_time - self.__time
            # time.strftime('%c')
            print(delta, sum)
            list_all = []
            self.__lock.release()


if __name__ == '__main__':
    lock = threading.Lock()
    th1 = OutThread(lock)
    th1.start()
    for i in range(os.cpu_count()):
        tread = FiboThread(lock, i)
        tread.start()
