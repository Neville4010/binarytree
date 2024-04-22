#Write your program here 👇👇

mathEquation = input("please input your maths equation in the format of (X?Y) and this will convert it to a binary tree :): ")
mathEquation = mathEquation.replace(' ', '')

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

infixOrPostfix(mathEquation)
