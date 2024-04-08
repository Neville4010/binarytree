#Write your program here 👇👇
class Node:
   def __init__(self, val, left = None, right = None):
      self.val = val
      self.left = left
      self.right = right
    
ADD = "+"
MINUS = "-"
MULTIPLY = "*"
DIVIDE = "/"

def evaluate(root):
   if root.val == ADD:
      return evaluate(root.left) + evaluate(root.right)
   elif root.val == MINUS:
      return evaluate(root.left) - evaluate(root.right)
   elif root.val == MULTIPLY:
      return evaluate(root.left) * evaluate(root.right)
   else:
      return root.val

def insert(root, val):
   if root is None:
      return Node(val)
   else:
      if root.val == val:
         return root
      elif root.val < val:
         root.right = insert(root.right, val)
      else:
         root.left = insert(root.left, val)
   return root

print(evaluate(tree))
