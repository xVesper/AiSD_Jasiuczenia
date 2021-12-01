from typing import Any, List


class TreeNode:
    def __init__(self, value:Any):
        self.value = value
        self.parent = None
        self.children = []

    def __str__(self):
        return self.value

    def level_of(self):
        lvl = 0
        parent = self.parent
        while parent!=None:
            lvl+=1
            parent = parent.parent
        return lvl



    def is_leaf(self):
        if len(self.children) == 0:
            return True
        else:
            return False

    def add(self, child : 'TreeNode'):
        self.children.append(child)
        child.parent = self

    def for_each_deep_first(self):
        for c in self.children:

            type(self).for_each_deep_first(c)



    def for_each_level_order(self):
        q = Queue()
        for c in self.children:
            q.enqueue(c)

        while len(q)!=0:
            t = q.peek()
            q.dequeue().value
            for c in t.children:
                q.enqueue(c)

    def search(self, value:Any):
        if self.value == value:
            return self
        else:
            q = Queue()
            for c in self.children:
                q.enqueue(c)

            while len(q) != 0:
                t = q.peek()
                comp = q.dequeue()
                if comp.value == value:
                    return comp
                for c in t.children:
                    q.enqueue(c)
            return None

class Tree:
    def __init__(self, root: TreeNode):
        self.root = root

    def add(self, value:Any, parent:Any):
        parent.children.append(TreeNode(value))

    def for_each_level_order(self):
        if type(self) is Tree:
            for c in self.root.children:
                print(c)
                Tree.for_each_level_order(c)
        if type(self) is TreeNode:
            for c in self.children:
                print(c)
                Tree.for_each_level_order(c)


    def for_each_deep_first(self):
        r = self.root
        q = Queue()
        for c in r.children:
            q.enqueue(c)

        while len(q) != 0:
            t = q.peek()
            q.dequeue()
            for c in t.children:
                q.enqueue(c)



    def show(self):
        spacer = "---|"

        if type(self) is Tree:
            print(self.root.value)
            for c in self.root.children:

                print(spacer*c.level_of()+c.value)
                Tree.show(c)
        if type(self) is TreeNode:
            for c in self.children:
                print(spacer*c.level_of()+c.value)
                Tree.show(c)










tf = TreeNode("F")
tb = TreeNode("B") #2
tg = TreeNode("G")#2
ta = TreeNode("A")#3b
td = TreeNode("D")#3b
ti = TreeNode("I")#3g
tc = TreeNode("C")#4d
te = TreeNode("E")#4d
th = TreeNode("H")#ti
tree = Tree(tf)

tf.add(tb)
tf.add(tg)
tb.add(ta)
tb.add(td)
tg.add(ti)
td.add(tc)
td.add(te)
ti.add(th)
# tree.add(69, ti)

# tree.show()
# tree.for_each_deep_first()
tree.show()
