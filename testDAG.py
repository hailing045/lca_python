from unittest import TestCase

from dag import *

class TestDAG(TestCase):

    def test_addNode_Empty(self):
        dag = DAG()
        self.assertRaises(TypeError, lambda: dag.add_node())

    def test_addNode(self):
        dag = DAG()
        dag.add_node('A')
        self.assertTrue(dag.graph == {'A': []})

    def test_addNode_NonExistent(self):
        dag = DAG()
        dag.add_node('B')
        self.assertFalse(dag.graph == {'A': []})

    def test_addNode_Duplicate(self):
        dag = DAG()
        dag.add_node('A')
        self.assertFalse(dag.add_node('A'))

    def test_addEdge(self):
        dag = DAG()
        dag.add_node('A')
        dag.add_node('B')
        self.assertTrue(dag.add_edge('A', 'B') is True)

    def test_addEdge_OneMissing(self):
        dag = DAG()
        dag.add_node('A')
        self.assertRaises(KeyError, lambda: dag.add_edge('A', 'B'))

    def test_addEdge_TwoMissing(self):
        dag = DAG()
        self.assertRaises(KeyError, lambda: dag.add_edge('A', 'B'))

        #        B
        #      /   \
        #     C  -  D

    def test_isAcyclic_No(self):
        dag = DAG()
        dag.add_node('B')
        dag.add_node('C')
        dag.add_node('D')
        dag.add_edge('B', 'C')
        dag.add_edge('C', 'D')
        dag.add_edge('D', 'B')
        self.assertFalse(isAcyclic_wrapper(dag.graph))

    # when graph contains no cycles
    def test_isAcyclic_Yes(self):
        dag = DAG()
        dag.add_node('A')
        dag.add_node('B')
        dag.add_node('C')
        dag.add_node('D')
        dag.add_edge('B', 'C')
        dag.add_edge('B', 'A')
        dag.add_edge('C', 'D')

        #       B
        #     /   \
        #    C     A
        #   /
        #  D

        self.assertTrue(isAcyclic_wrapper(dag.graph))

    # test when the graph is empty
    def test_findLCA_Empty(self):
        dag = DAG()
        self.assertTrue(findLCA(dag.graph, 'A', 'B') is -1)

    # test for one node only
    #       A
    def test_findLCA_OneNode(self):
        dag = DAG()
        dag.add_node('A')
        self.assertTrue(findLCA(dag.graph, 'A', 'B') is -1)

    #       A - B
    def test_findLCA_OneNotInGraph(self):
        dag = DAG()
        dag.add_node('A')
        dag.add_node('B')
        dag.add_edge('A', 'B')
        self.assertTrue(findLCA(dag.graph, 'A', 'G') is -1)

    # test when nodes only
    #       A   B
    def test_findLCA_NoEdge(self):
        dag = DAG()
        dag.add_node('A')
        dag.add_node('B')
        self.assertEqual(findLCA(dag.graph, 'A', 'B'), -1)

    # test for LCA with 2 nodes - one of which is the LCA
    #       A - B
    def test_findLCA_OneNodeIsLCA(self):
        dag = DAG()
        dag.add_node('A')
        dag.add_node('B')
        dag.add_edge('A', 'B')
        self.assertEqual(findLCA(dag.graph, 'A', 'B'), 'A')

    # test for LCA with 2 nodes
    #         A
    #        / \
    #       B   C
    def test_findLCA_BothSides(self):
        dag = DAG()
        dag.add_node('A')
        dag.add_node('B')
        dag.add_node('C')
        dag.add_edge('A', 'B')
        dag.add_edge('A', 'C')
        self.assertEqual(findLCA(dag.graph, 'B', 'C'), 'A')

    # test for findLCA with a cyclic graph
    #        B
    #      /   \
    #     C  -  D
    def test_findLCA_Cyclic(self):
        dag = DAG()
        dag.add_node('B')
        dag.add_node('C')
        dag.add_edge('B', 'C')
        dag.add_node('D')
        dag.add_edge('C', 'D')
        dag.add_edge('D', 'B')
        self.assertEqual(findLCA(dag.graph, 'B', 'C'), -1)


    # test for line graph
    def test_findLCA_LineGraph(self):
        dag = DAG()
        dag.add_node('A')
        dag.add_node('B')
        dag.add_node('C')
        dag.add_node('D')
        dag.add_node('E')
        dag.add_node('F')

        dag.add_edge('A', 'B')
        dag.add_edge('B', 'C')
        dag.add_edge('C', 'D')
        dag.add_edge('D', 'E')
        dag.add_edge('E', 'F')

        #   A
        #    \
        #     B
        #      \
        #       C
        #        \
        #         D
        #          \
        #           E
        #            \
        #             F

        self.assertEqual(findLCA(dag.graph, 'B', 'C'), 'B')
        self.assertEqual(findLCA(dag.graph, 'A', 'F'), 'A')


    # test for LCA with complexed graph
#              A
#          /      \
#         B        C
#       / | \     /  \
#      D  E  F   G    H
#            |          \
#           / \          K
#          I   J

    def test_findLCA_BigGraph(self):
        dag = DAG()
        dag.add_node('A')
        dag.add_node('B')
        dag.add_node('C')
        dag.add_node('D')
        dag.add_node('E')
        dag.add_node('F')
        dag.add_node('G')
        dag.add_node('H')
        dag.add_node('I')
        dag.add_node('J')
        dag.add_node('K')
        dag.add_edge('A', 'B')
        dag.add_edge('A', 'C')
        dag.add_edge('B', 'D')
        dag.add_edge('B', 'E')
        dag.add_edge('B', 'F')
        dag.add_edge('C', 'G')
        dag.add_edge('C', 'H')
        dag.add_edge('H', 'K')
        dag.add_edge('F', 'I')
        dag.add_edge('F', 'J')

        self.assertEqual(findLCA(dag.graph, 'E', 'I'), 'B')
        self.assertEqual(findLCA(dag.graph, 'E', 'H'), 'A')
        self.assertEqual(findLCA(dag.graph, 'A', 'J'), 'A')
        self.assertEqual(findLCA(dag.graph, 'G', 'H'), 'C')
        self.assertEqual(findLCA(dag.graph, 'I', 'J'), 'F')
        self.assertEqual(findLCA(dag.graph, 'K', 'J'), 'I')
        self.assertEqual(findLCA(dag.graph, 'G', 'K'), 'C')
        self.assertEqual(findLCA(dag.graph, 'E', 'J'), 'B')
        self.assertEqual(findLCA(dag.graph, 'G', 'E'), 'A')
        self.assertEqual(findLCA(dag.graph, 'D', 'J'), 'B')
