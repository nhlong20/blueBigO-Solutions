n=int(input())
l=list(map(int,input().strip().split()))[:n]

a= sorted(l)[::-1]
for el in l:
  print(a.index(el)+1, end=" ")