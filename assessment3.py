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

print(evaluate(tree))
