#Write your program here 👇👇

mathEquation = input("please input your maths equation in the format of (X?Y) and this will convert it to a binary tree :): ")
mathEquation = mathEquation.replace(' ', '')
postFix = ' '
nodeValues = ""

class Node:
  def __init__(self, value = None, left = None, right = None, next = None):
    self.data = value
    self.left = left
    self.right = right
    self.next = next

def prec(equation):
  if equation == '^':
    return 3
  elif equation == '/' or equation == '*':
    return 2
  elif equation == '+' or equation == '-':
    return 1
  else:
    return -1

def associativity(equation):
  if equation == '^':
    return 'Right'
  return 'Left'

def infixOrPostfix(equation):
  result = []
  stack = []
  global nodeValues
  nodeValues = ' '.join(result)

  for i in range(len(mathEquation)):
    equation = mathEquation[i]

    if ('a' <= equation <= 'z') or ('A' <= equation <= 'Z') or ('0' <= equation <= '9'):
      result.append(equation)
    elif equation == '(':
      stack.append(equation)
    elif equation == ')':
      while stack and stack[-1] != '(':
        result.append(stack.pop())
      stack.pop()
    else:
      while stack and (prec(mathEquation[i]) < prec(stack[-1]) or (prec(mathEquation[i]) == prec(stack[-1]) and associativity(mathEquation[i]) == 'Left')):
        result.append(stack.pop())
      stack.append(equation)
  
  while stack:
    result.append(stack.pop())
  
  print(''.join(result))

  for i in result:
    nodeValues += i +""

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

class binaryExpressionTree:
  def inorder(self, x):
    if not x:
      return
    self.inorder(x.left)
    print(x.value, end = " ")
    self.inorder(x.right)

def main():
  stack = Stack()
  tree = binaryExpressionTree()

  for c in nodeValues:
    if c in "+-*/^":
      z = Node(c)
      x = stack.pop()
      y = stack.pop()
      z.left = y
      z.right = x
      stack.push(z)
    else:
      stack.push(Node(c))
  print("The Inorder Traversal of Expression Tree: ", end = " ")
  infixOrPostfix(mathEquation)
  print(nodeValues)


if __name__ == "__main__":
  main()