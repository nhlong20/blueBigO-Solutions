import queue
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

MAX = 1000 + 5
visited = [[False]*MAX for _ in range(MAX)] 
dist = [[-1]*MAX for _ in range(MAX)]
bomb_map = [[0]*MAX for _ in range(MAX)]

def BFS(start, end):
  q = queue.Queue()
  q.put(start)
  sr, sc = start
  visited[sr][sc] = True
  dist[sr][sc] = 0
  reached_end = False
  while not q.empty():
    r, c = q.get()

    if r == end[0] and c == end[1]:
      reached_end = True
    for i in range(4):
      rr = r + dr[i]
      cc = c + dc[i] 
      # Skip out of bounds location
      if rr < 0 or cc < 0: continue
      if rr >= tr or cc >= tc: continue
      #skip visited location and blocked cells
      if visited[rr][cc]: continue
      if bomb_map[rr][cc] == 1: continue 
      dist[rr][cc] = dist[r][c] + 1
      visited[rr][cc] = True

      q.put((rr,cc))
    
    if reached_end: break


while True:
  tr, tc = map(int,input().split())
  if tr == 0 and tc == 0: break
  for i in range(MAX):
    for j in range(MAX):
      visited[i][j] = False
      dist[i][j] = -1
      bomb_map[i][j] = 0
  nRowHasBom = int(input())
  for i in range(nRowHasBom):
    line = list(map(int,input().split()))
    r = line[0]
    nBomInRow = line[1]
    colBombLocation = line[2:]
    for c in colBombLocation:
      bomb_map[r][c] = 1

  sr, sc = map(int,input().split())
  er, ec = map(int,input().split())

  BFS((sr,sc), (er,ec))
  
  print(dist[er][ec])