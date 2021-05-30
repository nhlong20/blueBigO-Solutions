import heapq
MAX = 500 + 1
INF = 10**9
dist = [INF]*MAX
graph = [[] for _ in range(MAX)]

def dijktra(src):
  minHeap = []
  dist[src] = 0
  heapq.heappush(minHeap,(src, 0))
  
  while len(minHeap) > 0:
    v, cur_dist = heapq.heappop(minHeap)
    if cur_dist != dist[v]: continue

    for u, w in graph[v]:
      if dist[v] + w < dist[u]:
        dist[u] = dist[v] + w
        heapq.heappush(minHeap,(u, dist[u]))

def main():
  n = int(input())

  for _ in range(n):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

  src = int(input())
  dijktra(src)

  Q = int(input())

  for _ in range(1,Q+1):
    des = int(input())
    print("NO PATH") if dist[des] == INF else print(dist[des])

main()
  