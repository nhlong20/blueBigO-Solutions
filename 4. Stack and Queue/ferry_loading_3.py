import queue

class Car:
  def __init__(self, id, arrivalTime):
      self.id = id
      self.arrivalTime = arrivalTime
  

test_case = int(input())
while (test_case):
  test_case -= 1
  N, T, M = map(int, input().strip().split())
  
  # init 2 queues
  qSide = [[], []]
  qSide[0] = queue.Queue()
  qSide[1] = queue.Queue()
  res = [0]*(10**5 +1) # this is an array to store arrival time of the car

  # add car to qSide queue
  for i in range(M):
    arrivalTime, side = input().split()
    if side == "left":
      qSide[0].put(Car(i, int(arrivalTime)))
    else:
      qSide[1].put(Car(i, int(arrivalTime)))
  
  curSide, curTime, nextTime = 0, 0, 0
  waiting = (not qSide[0].empty()) + (not qSide[1].empty())

  # check if there is car in queue
  while waiting:
    if waiting == 1:
      if qSide[0].empty():
        nextTime = qSide[1].queue[0].arrivalTime
      else:
        nextTime = qSide[0].queue[0].arrivalTime
    else:
      nextTime = min(qSide[0].queue[0].arrivalTime,qSide[1].queue[0].arrivalTime)
    
    curTime = max(curTime, nextTime)
    carried = 0

    # load the car into the ferry
    while not qSide[curSide].empty():
      car = qSide[curSide].queue[0]
      if car.arrivalTime <= curTime and carried < N:
        res[car.id] = curTime + T
        carried += 1
        qSide[curSide].get()
      else:
        break
    
    curTime += T # add time needed for the ferry to move to the other bank
    curSide = 1 - curSide # change the side of the bank

    # update waiting to prevent infinity loop
    waiting = (not qSide[0].empty()) + (not qSide[1].empty())

  # after transport all the car
  for i in range(M):
    print(res[i])
  if test_case:
    print()
