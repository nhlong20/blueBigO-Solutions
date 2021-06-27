from heapq import heappush, heappop
INF = 10**9
MAX = 50 + 1


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
      

T = int(input())
tc = 0
while tc < T:
  tc += 1
  input()
  nRoads = int(input())
  S = dict()
  nCities = 0
  cities = []
  graph = []

  for _ in range(nRoads):
    u, v, w  = input().split()
    if u not in S:
      graph.append([])
      S[u] = nCities
      nCities += 1
    if v not in S:
      graph.append([])
      S[v] = nCities
      nCities += 1

    graph[S[u]].append((S[v], int(w)))
    graph[S[v]].append((S[u], int(w)))

  costs = [INF]*nCities
  visited = [False]*nCities
  prims(0, graph, visited, costs)
  ans = 0

  for cost in costs[:nCities]: 
    if cost >= INF: 
      ans = "Impossible"
      break
    ans += cost
  print(f"Case {tc}: {ans}")
