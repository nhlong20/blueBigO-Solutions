from math import sqrt
MILLION = 10**6
n, nPopulation = map(int,input().split())

need = MILLION - nPopulation

S = dict()
nRadius = []
for _ in range(n):
  x, y, k = map(int,input().split())
  r = sqrt(x*x + y*y)
  if r in S: S[r] += k
  else: 
    S[r] = k
    nRadius.append(r)

nRadius.sort()
expanded = 0
for r in nRadius:
  expanded += S[r]
  if expanded >= need:
    print(r)
    break
if expanded < need: print(-1)