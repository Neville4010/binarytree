#user input
mathEquation = input("please input your maths equation in format of (X?Y) and this will convert it to a binary tree :) : ")
#reformatting of equation 
mathEquation = mathEquation.replace(' ', '')
postFix = ' '
#creation of class object
class Node:
#initalisation of class object
  def __init__(self, value = None, left = None, right = None, next = None):
    self.data = value
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
    nodeValues += i + " "

  return nodeValues

# main function
def main():
  #stack = Stack()
  #tree = binaryExpressionTree()
  postfixEquation = infixOrPostfix(mathEquation)

#conditional validation check for reusability of code
if __name__ == "__main__":
  main()