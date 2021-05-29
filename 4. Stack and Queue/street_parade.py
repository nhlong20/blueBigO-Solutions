import queue

def isOrderableStreet(trucks):
  s = []
  need = 1; state = True
  for truck in trucks:
    while(len(s) != 0 and s[-1] == need):
      need += 1
      s.pop()
    if truck == need:
      need += 1
    elif(len(s) != 0 and s[-1] < truck):
      state = False
      break
    else:
      s.append(truck)
  if(state): return "yes"
  return "no"

def main():
  while True:
    n = int(input())
    if n == 0: break
    trucks = list(map(int, input().strip().split()))
    print(isOrderableStreet(trucks))

if __name__ == '__main__':
  main()
