import queue
MAX = 501
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]
n, m = map(int,input().split())

rect = [[] for _ in range(n)]

# read the map
for i in range(n):
  rect[i] = list(input())
sr, sc = map(int, input().split())
er, ec = map(int, input().split())
def BFS(S, E):
  # a variables to check if get the end
  q = queue.Queue()
  rect[S[0]][S[1]] = "X"
  q.put(S)
  while not q.empty():
    r,c = q.get()
    for i in range(4):
      rr = r + dr[i]
      cc = c + dc[i]
      if(rr == E[0] and cc == E[1] and rect[rr][cc] == "X"):
        return True
      # Skip out of bound
      if rr < 0 or cc < 0: continue
      if rr >= n or cc >= m: continue
      
      #Skip visited and cracked ice
      if rect[rr][cc] == ".":
        rect[rr][cc] = "X"
        q.put((rr,cc))

  return False
res = BFS((sr-1,sc-1),(er-1,ec-1))
print(["NO", "YES"][res])