# In Python, the amount of whitespace tells the computer 
# what is part of a function and what is not part of that function.

# Also note that the execution of a program always begins on the first line. 
# The code is then executed one line at a time from top to bottom. 
# This is known as execution flow and is the order a program in python executes code.

def theAvengers():
    # This indented code is part of the function body --
    print("He's my friend.")
    print("I thought I was your friend.")

# The unindented code below is not part of the function body --
print("I understood that reference!")

# Even though my function was defined before my lone print() statement, 
# the output will put it right before the function.
theAvengers()

# OUTPUT: I understood that reference!
# He's my friend.
# I thought I was your friend. 