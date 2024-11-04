  import math

def q1(): 
  num = input("input a number: ")
  num = int(num)
  num = math.sqrt(num)
  print(num)

def q2(): 
  num = input("input a number: ")
  num = int(num)
  num = math.sqrt(num)
  print(num)

def q3(): 
  num = input("input a number: ")
  num = float(num)
  num = math.floor(num)
  print(num)
  
def q4(): 
  num = input("input a number: ")
  num = float(num)
  num = math.ceil(num)
  print(num)


def q5(): 
  num = input("input a number: ")
  num1 = input("input another number: ")
  num = int(num)
  num1 = int(num1)
  num2 = num1 * num
  num2 = int(num2)
  num3 = num2 / 2
  num3 = int(num3)
  num = math.floor(num3)
  print(num)



#Do not alter the following code
#Comment out the following code when running your tests

q1()
q2()
q3()
q4()
q5()
