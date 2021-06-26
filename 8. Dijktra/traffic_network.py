import heapq

INF = 10**9
MAX_MODE = 10**4 + 5
MAX_ONE_WAY = 10**5 + 5
MAX_TWO_WAY = 300

graphS = [[] for _ in range(MAX_MODE)]
graphT = [[] for _ in range(MAX_MODE)]
distS  = [INF]*MAX_MODE
distT = [INF]*MAX_MODE

class Node:
  def __init__(self, val, dist) -> None:
    self.val = val
    self.dist = dist
  def __lt__(self, o):
    return self.dist < o.dist

def dijktra(graph, dist, src):
  min_heap = []
  dist[src] = 0
  heapq.heappush(min_heap, Node(src, 0))

  while len(min_heap) > 0:
    tmp = heapq.heappop(min_heap)
    d, u = tmp.dist, tmp.val

    if d != dist[u]: continue
    for v, w in graph[u]:
      if dist[u] + w < dist[v]:
        dist[v] = dist[u] + w
        heapq.heappush(min_heap, Node(v, dist[v]))

tc = int(input())
for test in range(tc):
  N, M, K, S, T = map(int, input().strip().split())

  # reset graph and dist
  for i in range(N):
    graphS[i].clear()
    graphT[i].clear()
    distS[i] = INF
    distT[i] = INF

  # init one-way graph and its reversion
  for _ in range(M):
    u, v, w = map(int,input().strip().split())
    graphS[u-1].append((v-1, w))
    graphT[v-1].append((u-1, w))

  # find shortest path from S, T to another vertices
  dijktra(graphS, distS, S-1)
  dijktra(graphT, distT, T-1)

  ans = distS[T-1]
  # traverse all 2-way path to find shortest path
  for _ in range(K):
    u, v, w = map(int,input().strip().split()) 
    # S -> u -> v -> T
    ans = min(ans, distS[u-1] + w + distT[v-1])
    # S -> v -> u -> T
    ans = min(ans, distS[v-1] + w + distT[u-1])

  print(ans if ans != INF else -1)