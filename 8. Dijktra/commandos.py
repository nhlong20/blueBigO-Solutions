from heapq import heappush, heappop
INF = 10**9
MAX_BUILDINGS = 100 + 1
graph = [[] for _ in range(MAX_BUILDINGS)]
distS = [INF]*MAX_BUILDINGS
distD = [INF]*MAX_BUILDINGS

WEIGHT = 1

def dijkstra(s, dist, graph):
  min_heap = [(0, s)]
  dist[s] = 0

  while min_heap:
    d, u = heappop(min_heap)
    if d > dist[u]: continue
    for v in graph[u]:
      if dist[u] + WEIGHT < dist[v]:
        dist[v] = dist[u] + WEIGHT
        heappush(min_heap, (dist[v], v))  

T = int(input())
tc = 0
while tc < T:
  tc += 1
  N = int(input())
  R = int(input())

  for i in range(N):
    graph[i].clear()
    distS[i] = INF
    distD[i] = INF

  for _ in range(R):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
  
  s, d = map(int,input().split())
  dijkstra(s, distS, graph)
  dijkstra(d, distD, graph)

  ans = 0
  for u in range(N):
    ans = max(ans, distS[u] + distD[u])
  print(f"Case {tc}: {ans}")
