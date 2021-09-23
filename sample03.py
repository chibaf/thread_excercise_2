import threading
import queue, time

def thread1(a,q):
    time.sleep(1)
    ret = [1,2]
    q.put(ret)

q =queue.Queue()
th = threading.Thread(target=thread1, args=(1,q),daemon=True)
th.start()
#th.join()
while True:
  if threading.active_count()==1:
    rslt = q.get()
    print(rslt)
    print('thread ended')
    break
  print('not end')
  time.sleep(3)

exit()
