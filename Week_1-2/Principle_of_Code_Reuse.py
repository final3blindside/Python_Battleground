# Example of bad, unproductive programming
# Also uses len()
name = "Kay"
number = len(name) * 9
print( "Hello " + name + " Your lucky number is " + str(number))

name = "Cameron"
number = len(name) * 9
print( "Hello " + name + " Your lucky number is " + str(number))

# Example of good, productive programming
# Also uses len()
def lucky_number(name):
  number = len(name) * 9
  print("Hello " + name + " Your lucky number is " +       str(number))

lucky_number("Kay")
lucky_number("Cameron")