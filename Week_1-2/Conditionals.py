# A function that tells if your username is not allowed because it has more than 3 characters
def hint_username(username):
  if len(username) > 3:
    print("Invalid username. Please choose another one.")
  else:
    print("Username approved. Proceed to step 3")
    
hint_username("oga")

#Learning the Use of Modulo
#Else vs No Else statements

def is_even(number):
  if number % 2 == 0:
    return True
  else:
    return False

print(is_even(7))

#Learning how to use the elif statement

def hint_username(username):
  if len(username) < 3:
    print("Invalid username. Username must be at least 3 characters long")
  elif len(username) > 15:
    print('Invalid username. Username must be at most 15 characters long')
  else:
    print("You are a Top G")

hint_username("VianChicoKentJam")


#Practice Quiz Hard Question
def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize // block_size
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = filesize % block_size
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return block_size * (full_blocks + 1)
    return full_blocks * block_size

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192