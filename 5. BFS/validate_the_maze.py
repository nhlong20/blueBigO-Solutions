import queue
test_case = int(input())

while test_case:
  test_case -=1
  M, N = map(int, input().strip().split())
  maze = [[] for _ in range(M)]
  rq, cq = queue.Queue(), queue.Queue()

  # a variables to check if get the end
  reached_end = False
  # MxN matrix of False values to track visited nodes at [i,j]
  visited = [[False for i in range (N)] for _ in range(M)]
  openingPos = []
  # init direction vectors
  dr = [-1, 1, 0, 0]
  dc = [0, 0, 1, -1]
  for i in range(M):
    maze[i] = input()
    for j in range(N):
      if((i == 0 or j == 0 or i == M-1 or j == N - 1) and maze[i][j] == '.'):
        openingPos.append((i,j))
  if len(openingPos) == 2:
    sr = openingPos[0][0]
    sc = openingPos[0][1]
    er = openingPos[1][0]
    ec = openingPos[1][1]
    rq.put(sr)
    cq.put(sc)
    visited[sr][sc] = True
    while not rq.empty():
      r = rq.get()
      c = cq.get()
      if r == er and c == ec:
        reached_end = True
        break
      for i in range(4):
        rr = r + dr[i]
        cc = c + dc[i]

        # Skip out of bounds location
        if rr < 0 or cc < 0: continue
        if rr >= M or cc >= N: continue
        #skip visited location and blocked cells
        if visited[rr][cc]: continue
        if maze[rr][cc] == '#': continue

        visited[rr][cc] = True
        rq.put(rr)
        cq.put(cc)
    if reached_end: 
      print("valid")
    else:
      print("invalid")
  else:
    print("invalid")
