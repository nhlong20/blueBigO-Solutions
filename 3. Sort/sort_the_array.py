n = int(input())
a = list(map(int,input().strip().split()))

L = 0
while L < n-1 and a[L] < a[L+1]:
  L +=1
R = L
while R < n-1 and a[R] > a[R+1]:
  R +=1

rArr = a[:L] + a[L:R+1][::-1] + a[R+1:]
if rArr == sorted(rArr):
  print("yes")
  print (1,1) if L == R else print(L+1, R+1)
else:
  print("no")