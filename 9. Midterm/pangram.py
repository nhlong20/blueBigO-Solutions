n = int(input())
sentance = input()

if n < 25:
  print("NO")
  exit(0)

sent = sentance.lower()

visited = [False]*25

for character in sent:
  id = ord(character) - 98
  visited[id] = True
print("NO") if False in visited else print("YES")