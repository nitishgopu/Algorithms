
#!/usr/bin/python

class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if(self.root == None):
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if(val < node.v):
            if(node.l != None):
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if(node.r != None):
                self._add(val, node.r)
            else:
                node.r = Node(val)

    def find(self, val):
        if(self.root != None):
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if(val == node.v):
            return node
        elif(val < node.v and node.l != None):
            self._find(val, node.l)
        elif(val > node.v and node.r != None):
            self._find(val, node.r)

    def deleteTree(self):
        # garbage collector will do this for us.
        self.root = None

    def printTree(self):
        if(self.root != None):
            self._printTree(self.root)

    def _printTree(self, node):
        if(node != None):
            self._printTree(node.l)
            print str(node.v) + ' '
            self._printTree(node.r)

#     3
# 0     4
#   2      8
tree = Tree()
tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)
#tree.printTree()
#print (tree.find(3)).v
#print tree.find(10)
#tree.deleteTree()
#tree.printTree()
print "Diameter"
#print tree.getRoot()


def diameter_height(node):
    if node is None:
        return 0, 0
    print "l"
    ld, lh = diameter_height(node.l)
    #print ld,lh
    rd, rh = diameter_height(node.r)
    print "right"
    #print rd,rh
    return max(lh + rh + 1, ld, rd), 1 + max(lh, rh)

def find_tree_diameter(node):
    d, _ = diameter_height(node)
    return d

#print find_tree_diameter(tree.root)


def lowestCommonAncestor(root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """

    if not root:
        return
    elif root.v == p or root.v == q:
        return root.v
    l = lowestCommonAncestor(root.l, p, q)
    r = lowestCommonAncestor(root.r, p, q)
    if l and r:
        return root.v
    else:
        return l or r

ans =  lowestCommonAncestor(tree.root,4,8)
print ans