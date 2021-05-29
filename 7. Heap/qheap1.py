import queue

pq = queue.PriorityQueue()
pqRemove = queue.PriorityQueue()

Q = int(input())
for _ in range(Q):
  line = input()
  if line[0] == '1':
    v = int(line.split()[1])
    pq.put(v)
  if line[0] == '2':
    v = int(line.split()[1])
    pqRemove.put(v)
  if line[0] == '3':
    while not pqRemove.empty() and pqRemove.queue[0] == pq.queue[0]:
      pq.get()
      pqRemove.get()
    print(pq.queue[0])