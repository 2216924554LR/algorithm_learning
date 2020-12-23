class Queue:
    def __init__(self):
        self.__queue = []

    def enqueue(self, item):
        self.__queue.append(item)

    def dequeue(self):
        return self.__queue.pop(0)

    def is_empty(self):
        return self.__queue == []

    def size(self):
        return len(self.__queue)
