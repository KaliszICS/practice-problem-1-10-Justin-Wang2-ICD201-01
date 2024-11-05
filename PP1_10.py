import math

def q1(): 
  num = float(input("Input a number: "))

  print(math.sqrt(num))

def q2(): 
  num = int(input("Input a number: "))
  print(math.isqrt(num))

def q3(): 
  num = float(input("Input a number: "))
  print(math.floor(num))
  
def q4(): 
  num = float(input("Input a number: "))
  print(math.ceil(num))


def q5(): 
  num = float(input("Input a number: "))
  num1 = float(input("Input another number: "))
  num = num1 * num
  num = num / 2
  print(math.trunc(num))



#Do not alter the following code
#Comment out the following code when running your tests

#q1()
#q2()
#q3()
#q4()
#q5()
