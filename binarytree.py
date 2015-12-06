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
        #print(self.right)
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.right = self.right
            self.right = tree
        
    def insertLeft(self,newNode):
        #print(self.left)
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.left = self.left
            self.left = tree
            
    def insertLeftFrom(self, fromNode, newNode):
        if self.rootid == fromNode: # First Node
            self.insertLeft(newNode);
        else:
            self.findNode(fromNode).insertLeft(newNode)
            
    def insertRightFrom(self, fromNode, newNode):
        if self.rootid == fromNode: # First Node
            self.insertRight(newNode);
        else:
            self.findNode(fromNode).insertRight(newNode)
        
    def findNode(self, nodeName):
        self.treeStore = None
        self._findNode(self.left, nodeName)
        self._findNode(self.right, nodeName)
        return self.treeStore if self.treeStore != None else False;
    
    def _findNode(self, tree, nodeName):
        if tree != None:
            if tree.rootid == nodeName:
                self.treeStore = tree;
                return True;
        else:
            return False;
        self._findNode(tree.left, nodeName)
        self._findNode(tree.right, nodeName)
            
def printTree2(tree, txt="C>"):
    if tree!=None:
        printTree2(tree.getLeftChild(), txt+"L>")
        print(txt +"  "+tree.getNodeValue())
        printTree2(tree.getRightChild(),txt+"R>")

# test tree
def testTree():
    print "Create Tree"
    # Facing Point
    t = BinaryTree("LPT6101")
    t.insertLeftFrom("LPT6101", "LTF6103a")
    t.insertRightFrom("LPT6101", "LTF6103")
    t.insertLeftFrom("LTF6103a", "LTF6103a_1")
    t.insertLeftFrom("LTF6103a_1", "LTF6103a_2")
    # Facing Point
    t.insertLeftFrom("LTF6103a_2", "LPT6102")
    t.insertLeftFrom("LPT6102", "LTF6111a")
    t.insertRightFrom("LPT6102", "LTF6111")
    # Facing Point
    t.insertRightFrom("LTF6103", "LPT6103")
    t.insertLeftFrom("LPT6103", "LTF6133a")
    t.insertRightFrom("LPT6103", "LTF6133")
    print "Print Tree"
    printTree2(t)

# testTree()

