import queue

class Topic:
  def __init__(self, id, old_score, new_score):
    self.id = id
    self.old_score = old_score
    self.new_score = new_score
    self.change = self.new_score - self.old_score
  def __lt__(self, other):
    return self.change > other.change or (self.change == other.change and self.id > other.id)

n = int(input())
pq = queue.PriorityQueue()

def calScore(post, like, comment, share):
  return post*50 + like*5 + comment*10 + share*20
for i in range(n):
  id, old_score, post, like, comment, share = map(int,input().split())
  new_score = calScore(post, like, comment, share)
  topic = Topic(id, old_score, new_score)
  pq.put(topic)

for i in range(5):
  topic = pq.get()
  print(topic.id, topic.new_score)