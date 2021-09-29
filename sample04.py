import threading
import queue,time

def thread1(a,q):
    time.sleep(1)
    ret = [a,2]
    q.put(ret)

i=1
q =queue.Queue()  # queue which stores a result of a thread
th = threading.Thread(target=thread1, args=(i,q),daemon=True)
th.start()
#th.join()
while True:
  if th.is_alive()==False:
    result = q.get()
    print("thread: "+str(i)+" "+str(result))
    i=i+1
    if i>5:
      break;
    th = threading.Thread(target=thread1, args=(i,q),daemon=True)
    th.start()
  time.sleep(2)  #do other tasks

exit()
