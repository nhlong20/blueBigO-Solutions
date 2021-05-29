import queue
n_test_case = int(input())

for _ in range(n_test_case):
  n, pos = map(int,input().split())
  q = queue.Queue()
  pq = queue.PriorityQueue()

  count = 0

  for pior in map(int,input().split()):
    q.put(pior)
    pq.put(-pior)

  printed = False
  min_count = 0
  while not printed:
    job = q.get()
    # neu job dau tien in duoc,    
    if job == -pq.queue[0]:
      # nhung khong phai job cua ban
      if pos != 0: 
        min_count +=1
        pos -=1
        pq.get()
      else:
        min_count +=1
        break

     # neu job dau tien khong in duoc,    
    if job < -pq.queue[0]:
      # neu khong phai job cua ban
      if pos != 0: 
        pos -=1
      # neu do la job cua ban
      else: pos = q.qsize()
      q.put(job)
  print(min_count)
