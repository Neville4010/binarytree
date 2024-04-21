#Write your program here 👇👇
class Node:
    def __init__(self,x):
        self.key = x
        self.left = None
        self.right = None
        self.parent = None

ADD = "+"
MINUS = "-"
MULTIPLY = "*"
DIVIDE = "/"

class BST:
    def __init__(self):
        self.root = None

    def BSTsearch(self,k):

        x = self.root
        while x!=None and x.key!=k:
            if k<x.key:
                x=x.left
            else:
                x=x.right
        return x

    def BSTinsert(self, z):

        x = self.root
        y = None
        while x != None:
            y=x
            if z.key<x.key:
                x=x.left
            else:
                x=x.right
        z.p=y
        if y==None:
            self.root=z
        else:
            if z.key<y.key:
                y.left=z
            else:
                y.right=z

    def bstDelete(self, z):

        if z.left == None and z.right == None:
            if z == self.root:
                self.root = None
            else:
                if z == z.p.left:
                    z.p.left = None
                else:
                    z.p.right = None
        elif z.left != None and z.right != None:
            y = self.bstMinimum(z.right)
            z.key = y.key
            self.bstDelete(y)
        else:
            if z.left != None:
                z.left.p=z.p
                if z==self.root:
                    self.root=z.left
                else:
                    if z==z.p.left:
                        z.p.left=z.left
                    else:
                        z.p.right=z.left
            else:
                z.right.p=z.p
                if z==self.root:
                    self.root=z.right
                else:
                    if z==z.p.left:
                        z.p.left=z.left
                    else:
                        z.p.right=z.left

    def bstMinimum(self, x):

        while x.left != None:
            x = x.left
        return x

    def BSTinOrder(self, x):

        if x == None: return
        self.BSTinOrder(x.left)
        print(x.key)
        self.BSTinOrder(x.right)

    def bstGetRoot(self):
        return self.root
    
    def evaluate(root):
      if root.val == ADD:
        return evaluate(root.left) + evaluate(root.right)
      elif root.val == MINUS:
        return evaluate(root.left) - evaluate(root.right)
      elif root.val == MULTIPLY:
        return evaluate(root.left) * evaluate(root.right)
      else:
        return root.val

    def print_tree(self, root, val="val", left="left", right="right"):
        def display(root, val=val, left=left, right=right):
            """Returns list of strings, width, height, and horizontal coordinate of the root."""
            # No child.
            if getattr(root, right) is None and getattr(root, left) is None:
                line = '%s' % getattr(root, val)
                width = len(line)
                height = 1
                middle = width // 2
                return [line], width, height, middle

            # Only left child.
            if getattr(root, right) is None:
                lines, n, p, x = display(getattr(root, left))
                s = '%s' % getattr(root, val)
                u = len(s)
                first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
                second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
                shifted_lines = [line + u * ' ' for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

            # Only right child.
            if getattr(root, left) is None:
                lines, n, p, x = display(getattr(root, right))
                s = '%s' % getattr(root, val)
                u = len(s)
                first_line = s + x * '_' + (n - x) * ' '
                second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
                shifted_lines = [u * ' ' + line for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

            # Two children.
            left, n, p, x = display(getattr(root, left))
            right, m, q, y = display(getattr(root, right))
            s = '%s' % getattr(root, val)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
            second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
            if p < q:
                left += [n * ' '] * (q - p)
            elif q < p:
                right += [m * ' '] * (p - q)
            zipped_lines = zip(left, right)
            lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
            return lines, n + m + u, max(p, q) + 2, n + u // 2

        lines, *_ = display(root, val, left, right)
        for line in lines:
            print(line)

tree = BST()
tree.BSTinsert(Node(ADD))
tree.BSTinsert(Node(3))
tree.BSTinsert(Node(7))
tree.BSTinsert(Node(2))
tree.BSTinsert(Node(4))
tree.BSTinsert(Node(9))

#tree.BSTinOrder(tree.bstGetRoot())

tree.print_tree(tree.bstGetRoot(), val="key")