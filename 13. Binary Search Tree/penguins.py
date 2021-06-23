penguins = {"Emperor Penguin": 0, "Little Penguin":0,"Macaroni Penguin":0}

n = int(input())
for _ in range(n):
  penguin = input()
  penguins[penguin] +=1

ans = ""
maxP = 0
for penguin in penguins:
  if penguins[penguin] > maxP:
    maxP = penguins[penguin]
    ans = penguin

print(ans)