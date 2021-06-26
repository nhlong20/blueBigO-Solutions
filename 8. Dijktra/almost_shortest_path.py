from heapq import heappush, heappop
INF = 10**9
MAX_NODE = 500 + 5

graphS = [[] for _ in range(MAX_NODE)]
graphD = [[] for _ in range(MAX_NODE)]
graph = [[] for _ in range(MAX_NODE)]
distS = [INF]*MAX_NODE
distD = [INF]*MAX_NODE
dist = [INF]*MAX_NODE


def dijkstra(s, dist, graph):
  min_heap = []
  dist[s] = 0
  heappush(min_heap, (0, s))
  
  while len(min_heap) > 0:
    d, u = heappop(min_heap)

    if dist[u] != d: continue
    
    for v, weight  in graph[u]:
      if d + weight < dist[v]:
        dist[v] = d + weight
        heappush(min_heap, (dist[v], v))
  
def main():
  while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0: break
    S, D = map(int, input().split())

    # reset graph
    for i in range(n):
      graphS[i].clear()
      graphD[i].clear()
      graph[i].clear()
      distS[i] = INF
      distD[i] = INF
      dist[i] = INF

    for _ in range(m):
      u, v, w = map(int, input().split())
      graphS[u].append((v, w))
      graphD[v].append((u, w))

    dijkstra(S, distS, graphS)
    dijkstra(D, distD, graphD)
    shortest_length = distS[D]

    # this step to get rid of the edge of the shortest path
    for u in range(n):
      for v, w in graphS[u]:
        if distS[u] + w + distD[v] != shortest_length:
          graph[u].append((v, w))
    
    dijkstra(S, dist, graph)

    print(dist[D] if dist[D] != INF else -1)

if __name__ == '__main__':
  main()