import threading
import queue,time

def thread1(a,q):
    time.sleep(1)
    ret = [a,2]
    q.put(ret)

i=1
q =queue.Queue()
th = threading.Thread(target=thread1, args=(i,q),daemon=True)
th.start()
#th.join()
while True:
  if threading.active_count()==1:
    rslt = q.get()
    print(rslt)
    print(str(i)+': thread ended')
    i=i+1
    if i>10:
      break;
    th = threading.Thread(target=thread1, args=(i,q),daemon=True)
    th.start()
  print('not end')
  time.sleep(2)

exit()
