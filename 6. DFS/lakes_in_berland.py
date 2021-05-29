MAX = 50 + 1
# movement
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

# visited point
visited = [[False]*MAX for _ in range(MAX)]

#list of lakes in the land
lakes = []

# map to store land's status
tables = []

# read input()
n, m , k = map(int,input().split())

def DFS(sr, sc):
  st = []
  st.append((sr,sc))
  visited[sr][sc] = True

  isOcean = False
  pendingLake = []
  while len(st) > 0:
    r, c = st.pop()
    pendingLake.append((r,c))
    if r == 0 or c == 0 or r == n -1 or c == m - 1:
      isOcean = True
    for i in range(4):
      rr = r + dr[i]
      cc = c + dc[i]

      # skip out of bounds
      if rr < 0 or cc < 0: continue
      if rr > n- 1 or cc > m-1: continue
      # skip visited cells and not water cells
      if visited[rr][cc]: continue
      if tables[rr][cc] == "*": continue

      visited[rr][cc] = True
      st.append((rr, cc))

  if not isOcean:
    lakes.append(pendingLake)

# read input table
for _ in range(n):
  tables.append(list(input()))


for i in range(n):
  for j in range(m):
    if visited[i][j]: continue
    if tables[i][j] == "*": continue
    DFS(i,j)

lakes.sort(key= lambda lake: len(lake))
# cover the smallest lake
covered_cells = 0

for i in range(len(lakes) - k):
  covered_cells += len(lakes[i])
  for r,c in lakes[i]:
    tables[r][c] = "*"

print(covered_cells)

for i in range(n):
  print("".join(tables[i]))