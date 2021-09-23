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
    if i>5:
      break;
    th = threading.Thread(target=thread1, args=(i,q),daemon=True)
    th.start()
  print(str(i)+' dose not end')
  time.sleep(2)  #do other tasks

exit()
