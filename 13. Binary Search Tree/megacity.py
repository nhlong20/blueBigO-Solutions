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
expaned = 0
for r in nRadius:
  expaned += S[r]
  if expaned >= need:
    print(r)
    break
if expaned < need: print(-1)