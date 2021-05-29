import sys
sys.setrecursionlimit(100000)
dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]
MAX = 100 + 5

matrix = [None]*MAX
dist = [[0] * MAX for _ in range(MAX)]

def DFS(sr, sc):
  if dist[sr][sc]: return dist[sr][sc]
  max_path = 0

  for k in range(8):
    rr, cc = sr + dr[k], sc + dc[k]
    
    if rr < 0 or cc < 0 or rr >= n_rows or cc >= n_cols: continue
    if ord(matrix[rr][cc]) != ord(matrix[sr][sc])+1: continue

    max_path = max(max_path, DFS(rr, cc))
  dist[sr][sc] = max_path + 1
  return dist[sr][sc]

T = 0
while True:
  T +=1
  n_rows, n_cols = map(int, input().split())
  if n_rows == 0 and n_cols == 0: break
  for i in range(n_rows):
    matrix[i] = input()
    for j in range(n_cols):
      dist[i][j] = 0

  res = 0
  for i in range(n_rows):
    for j in range(n_cols):
      if matrix[i][j] != 'A': continue
      res = max(res, DFS(i,j))

  print(f'Case {T}: {res}')