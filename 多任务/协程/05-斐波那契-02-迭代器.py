import collections
from collections.abc import Iterable
from collections.abc import Iterator
import time


class Fibonacci(object):
    def __init__(self, all_num):
        self.all_num = all_num
        self.current_num = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        """如果想让一个对象成为一个可以迭代的对象，即可以使用for, 那么必须实现__iter__方法"""
        return self

    def __next__(self):
        if self.current_num < self.all_num:
            ret = self.a
            self.a, self.b = self.b, self.a + self.b
            self.current_num += 1
            return ret
        else:
            raise StopIteration

fibo = Fibonacci(10)

for num in fibo:
    print(num)
    time.sleep(1)