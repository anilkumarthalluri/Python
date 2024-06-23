from threading import *
from time import sleep

class hello(Thread):
    def run(self):
        for i in range(10):
          print("hello")
          sleep(0.5)
        
class hi(Thread):
    def run(self):
        for i in range(10):
         print("hi")
         sleep(0.5)
        
obj1 = hello()
obj2 = hi()
obj1.start()
sleep(0.1)
obj2.start()

obj1.join()
obj2.join()
print("last thread : bye")

