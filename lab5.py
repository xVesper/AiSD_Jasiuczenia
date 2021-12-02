from typing import Any, Callable


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value):
        self.value = value
        self.right_child = None
        self.left_child = None

    def is_leaf(self):
        if not self.left_child and not self.right_child:
            return True
        return False

    def add_left_child(self, value: Any):
        self.left_child = BinaryNode(value)

        return self.left_child

    def add_right_child(self, value: Any):
        self.right_child = BinaryNode(value)

        return self.right_child

    def traverse_in_order(self, visit: Callable[[Any], None]):
        if self.left_child:
            self.left_child.traverse_in_order(visit)

        visit(self)

        if self.right_child:
            self.right_child.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]):
        if self.left_child:
            self.left_child.traverse_post_order(visit)

        if self.right_child:
            self.right_child.traverse_post_order(visit)

        visit(self)

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        visit(self)

        if self.left_child:
            self.left_child.traverse_pre_order(visit)

        if self.right_child:
            self.right_child.traverse_pre_order(visit)

    def __str__(self):
        return self.value

class BinaryTree:
    root: BinaryNode

    def __init__(self, value):
        self.root = BinaryNode(value)

    def traverse_in_order(self, visit: Callable[[Any], None]):
        self.root.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]):
        self.root.traverse_post_order(visit)

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        self.root.traverse_pre_order(visit)

    def show(self):
        obj = {}

        def show_visit(node):
            if not node.is_leaf():
                obj[node] = {}
                obj[node]['children'] = [node.left_child, node.right_child]

        tree.traverse_pre_order(show_visit)
        print(obj)

        for node_parent in obj:
            if not obj[node_parent]['node']:
                obj[node_parent]['node'] = Node(node_parent.value)

            for child in obj[node_parent]['children']:
                node_child = Node(node_parent.value)

                if not obj[node_parent]['node']:
                    obj[node_parent]['node'] =

tree = BinaryTree(10)
child_9 = tree.root.add_left_child(9)
child_9_1 = child_9.add_left_child(1)
child_9_3 = child_9.add_right_child(3)

child_2 = tree.root.add_right_child(2)
child_2_4 = child_2.add_left_child(4)
child_2_6 = child_2.add_right_child(6)

assert tree.root.value == 10
assert tree.root.right_child.value == 2
assert tree.root.right_child.is_leaf() is False
assert tree.root.left_child.left_child.value == 1
assert tree.root.left_child.left_child.is_leaf() is True

tree.show()