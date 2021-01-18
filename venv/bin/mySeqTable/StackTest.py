from StackDemo import *

# s = Stack()
#
# s.show()
# s.push('cat')
# s.push('dog')
# s.push('hello')
# print(s.peek())
# print(s.pop())
#
# print(s.is_empty())

def bracketMatch(brackets):
    s = []
    for b in brackets:
        if b == '(':
            s.append(b)
        else:
            if s:
                s.pop()
            else:
                return False
    return len(s) == 0

print(bracketMatch("((()()())())"))