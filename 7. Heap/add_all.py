import queue

pq = queue.PriorityQueue()

while True:

  n = int(input())

  if n == 0: break

  arr = list(map(int,input().split()))

  for el in arr:
    pq.put(el)
    
  cost = 0
  
  while pq.qsize() > 1:
    a = pq.get()
    b = pq.get()
    cost += a + b
    pq.put(a+b)
  print(cost)
  pq.get()