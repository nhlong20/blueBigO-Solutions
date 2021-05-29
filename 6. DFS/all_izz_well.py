import sys
sys.setrecursionlimit(100000)
dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]
MAX = 100 + 5

matrix = [None]*MAX
visited = [[False] * MAX for _ in range(MAX)]
res = "ALLIZZWELL"
65-65
def DFS(sr, sc, count = 1):
  global found
  visited[sr][sc] = True
  if count == len(res):
    found = True
    return
  
  for k in range(8):
    rr = sr + dr[k]
    cc = sc + dc[k]

    if rr < 0 or cc < 0: continue
    if rr >= n_rows or cc >= n_cols: continue
    if visited[rr][cc]: continue
    if matrix[rr][cc] != res[count]: continue

    visited[rr][cc] = True
    DFS(rr, cc, count + 1)
    visited[rr][cc] = False

n_test_case = int(input())
for _ in range(n_test_case):
  n_rows, n_cols = map(int, input().split())

  for i in range(n_rows):
    matrix[i] = input()
    for j in range(n_cols):
      visited[i][j] = False
  
  found = False
  for i in range(n_rows):
    for j in range(n_cols):
      if found: break
      if matrix[i][j] != res[0]: continue
      DFS(i, j, 1)
  
  print(["NO", "YES"][found])
  input()
