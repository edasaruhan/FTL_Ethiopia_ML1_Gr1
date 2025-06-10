import time
import threading
def stepper(n, name):
    print("Hi, I am {}. Going to sleep for 5 sec\n".format(name))
    time.sleep(n)
    print('{} has woken up from sleep \n'.format(name))

threads = []
for i in range(5):
    t = threading.Thread(target = stepper, name= 'thread{}'.format(i),
                        args= (5, 'thread{}'.format(i)))
    t.start()
    print("{} has started".format(t.name))
for t in threads:
    t.join()