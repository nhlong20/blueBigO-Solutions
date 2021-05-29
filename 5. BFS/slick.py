import queue
# init direction vectors
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]
MAX = 250
image = [[] for _ in range(MAX)]
while True:
  N, M = map(int, input().strip().split())
  if N == 0 and M == 0: break
  
  slick_fre = [0]*(M*N + 1)
  # MxN matrix of False values to track visited nodes at [i,j]
  visited = [[False for i in range (M)] for _ in range(N)]

  for i in range(N):
    image[i] = list(map(int, input().strip().split()))

  q = queue.Queue()
  total = 0
  for i in range(N):
    for j in range(M):
      if visited[i][j]: continue
      if not image[i][j]: continue
      visited[i][j] = True
      q.put((i,j))
  
      move_count = 1
      while not q.empty():
        (r,c) = q.get()
        for k in range(4):
          rr = r + dr[k]
          cc = c + dc[k]
          # Skip out of bounds location
          if rr < 0 or cc < 0: continue
          if rr >= N or cc >= M: continue
          #skip visited location and blocked cells
          if visited[rr][cc]: continue
          if image[rr][cc] == 0: continue
          move_count +=1
          visited[rr][cc] = True
          q.put((rr,cc))
      slick_fre[move_count] +=1
      total += 1
  print(total)
  for i in range(N*M+1):
    if(slick_fre[i] != 0):
      print(i, slick_fre[i])
