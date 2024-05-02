# variable obtaining user input math equation
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

#function created for validating user input
def validExpression(expression):
#setting initial values of variables
  operands = 0
  operators = 0
#getting value via use of .count()
  openBrackets = expression.count('(')
  closedBrackets = expression.count(')')
  bracketSet = openBrackets / 2
  totalBrackets = openBrackets - closedBrackets
#setting generic error message
  errorMessage = "Not a valid expression,"
  error = False

#iteration through user input
  for character in expression:
#check to see whether a character is an operator
    if character == "+" or character == "-" or character == "/" or character == "*":
      operators += 1
#check to see whether a character is a number between 0 and 9 via use of .isdigit()
    elif character.isdigit() :
      operands += 1
#for loop to check positioning of operators
  for i in range(1, len(expression)):
#checking whether there are multiple operators in a row via comparison of current character to prior character in the string.
    if expression[i-1] in "+-/*" and expression[i] in "+-/*":
      errorMessage = errorMessage + " 2. wrong amount of operands"
#set error to 'True'
      error = True
#checking if there are mismatched brackets
  if totalBrackets != 0:
    errorMessage = errorMessage + " 1. brackets are mismatched"
#set error to 'True'
    error = True
#checking if there are an uneven amount of numbers
  if operands % 2 != 0:
    errorMessage = errorMessage + " 3. missing operator."
#set error to 'True'
    error = True
#if error is 'True' the errorMessage will be displayed and the program will end
  if error:
    print(errorMessage)
    quit()

#this code's inpsiration was taken from https://www.geeksforgeeks.org/print-binary-tree-2-dimensions/ with alterations to variable and function names.
def printExpressionTree(x, space):
 
    # Base case
    if (x == None):
        return
 
    # to increase the distances between each level
    space += COUNT[0]
 
    # working with the right value first
    printExpressionTree(x.right, space)
 
    #spacing current node by placing spaces before printing current node
    print()
    for i in range(COUNT[0], space):
        print(end=" ")
    print(x.value)
 
    # working with the left value
    printExpressionTree(x.left, space)

#this code's inpsiration was taken from https://www.geeksforgeeks.org/print-binary-tree-2-dimensions/ with alterations to variable and function names.
def getPrintExpressionTree(x):
    #passing the current node value with an initial space value as '0'
    printExpressionTree(x, 0)

#function to determine the precedence of operators
def operatorOrder(equation):
  if equation == '/' or equation == '*':
    return 2
  elif equation == '+' or equation == '-':
    return 1
  else:
    return -1

#function to convert user's infix input to a postfix output via use of stacks
#this function to convert infix to postfix has taken inspiration from https://www.geeksforgeeks.org/convert-infix-expression-to-postfix-expression/ with alterations to if statement conditions, variable names, and some other code to tailor this to the assessment 2 requirements.
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

#adds anything left within postfixStack to result
  while postfixStack:
   result.append(postfixStack.pop())

#creating nodeValues string via use of .join()
  nodeValues = ''.join(result)

  return nodeValues

 
class Stack:
#This code's inspiration was drawn from https://www.geeksforgeeks.org/expression-tree/ with alterations to variable names and additional code.
    def __init__(self):
      self.head = None

#push function to add an element to the top of the stack
    def push(self, node):
      if not self.head:
        self.head = node
      else:
        node.next = self.head
        self.head = node

#pop function to remove the top element of the stack
    def pop(self):
      if self.head:
        popped = self.head
        self.head = self.head.next
        return popped
      else:
        raise Exception("Stack is empty")

#returns the head(root node) of the stack
    def top(self):
        return self.head
 
class ExpressionTreeTraversal:
#This class's code inspiration was drawn from https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/ with alterations to variable names.
  def inorder(self, x):
#Base Case
    if not x:
      return
#displays nodes in order of left, root, and right node
    self.inorder(x.left)
    print(x.value, end=" ")
    self.inorder(x.right)
    return

  def preorder(self, x):
#Base Case
    if not x:
      return
#displays nodes in order of root, left, and right node
    print(x.value, end=" ")
    self.preorder(x.left)
    self.preorder(x.right)
    return

  def postorder(self, x):
#Base Case
    if not x:
      return
#displays nodes in order of left, right, and root node
    self.postorder(x.left)
    self.postorder(x.right)
    print(x.value, end=" ")
    return

#function which traverses expression tree by each entire level of the tree        
  def breadthFirstTraversal(self, x):
#Base Case
    if not x:
      return
    
    treeQueue = []
#creation of breadthFirst string via use of .join to add the treeQueue values
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

#This code's inspiration was drawn from https://www.geeksforgeeks.org/expression-tree/ with alterations to variable names and additional code to tailor to assessment requirements.
def main():
#calling expression validation function
  validExpression(mathEquation)
#setting postfixEquation to the result of infixOrPostfix()
  postfixEquation = infixOrPostfix(mathEquation)
  stack = Stack()
#setting treeTraversal to the result of ExpressionTreeTraversal()
  treeTraversal = ExpressionTreeTraversal()
#creating expression tree via use of a for loop and a stack
  for character in postfixEquation:
#if statement contained within for loop which sets the root nodes to each listed operator
    if character in "+-*/^":
      root = Node(character)
      x = stack.pop()
      y = stack.pop()
      root.left = y
      root.right = x
      stack.push(root)
    else:
      stack.push(Node(character))

#printing of each version of traversal via use of treeTraversal class functions
  print("The Inorder Traversal of Expression Tree: ", end=" ")
  treeTraversal.inorder(stack.top())
  print("\n The Preorder Traversal of Expression Tree: ", end=" ")
  treeTraversal.preorder(stack.top())
  print("\n The Postorder Traversal of Expression Tree: ", end=" ")
  treeTraversal.postorder(stack.top())
  print("\n The Breadth First Traversal of Expression Tree: ", end=" ")
  treeTraversal.breadthFirstTraversal(stack.top())
  print("\n A visual representation of the tree :) \n", end=" ")
  getPrintExpressionTree(stack.top())
    

#conditional statement to call main() to promote reusability of code
if __name__ == "__main__":
  main()
