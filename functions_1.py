#type() function
yummy = 3
print (type(yummy))

# Learning how to use functions
def greeting(name, department):
  print("Welcome, " + name + "!")
  print("You are part of the " + department) 

greeting("Yancey", "ECEPC")

# Learning how to use functions
def information(name, city, phone_number):
  print("Welcome, " + name)
  print("You live in " + city)
  print("We can contact you using: " + phone_number)

information("Yuan", "Cabuyao City", "09088797798")


# Learning how to use functions
## Plus str() function
def area_triangle(base, height):
  return (base*height)/2

area_a = area_triangle(3,5)
area_b = area_triangle(3,5)
sum = area_a + area_b
print("The sum of the two triangles is: " + str(sum))

