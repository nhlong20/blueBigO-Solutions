t = int(input())

for _ in range(t):
  n, m = map(int, input().split())
  l = list(map(int, input().split()))
  s = set()
  for el in l[:n]:
    s.add(el)
  for el in l[n:]:
    print("YES") if el in s else print("NO")
    s.add(el)
