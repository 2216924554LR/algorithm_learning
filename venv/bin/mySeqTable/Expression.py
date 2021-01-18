# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 10:50:01 2020

@author: 22169
"""

def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = []
    postfixList = []
    tokenList = list(infixexpr)
    
    for token in tokenList:
        if token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.append(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not len(opStack) == 0 ) and (prec[opStack[-1]] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.append(token)
    while not len(opStack) == 0:
        postfixList.append(opStack.pop())
    return "".join(postfixList)

def postfixEval(postfixExpr):
    operandStack = []
    tokenList = list(postfixExpr)
    
    for token in tokenList:
        if token in "0123456789":
            operandStack.append(token)
        else:
            op1 = operandStack.pop()
            op2 = operandStack.pop()
            result = eval(op1 + token + op2)
            operandStack.append(str(result))
    return int(operandStack.pop())
    

if __name__ == "__main__":
    infix = "(1+2)*(3+4)"
    postfix = infixToPostfix(infix)
    print(postfix)
    print(postfixEval(postfix))
    
                


