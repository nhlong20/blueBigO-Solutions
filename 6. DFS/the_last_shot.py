MAX = 10**5 +5
graph = [[] for _ in range(MAX)]
n, m = map(int, input().split())

for _ in range(m):
  u, v = map(int, input().split())
  if u == v: continue
  graph[u-1].append(v-1)


def DFS(i):
  st = []
  st.append(i)
  visited[i] = True
  count = 1
  while len(st) > 0:
    u = st.pop()
    for v in graph[u]:
      if visited[v]: continue
      visited[v] = True
      st.append(v)
      count +=1
  return count


max_impact = 0
for i in range(n):
  visited = [False]*n
  max_impact = max(max_impact, DFS(i))
print(max_impact)