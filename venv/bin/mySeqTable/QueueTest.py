from QueueDemo import *

q = Queue()

print(q.is_empty())
for i in range(5):
    q.enqueue(i)

for i in range(5):
    print(q.dequeue())