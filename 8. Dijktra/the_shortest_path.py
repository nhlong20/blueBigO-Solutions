import heapq
MAX = 2*10**6 +5
INF = 10**9 +5
graph = [[] for _ in range(MAX)]
dist = [INF]*MAX
s = int(input())


def dijktra(src, dist, graph):
  minHeap = []
  dist[src] = 0
  heapq.heappush(minHeap, (0, src))

  while len(minHeap) > 0:
    d, v = heapq.heappop(minHeap)
    if d != dist[v]: continue
    for u, w in graph[v]:
      if dist[v] + w < dist[u]:
        dist[u] = dist[v] + w
        heapq.heappush(minHeap, (dist[u], u))

for _ in range(s):
  nCities = int(input())
  cities = [None]
  # clear the graph
  for i in range(nCities+1):
    graph[i].clear()

  for i in range(1, nCities + 1):
    city_name = input()
    cities.append(city_name)
    n_connections = int(input())
    for _ in range(n_connections):
      u, w = map(int, input().split())
      graph[i].append((u, w))

  r = int(input())
  for _ in range(r):
    src_city, des_city = input().strip().split()
    src = cities.index(src_city)
    des = cities.index(des_city)
    
    for i in range(nCities+1):
      dist[i] = INF
    dijktra(src, dist, graph)
    print(dist[des])
  input()
