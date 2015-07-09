# simple binary tree
# in this implementation, a node is inserted between an existing node and the root
import sys

class BinaryTree():

    def __init__(self,rootid):
      self.left = None
      self.right = None
      self.rootid = rootid  #Value

    def getLeftChild(self):
        return self.left
    def getRightChild(self):
        return self.right
    def setNodeValue(self,value):
        self.rootid = value
    def getNodeValue(self):
        return self.rootid

    def insertRight(self,newNode):
        print(self.right)
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.right = self.right
            self.right = tree
        
    def insertLeft(self,newNode):
        print(self.left)
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.left = self.left
            self.left = tree


def printTree(tree):
        if tree != None:
            printTree(tree.getLeftChild())
            print(tree.getNodeValue())
            printTree(tree.getRightChild())
            
            


# test tree

def testTree():
    myTree = BinaryTree("Maud")
    myTree.insertLeft("Bob")
    myTree.insertRight("Tony")
    myTree.insertRight("Steven")
    printTree(myTree)

## Binary Tree
testTree()

t = BinaryTree("Start")
t.insertLeft("LEFT1")
t.insertLeft("LEFT2")
t.insertLeft("LEFT3")
t.insertRight("LEFTs")

print("TEST")
while(True):
    if (t != None):
        print(t.getNodeValue())
        t = t.getLeftChild()
        print("OK")
    else:
        print("BREAK")
        break