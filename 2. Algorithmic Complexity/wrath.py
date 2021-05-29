n = int(input())
L = list(map(int,input().strip().split()))
alive=0
minTemp = n
for i in range(n-1,-1,-1):
    if minTemp>i: 
      alive+=1
    minTemp=min(minTemp,i-L[i])
print(alive)  