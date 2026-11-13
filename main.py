import math

def addmultiplenumbers(num):
  return sum(num)

def multiplymultiplenumbers(num):
  return math.prod(num)
  
def isiteven(num:int) -> bool:
  return num % 2 == 0
  
def isitaninteger(num) -> bool:
  if isinstance(num, int):
      return True
  elif isinstance(num, float):
      return False
  
def main():
    print("¡Bienvenido a la calculadora!")

    print(addmultiplenumbers([2, 3, 6, 10]))
    print(multiplymultiplenumbers([2, 3, 4]))
    print(isiteven(6))
    print(isitaninteger(7.3))

if __name__=="__main__":
  main()