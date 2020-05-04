"""
CTEC 121
<Tristan Sahagun>
<Mod 3 Lab 1>
<assignment/lab description
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""

def main():
  
  print("/nBoolean Literals")
  print(True)
  print(False)
  print(type(True))
  print()

  #relational operators
  print("Relational Operators")
  print("3 < 5", 3 < 5)
  print("3 <= 3",  3 <=3)
  print("3 == 3", 3 == 3)
  print("3 >= 5", 3 >= 5)
  print("3 != 5", 3 != 5)
  print()

  #using variables
  x = 3
  y = 5
  print("using variables")
  print("x:", x, "y:", y)
  print("x < y", x < y)
  print("x != y", x != y)
  print()

  #simple if statement
  print("x:", x, "y:", y)
  if x < y:
      print("x < y")

  if x > y:
        print("x > y")
  
  print("end simple if example")
  print()

  #if/else statement
  print("if/esle example")
  print("x:", x, "y:", y)
  if x < y:
      print("x < y")
  else:
      print("x >= y")    
  print("end if/else example")
  print()

  # exercise 3-1
  for i in range(1, 11):
      if (i % 2) == 0:
          outputstring = "even"
      else:
          outputstring = "odd"
      print(i, outputstring)
  # alphabetize names
  name = "Bill"
  firstletterofname = "B"
  if firstletterofname == "A":
      print("A")
  elif firstletterofname == "B":
      print("B")
  elif firstletterofname == "C":
      print("C")
  elif firstletterofname == "D":
      print("D")
  elif firstletterofname == "E":
      print("E")
  # . . .
    elif firstletterofname == "Z":
      print("Z")
  print()
  try:
      print(4/0)
  except:
      print("\nThere was a divide by zero error. try again")
      print()
      


main()    