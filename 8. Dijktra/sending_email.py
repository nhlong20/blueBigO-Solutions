import heapq
INF = 10**9 + 5
MAX_SERVER = 2*10*5 + 5

Q = int(input())

def dijktra(src, T, dist, graph):
  minHeap = []
  dist[src] = 0
  heapq.heappush(minHeap, (0, src))

  while len(minHeap)> 0:
    d, v = heapq.heappop(minHeap)
    if v == T: break
    if d != dist[v]: continue
    for u, w in graph[v]:
      if dist[v] + w < dist[u]:
        dist[u] = dist[v] + w
        heapq.heappush(minHeap, (dist[u], u))

for case in range(1, Q + 1):
  N, M, S, T = map(int,input().split())
  graph = [[] for _ in range(MAX_SERVER)]
  dist = [INF]*MAX_SERVER

  for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))
  
  dijktra(S, T, dist, graph)
  print(f"Case #{case}: {dist[T]}") if dist[T] != INF else print(f"Case #{case}: unreachable")