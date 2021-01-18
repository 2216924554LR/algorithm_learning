from Tree import *

def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

def postorder(tree):
    if tree:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

def inorder(tree):
    if tree:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())

if __name__ == "__main__":
    r = BinaryTree("a")
    r.insertLeft('b')
    r.insertRight('c')
    r.getRightChild().setRootVal('hello')
    r.getLeftChild().insertRight('d')
    preorder(r)
    print("============")
    r.preorder()