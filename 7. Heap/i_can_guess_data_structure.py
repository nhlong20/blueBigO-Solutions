import queue

st = []
q = queue.Queue()
pq = queue.PriorityQueue()

while True:
  isStack = isQueue = isPQ = True
  st.clear()
  q.queue.clear()
  pq.queue.clear()
  try:
    n = int(input())
  except EOFError:
    break

  for _ in range(n):
    opt, val = map(int, input().split())
    if opt == 1:
      st.append(val)
      q.put(val)
      pq.put(-val)
    elif opt == 2:
      if val != st.pop():
        isStack = False
      if val != q.get():
        isQueue = False
      if val != -pq.get():
        isPQ = False
  res = isStack + isQueue +isPQ
  out = ""
  if res == 0: out = "impossible"
  elif res > 1: out = "not sure"
  else:
    if isPQ: out = "priority queue"
    if isStack: out = "stack"
    if isQueue: out = "queue"
  print(out)
