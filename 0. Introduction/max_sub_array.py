# find max sum in this array [−1 2 4 −3 5 2 −5 2]
array = [-1,2,4,-3,5,2,-5,2]

# Solution 1:
best = 0
for i in range(len(array)):
  sum = 0
  for j in range(i, len(array), 1):
    sum += array[j]
    best = max(best, sum)
print("Solution 1:",best)

# Solution 2:
best, sum = 0, 0
for el in array:
  sum = max(el, sum + el)
  best = max(best, sum)
print("Solution 2:",best)