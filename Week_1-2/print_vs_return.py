# In Belya's words: "you are calling greeting function and then calling print function"
# Therefore the output is "None"
def greetings(name):
  print("Welcome, " + name)

result = greetings("Christine!")
print(result)


# In Belya's words:  "you are invoking the greeting function and passing in the string "Christine" to the name parameter then the function will evaluate the string "Welcome, " + name and return it and it will be bindid to the result variable"
# Therefore the output is stored.
def greetings(name):
  return "Welcome, " + name

result = greetings("Christine!")
print(result)


# Return values allow our functions to be more flexible and powerful, so they can be reused and called multiple times. 

# Functions can even return multiple values. Just don't forget to store all returned values in variables! You could also have a function return nothing, in which case the function simply exits.
