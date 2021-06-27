from heapq import heappush, heappop
INF = 10**9
MAX = 10**3+1
graph = [[] for _ in range(MAX)]
costs = [INF]*MAX
visited = [False]*MAX

t = int(input())

def prims(s, graph, visited, costs):
  min_heap = [(0, s)]
  costs[s] = 0

  while min_heap:
    u = heappop(min_heap)[1]
    visited[u] = True
    for v, w in graph[u]:
      if visited[v]: continue
      if costs[v] > w:
        costs[v] = w
        heappush(min_heap, (costs[v], v))
      

for tc in range(t):
  p = int(input())
  n = int(input())
  m = int(input())

  for i in range(n):
    graph[i].clear()
    costs[i] = INF
    visited[i] = False

  for _ in range(m):
    u, v, w = map(int, input().split())
    w = w*p
    graph[u-1].append((v-1, w))
    graph[v-1].append((u-1, w))
  prims(0, graph, visited, costs)

  ans = 0
  for cost in costs[:n]: 
    ans += cost
  print(ans)
    
