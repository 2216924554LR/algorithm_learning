# Use list to implement stacks

class Stack:
    def __init__(self, item=None):
        if item:
            self.__myList = [item]
        else:
            self.__myList = []

    def push(self, item):
        self.__myList.append(item)

    def pop(self):
        return self.__myList.pop()

    def peek(self):
        if self.__myList:
            return self.__myList[-1]
        else:
            print("This is an empty stack")
            return None

    def show(self):
        print(self.__myList)

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.__myList)

