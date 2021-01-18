from Tree import *
import operator

def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = []
    eTree = BinaryTree('')
    pStack.append(eTree)
    currentTree = eTree
    for i in fplist:
        # print(i)
        if i == '(':
            currentTree.insertLeft('')
            pStack.append(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in '+-*/)':
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in '+=*/':
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.append(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise  ValueError
    return eTree

def evaluate(parseTree):
    opers = {'+':operator.add, '-':operator.sub,
             '*':operator.mul, '/':operator.truediv}
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()
    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC))
    else:
        return parseTree.getRootVal()

def printexp(tree):
    sVal = ""
    if tree:
        if tree.rightChild and tree.leftChild:
            sVal = '(' +printexp(tree.getLeftChild())
            sVal = sVal + str(tree.getRootVal())
            sVal = sVal + printexp(tree.getRightChild()) + ')'
        else:
            sVal = printexp(tree.getLeftChild())
            sVal = sVal + str(tree.getRootVal())
            sVal = sVal + printexp(tree.getRightChild())

    return sVal

if __name__ == '__main__':
    parse = '( ( 3 + 4 ) * 5 )'
    t = buildParseTree(parse)
    print(t.getRootVal())
    print(evaluate(t))
    print(printexp(t))