import heapq
INF = 10**9
MAX = 100 + 5
graph = [[] for _ in range(MAX)]
dist = [INF]*MAX

def dijktra(src):
  minHeap = []
  dist[src] = 0
  heapq.heappush(minHeap, (dist[src], src))

  while len(minHeap) > 0:
    cur_dist, v = heapq.heappop(minHeap)
    if cur_dist != dist[v]: continue
    for u, w in graph[v]:
      if dist[v] + w < dist[u]:
        dist[u] = dist[v] + w
        heapq.heappush(minHeap, (dist[u], u))


N = int(input())
exit_cell = int(input())
T = int(input())
M = int(input())

for _ in range(M):
  u, v, w = map(int, input().split())
  graph[v-1].append((u-1, w))

dijktra(exit_cell-1)

count = 0

for v in range(N):
  if(dist[v] <= T): count +=1
print(count)