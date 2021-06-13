import bisect
T = 0
while True:
  T +=1
  N, Q = map(int, input().split())
  if N ==0 and Q == 0: break
  arr = []
  for i in range(N):
    num = int(input())
    arr.append(num)
  arr.sort()
  print(f"CASE# {T}:")
  for i in range(Q):
    query = int(input())
    pos = bisect.bisect_left(arr, query)
    if (pos >= len(arr) or arr[pos] != query):
      print(f"{query} not found")
    else:
      print(f"{query} found at {pos+1}")
