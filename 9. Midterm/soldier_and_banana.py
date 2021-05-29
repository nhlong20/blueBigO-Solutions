k, n, w = map(int, input().split())

sum = 0
for i in range(1,w+1):
  sum += i*k
  
print(0) if n> sum else print(sum -n)