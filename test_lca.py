from unittest import TestCase

from lca import *

class TestLCA(TestCase):

#test for null
 def test_nodeInitEmpty(self):
    node = Node()
    self.assertEqual(node.key, None)

# key and comparison equal
 def test_nodeInitTrue(self):
    node = Node(6)
    self.assertTrue(node.key == 6)

# key and comparison not equal
 def test_nodeInitFalse(self):
    node = Node(6)
    self.assertFalse(node.key == 8)


#test for findPath
#when tree is test_nodeInitEmpty
 def test_findPathEmpty(self):
    path = []
    root = Node()
    self.assertEqual(findPath(root, path, 6), False)

#test invalid position in the Tree
 def test_findPathNotInTree(self):
    path = []
    root = Node(1)
    self.assertEqual(findPath(root, path, 5), False)

#test the node in the Tree
 def test_findPathRoot(self):
    path = []
    root = Node(1)
    self.assertEqual(findPath(root, path, 1), True)

#test a tree
 def test_findPath(self):
    path = []
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)


    self.assertEqual(findPath(root, path, 1), True)
    self.assertEqual(findPath(root, path, 3), True)

    self.assertEqual(findPath(root, path, 6), True)
    self.assertEqual(findPath(root, path, 10), False)



#test for findLCA
#when empty
 def test_findLCAEmpty(self):
    root = Node()
    path = []
    self.assertEqual(findLCA(root, 1, 2), -1)

 def test_findLCANotInTree(self):
    root = Node(1)
    self.assertEqual(findLCA(root, 1, 5), -1)

# test for only root,which is the lca to itself
 def test_findLCARoot(self):
    root = Node(1)
    path = []
    self.assertEqual(findLCA(root, 1, 1), 1)

# test for complete tree
 def test_findLCA(self):
    root = Node(1)
    root.left = Node(2)
    root.right = Node(6)
    root.left.left = Node(3)
    root.left.left.right = Node(4)
    root.left.left.right.right = Node(5)
    root.left.right = Node(9)
    root.right.right = Node(7)
    root.right.right.right = Node(8)

    self.assertEqual(findLCA(root, 8, 5), 1)
    self.assertEqual(findLCA(root, 4, 9), 2)
    self.assertEqual(findLCA(root, 6, 7), 6)
