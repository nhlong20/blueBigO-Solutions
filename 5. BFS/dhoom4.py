import queue
MAX = 10**5+5
MOD = 10**5

s, e = map(int, input().strip().split())
n = int(input())
arr = list(map(int, input().strip().split()))

def BFS(s, key):
  dist = [-1]*MAX
  q = queue.Queue()
  q.put(s)
  dist[s] = 0

  while not q.empty():
    u = q.get()
    for el in arr:
      new_key = (u*el)%MOD
      if dist[new_key] == -1:
        dist[new_key] = dist[u] + 1
        q.put(new_key)
        
        if new_key == key:
          return dist[new_key]
  return -1

print(BFS(s,e))


