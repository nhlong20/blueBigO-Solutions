
from heapq import heappush, heappop
MAX_CITIES = 10**5 + 1
INF = 10**11 +5
graph = [[] for _ in range(MAX_CITIES)]
distA = [INF]*MAX_CITIES
distB = [INF]*MAX_CITIES

def dijkstra(s, dist, graph):
  min_heap = []
  dist[s] = 0
  heappush(min_heap, (0, s))
  
  while len(min_heap) > 0:
    d, u = heappop(min_heap)

    if dist[u] < d: continue
    
    for v, w  in graph[u]:
      if dist[u] + w < dist[v]:
        dist[v] = dist[u] + w
        heappush(min_heap, (dist[v], v))
  
def main():
  n, m, k, x = map(int,input().split())
  chocolate_cities = list(map(int,input().split()))[:k]

  for _ in range(m):
    u, v, w = map(int,input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))
  
  A, B = map(int, input().split())

  dijkstra(A, distA, graph)
  dijkstra(B, distB, graph)

  ans = INF

  for city in chocolate_cities:
    if distB[city] <= x:
      ans = min(ans, distA[city] + distB[city])
  print(ans if ans != INF else -1)

if __name__ == '__main__':
  main()
