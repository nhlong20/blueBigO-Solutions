import queue
test_case = 1

while True:
  P, C = map(int, input().strip().split())
  if not P and not C:
    break
  # init queue
  q = queue.Queue()
  for order in range(1, min(P,C) +1):
    q.put(order)
  print(f"Case {test_case}:")
  test_case += 1

  for _ in range(C):
    line = input().split()
    cmd = line[0]
    if cmd == "N":
      print(q.queue[0])
      q.put(q.get())
    else:
      x = int(line[1])
      n = q.qsize()
      q.put(x)
      for i in range(n):
        first = q.get()
        if first != x:
          q.put(first)


