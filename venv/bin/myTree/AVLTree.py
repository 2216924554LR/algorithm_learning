from BinSearchTree import *

class AVLTree(BinarySearchTree):
    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent = currentNode)
                self.updateBalance(currentNode.leftChild)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent = currentNode)
                self.updateBalance(currentNode.rightChild)

    def updateBalance(self, node):
        if abs(node.balanceFactor) > 1:
            self.reBalance(node)
            return
        if node.parent is not None:
            if node.isLeftChild():
                node.parent.balanceFactor += 1
            elif node.isRightChild():
                node.parent.balanceFactor -= 1
            if node.parent.balanceFactor != 0:
                self.updateBalance(node.parent)

    # the right tree is heavier than the left tree.
    def rotateLeft(self, rotRoot):
        # The new root node is the rightChild of the original root node
        newRoot = rotRoot.rightChild
        rotRoot.rightChild = newRoot.leftChild
        if newRoot.leftChild is not None:
            newRoot.leftChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
        newRoot.leftChild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor + \
                                1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = rotRoot.balanceFactor + \
                                1 + max(rotRoot.balanceFactor, 0)

    def rotateRight(self, rootRoot):
        pass



    def reBalance(self, node):
        if node.balanceFactor < 0:
            if node.rightChild.balanceFactor > 0:
                self.rotateRight(node.rightChild)
                self.rotateLeft(node)
            else:
                self.rotateLeft(node)
        elif node.balanceFactor > 0:
            if node.rightChild.balanceFactor < 0:
                self.rotateLeft(node.rightChild)
                self.rotateRight(node)
            else:
                self.rotateRight(node)


