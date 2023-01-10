import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_agraph import write_dot, graphviz_layout


class Vertex:

    def __init__(self, value):
        self.__value = value
        self.__left = None
        self.__right = None
        self.__height = 1

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left):
        self.__left = left

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right):
        self.__right = right

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height


class AVLTree(object):
    def __init__(self) -> None:
        self.__root = None

    @property
    def root(self):
        return self.__root

    @root.setter
    def root(self, root):
        self.__root = root

    def get_height(self, root):
        '''Method returng height of root with some sequred cases'''
        if root is None:
            return 0
        return root.height

    def get_balance_factor(self, root):
        '''Method returning root balance factor'''
        if root is None:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def right_rotation(self, root):
        '''Method providing left rotation'''
        child = root.left
        root.left = child.right
        child.right = root

        root.height = self.height_update(root)
        child.height = self.height_update(child)

        return child

    def left_rotation(self, root):
        '''Method providing right rotation'''
        child = root.right
        root.right = child.left
        child.left = root

        root.height = self.height_update(root)
        child.height = self.height_update(child)

        return child

    def insert(self, root, value):
        '''Method inserting new node into tree'''
        if root is None:
            return Vertex(value)

        if value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        root.height = self.height_update(root)

        balance_factor = self.get_balance_factor(root)

        if balance_factor > 1:
            if value < root.left.value:
                return self.right_rotation(root)
            else:
                root.left = self.left_rotation(root.left)
                return self.right_rotation(root)

        if balance_factor < -1:
            if value > root.right.value:
                return self.left_rotation(root)
            else:
                root.right = self.right_rotation(root.right)
                return self.left_rotation(root)

        return root

    def height_update(self, root):
        '''Method updating node heaight'''
        return max(self.get_height(root.left),
                   self.get_height(root.right)) + 1

    def minvalueNode(self, root):
        '''Method searching for minimal value Node'''
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    # deleting wents wrong
    def delete(self, root, value):
        '''Method deleting Node from tree where root is starting point 
        of iterations and value is searching value'''
        if root is None:
            return root

        # BST logic
        if value < root.value:
            root.left = self.delete(root.left, value)
        elif value > root.value:
            root.tight = self.delete(root.right, value)
        else:
            if (root.left is None) or (root.right is None):
                temp = None
                if root.left is None:
                    temp = root.right
                else:
                    temp = root.left
                if temp is None:
                    temp = root
                    root = None
                else:
                    root = temp
            else:
                temp = self.minvalueNode(root.right)
                root.value = temp.value
                root.right = self.delete(root.right, temp.value)

        if root is None:
            return root

        # Update Height
        root.height = self.height_update(root)
        # Re-balance if needed
        balance_factor = self.get_balance_factor(root)

        # Balance the tree
        if balance_factor > 1:
            if self.get_balance_factor(root.left) >= 0:
                return self.right_rotation(root)
            else:
                root.left = self.left_rotation(root.left)
                return self.right_rotation(root)
        if balance_factor < -1:
            if self.get_balance_factor(root.right) <= 0:
                return self.left_rotation(root)
            else:
                root.right = self.right_rotation(root.right)
                return self.left_rotation(root)

        return root

    def convert_to_nxGraph(self, root, graph):
        '''Assisting method for print method to convert tree to networkx Graph'''
        if root.left is not None:
            graph.add_edge(root.value, root.left.value)
            self.convert_to_nxGraph(root.left, graph)

        if root.right is not None:
            graph.add_edge(root.value, root.right.value)
            self.convert_to_nxGraph(root.right, graph)

    # Print the tree
    def print(self, root):
        '''Method printing tree'''
        graph = nx.Graph()
        self.convert_to_nxGraph(root, graph)

        pos = graphviz_layout(graph, prog='dot')
        nx.draw(graph, pos, with_labels=True)

        plt.show()


if __name__ == "__main__":
    myTree = AVLTree()
    nums = [33, 13, 52, 9, 21, 61, 8, 11]
    for num in nums:
        myTree.root = myTree.insert(myTree.root, num)
    myTree.root = myTree.delete(myTree.root, 13)
    myTree.print(myTree.root)
