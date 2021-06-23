INF = 10**9
T = int(input())

def floyd():
  for k in range(M):
    for u in range(M):
      for v in range(M):
        dist[u][v] = min(dist[u][v], dist[u][k] + dist[k][v])

for _ in range(T):
  arr = []
  line = input()
  M = len(line)
  dist = [[INF]*M for _ in range(M)]

  for u in range(M):
     # read input to array
    if u == 0: arr.append(line)
    else: arr.append(input())

    # init dist adjcency matrix
    for v in range(M):
      if u == v: dist[u][v] = 0
      elif arr[u][v] == "Y": dist[u][v] = 1

  floyd()

  person_id = 0
  nFriends = 0
  for u in range(M):
    cnt = 0
    for v in range(M):
      if dist[u][v] == 2: cnt +=1
    if cnt > nFriends:
      nFriends = cnt
      person_id = u
  print(person_id, nFriends)