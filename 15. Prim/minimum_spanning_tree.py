import queue
INF = 10**9
class Node:
  def __init__(self, value, cost) -> None:
      self.value = value
      self.cost = cost
  def __lt__(self, other):
    return self.cost < other.cost

def prims(graph, costs,visited, src):
  costs[src] = 0
  pq = queue.PriorityQueue()
  pq.put(Node(src, 0))
  visited[src] = True
  while not pq.empty():
    u = pq.get().value
    visited[u] = True
    for node in graph[u]:
      v = node.value
      w = node.cost
      if visited[v]: continue
      if w >= costs[v]: continue
      costs[v] = w
      pq.put(node)
      
  
def main():
  n, m = map(int,input().split())
  graph = [[] for _ in range(n)]
  for _ in range(m):
    u, v, w = map(int,input().split())
    graph[u-1].append(Node(v-1, w))
    graph[v-1].append(Node(u-1, w))
  costs = [INF]*(n)
  visited = [False]*(n)

  prims(graph, costs,visited, 0)
  ans = 0
  for cost in costs:
    ans += cost
  print(ans)

main()