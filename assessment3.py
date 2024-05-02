#user input
mathEquation = input("please input your maths equation in format of (X?Y) and this will convert it to a binary tree :) : ")
#reformatting of equation 
mathEquation = mathEquation.replace(' ', '')
postFix = ' '
#creation of class object

#creation of class object
class Node:
#initalisation of class object
  def __init__(self, value = None, left = None, right = None, next = None):
    self.value = value
    self.left = left
    self.right = right
    self.next = next

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
      while postfixStack and (operatorOrder(mathEquation[i]) < operatorOrder(postfixStack[-1]) or (operatorOrder(mathEquation[i]) == operatorOrder(postfixStack[-1]))):
        result.append(postfixStack.pop())
      postfixStack.append(equation)

  while postfixStack:
   result.append(postfixStack.pop())

  print(''.join(result))

#creation of postfix order string
  for i in result:
    nodeValues += i

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
        if not x:
            return
        self.inorder(x.left)
        print(x.value, end=" ")
        self.inorder(x.right)

    def preorder(self, x):
        if not x:
            return
        print(x.value, end=" ")
        self.preorder(x.left)
        self.preorder(x.right)

    def postorder(self, x):
        if not x:
            return
        self.postorder(x.left)
        self.postorder(x.right)
        print(x.value, end=" ")
        
    def breadthFirstTraversal(self, x):
        if not x:
            return
 
def main():
    postfixEquation = infixOrPostfix(mathEquation)
    stack = Stack()
    tree = ExpressionTree()
    for character in postfixEquation:
        if character in "+-*/^":
            z = Node(character)
            x = stack.pop()
            y = stack.pop()
            z.left = y
            z.right = x
            stack.push(z)
        else:
            stack.push(Node(character))
    print("The Inorder Traversal of Expression Tree: ", end="")
    tree.inorder(stack.top())
    print("The Preorder Traversal of Expression Tree: ", end="")
    tree.preorder(stack.top())
    print("The Postorder Traversal of Expression Tree: ", end="")
    tree.postorder(stack.top())
    
 
if __name__ == "__main__":
    main()