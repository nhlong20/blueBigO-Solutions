import queue
test_case = int(input())

for t in range(test_case):
  W, H = map(int, input().strip().split())
  place = [[] for _ in range(H)]
  rq, cq = queue.Queue(), queue.Queue()

  # a variables to check if get the end
  reached_end = False
  # MxN matrix of False values to track visited nodes at [i,j]
  visited = [[False for i in range (W)] for _ in range(H)]

  move_count = 0
  start_pos = ()
  # init direction vectors
  dr = [-1, 1, 0, 0]
  dc = [0, 0, 1, -1]
  for i in range(H):
    place[i] = input()
    posC = place[i].find("@")
    if posC != -1:
      start_pos = (i,posC)
  
  sr = start_pos[0]
  sc = start_pos[1]
  rq.put(sr)
  cq.put(sc)
  visited[sr][sc] = True
  move_count +=1
  while not rq.empty():
    r = rq.get()
    c = cq.get()
    for i in range(4):
      rr = r + dr[i]
      cc = c + dc[i]
      # Skip out of bounds location
      if rr < 0 or cc < 0: continue
      if rr >= H or cc >= W: continue
      #skip visited location and blocked cells
      if visited[rr][cc]: continue
      if place[rr][cc] == '#': continue
      move_count +=1
      visited[rr][cc] = True
      rq.put(rr)
      cq.put(cc)
  print(f"Case {t+1}: {move_count}")
