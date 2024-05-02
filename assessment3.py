import unittest
#user input
mathEquation = input("please input your maths equation in format of (X?Y) and this will convert it to a binary tree :) : ")
#reformatting of equation 
mathEquation = mathEquation.replace(' ', '')
postFix = ' '
COUNT = [10]

#creation of class object
class Node:
#initalisation of class object
  def __init__(self, value = None, left = None, right = None, next = None):
    self.value = value
    self.left = left
    self.right = right
    self.next = next
  
def validExpression(expression):
  operands = 0
  operators = 0
  openBrackets = expression.count('(')
  closedBrackets = expression.count(')')
  errorMessage = "Not a valid expression,"
  for thing in expression:
    if thing == "+" or thing == "-" or thing == "/" or thing == "*":
      operators += 1
    elif thing.isdigit() :
      operands += 1
  if openBrackets != closedBrackets:
    errorMessage = errorMessage + " brackets are mismatched,"
  if operators > (operands/2) or operators < (operands/2):
    errorMessage = errorMessage + " wrong amount of operands,"
  if operands % 2 != 0:
    errorMessage = errorMessage + " missing operator."
  print(errorMessage)
  quit()

def print2DUtil(x, space):
 
    # Base case
    if (x == None):
        return
 
    # Increase distance between levels
    space += COUNT[0]
 
    # Process right child first
    print2DUtil(x.right, space)
 
    # Print current node after space
    # count
    print()
    for i in range(COUNT[0], space):
        print(end=" ")
    print(x.value)
 
    # Process left child
    print2DUtil(x.left, space)
 
def print2D(x):
 
    # space=[0]
    # Pass initial space count as 0
    print2DUtil(x, 0)

#function to determine the precedence of operators
def operatorOrder(equation):
  if equation == '/' or equation == '*':
    return 2
  elif equation == '+' or equation == '-':
    return 1
  else:
    return -1

#function to convert user's infix input to a postfix output via use of stacks
def infixOrPostfix(equation):
  result = []
  postfixStack = []
#initialisation of postfix string output
  nodeValues = ' '.join(result)

# iteration through user input
  for i in range(len(mathEquation)):
    equation = mathEquation[i]

#conditional statement checking whether or not value is a digit 0-9
    if equation.isdigit():
      result.append(equation)
    elif equation == '(':
     postfixStack.append(equation)
    elif equation == ')':
#removes brackets from the stack and result
     while postfixStack and postfixStack[-1] != '(':
      result.append(postfixStack.pop())
     postfixStack.pop()
    else:
#sorts the order of which operators and operands are displayed in result
      while postfixStack and (operatorOrder(mathEquation[i]) <= operatorOrder(postfixStack[-1])):
        result.append(postfixStack.pop())
      postfixStack.append(equation)

  while postfixStack:
   result.append(postfixStack.pop())

  print(''.join(result))
  nodeValues = ''.join(result)
#creation of postfix order string

  return nodeValues

 
class Stack:
    def __init__(self):
      self.head = None
 
    def push(self, node):
      if not self.head:
        self.head = node
      else:
        node.next = self.head
        self.head = node
 
    def pop(self):
      if self.head:
        popped = self.head
        self.head = self.head.next
        return popped
      else:
        raise Exception("Stack is empty")

    def top(self):
        return self.head
 
class ExpressionTree:
  def inorder(self, x):
#Base Case
    if not x:
      return
    self.inorder(x.left)
    print(x.value, end=" ")
    self.inorder(x.right)
    return

  def preorder(self, x):
#Base Case
    if not x:
      return
    print(x.value, end=" ")
    self.preorder(x.left)
    self.preorder(x.right)
    return

  def postorder(self, x):
#Base Case
    if not x:
      return
    self.postorder(x.left)
    self.postorder(x.right)
    print(x.value, end=" ")
    return
        
  def breadthFirstTraversal(self, x):
#Base Case
    if not x:
      return
    
    treeQueue = []
    breadthFirst = ' '.join(treeQueue)

    treeQueue.append(x)
    while(len(treeQueue) > 0):
      print(treeQueue[0].value, end =" ")
      node = treeQueue.pop(0)
      
      if node.left is not None:
        treeQueue.append(node.left)
      
      if node.right is not None:
        treeQueue.append(node.right)
    return breadthFirst
       
def main():
  validExpression(mathEquation)
  postfixEquation = infixOrPostfix(mathEquation)
  stack = Stack()
  tree = ExpressionTree()
  for character in postfixEquation:
    if character in "+-*/^":
      root = Node(character)
      print(root.value)
      x = stack.pop()
      print(x.value)
      y = stack.pop()
      root.left = y
      root.right = x
      stack.push(root)
    else:
      stack.push(Node(character))
  print("The Inorder Traversal of Expression Tree: \n", end=" ")
  tree.inorder(stack.top())
  print("The Preorder Traversal of Expression Tree: \n", end=" ")
  tree.preorder(stack.top())
  print("The Postorder Traversal of Expression Tree: \n", end=" ")
  tree.postorder(stack.top())
  print("The Breadth First Traversal of Expression Tree: \n", end=" ")
  tree.breadthFirstTraversal(stack.top())
  print("A visual representation of the tree :) \n", end=" ")
  print2D(stack.top())
    
 
if __name__ == "__main__":
  main()
