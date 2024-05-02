#user input
mathEquation = input("please input your maths equation in format of (X?Y) and this will convert it to a binary tree :) : ")
#reformatting of equation 
mathEquation = mathEquation.replace(' ', '')
postFix = ' '
COUNT = [10]
#creation of class object

#creation of class object
class Node:
#initalisation of class object
  def __init__(self, value = None, left = None, right = None, next = None):
    self.value = value
    self.left = left
    self.right = right
    self.next = next

def print2DUtil(root, space):
 
    # Base case
    if (root == None):
        return
 
    # Increase distance between levels
    space += COUNT[0]
 
    # Process right child first
    print2DUtil(root.right, space)
 
    # Print current node after space
    # count
    print()
    for i in range(COUNT[0], space):
        print(end=" ")
    print(root.value)
 
    # Process left child
    print2DUtil(root.left, space)
 
def print2D(root):
 
    # space=[0]
    # Pass initial space count as 0
    print2DUtil(root, 0)

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
  def inorder(self, root):
#Base Case
    if not root:
      return
    self.inorder(root.left)
    print(root.value, end=" ")
    self.inorder(root.right)
    return

  def preorder(self, root):
#Base Case
    if not root:
      return
    print(root.value, end=" ")
    self.preorder(root.left)
    self.preorder(root.right)
    return

  def postorder(self, root):
#Base Case
    if not root:
      return
    self.postorder(root.left)
    self.postorder(root.right)
    print(root.value, end=" ")
    return
        
  def breadthFirstTraversal(self, root):
#Base Case
    if not root:
      return
    
    treeQueue = []
    breadthFirst = ' '.join(treeQueue)

    treeQueue.append(root)
    while(len(treeQueue) > 0):
      print(treeQueue[0].value, end =" ")
      node = treeQueue.pop(0)
      
      if node.left is not None:
        treeQueue.append(node.left)
      
      if node.right is not None:
        treeQueue.append(node.right)
    return breadthFirst
          
def main():
    postfixEquation = infixOrPostfix(mathEquation)
    stack = Stack()
    tree = ExpressionTree()
    for character in postfixEquation:
        if character in "+-*/^":
            z = Node(character)
            print(z.value)
            root = stack.pop()
            print(root.value)
            y = stack.pop()
            print(y.value)
            z.left = y
            z.right = root
            stack.push(z)
        else:
            stack.push(Node(character))
    print("The Inorder Traversal of Expression Tree: ", end=" ")
    tree.inorder(stack.top())
    print("The Preorder Traversal of Expression Tree: ", end=" ")
    tree.preorder(stack.top())
    print("The Postorder Traversal of Expression Tree: ", end=" ")
    tree.postorder(stack.top())
    print("The Breadth First Traversal of Expression Tree: ", end=" ")
    tree.breadthFirstTraversal(stack.top())
    print("A visual representation of the tree :) ", end=" ")
    print2D(stack.top())
    
 
if __name__ == "__main__":
  main()
