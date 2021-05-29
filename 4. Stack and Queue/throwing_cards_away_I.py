import queue
def main():
  while True:
    n = int(input())
    if n == 0: break
    q = queue.Queue()
    discarded_cards = []
    remaining_card = -1
    for i in range(n):
      q.put(i+1)
    while q.qsize() > 1:
      discarded_cards.append(q.get())
      q.put(q.get())
    remaining_card = q.get()
    print("Discarded cards:", end="")
    for order in range(len(discarded_cards)-1):
      print(f" {discarded_cards[order]},", end="")
    if len(discarded_cards): 
      print(f" {discarded_cards[-1]}")
    else: print()
    print(f"Remaining card: {remaining_card}")
if __name__ == '__main__':
  main()
