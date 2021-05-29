N, K = map(int, input().strip().split())
a = list(map(int, input().strip().split()))
L = R = 0
fre = [0]*(10**5+1)
i = j = count = 0
while i < N:
  fre[a[R]] += 1 # increment frequency of current number in a by one
  if fre[a[R]] == 1: # this mean a[R] exist for the first time
    count +=1
  if count == K: break
  i += 1
  R +=1
if count < K:
  print("-1 -1")
  exit(0)
while j < N:
  fre[a[L]] -=1
  if fre[a[L]] == 0:
    count -=1
  if count < K: break
  j +=1
  L +=1

print(L+1,R+1)