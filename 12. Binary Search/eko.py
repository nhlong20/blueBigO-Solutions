def binarySearch(arr, l, r, x):
  ans = r
  while(l <= r):
    height = l + (r-l)//2
    nWoods =  countAmountOfCutWoods(arr, height)
    if nWoods >= x:
      ans = height
      l = height + 1
    else:
      r = height -1
  return ans

def countAmountOfCutWoods(arr, cut_height):
  sum = 0
  for height in arr:
    if(height - cut_height < 0): continue
    sum += height - cut_height
  return sum


n, h = map(int, input().split())
arr = list(map(int, input().strip().split()))[:n]

print(binarySearch(arr, 0, max(arr), h))
      
