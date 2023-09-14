# In Python, there are 3 different types of arguments we can give a function --
# Positional arguments: arguments that can be called by their position in the function definition.
# Keyword arguments: arguments that can be called by their name.
# Default arguments: arguments that are given default values.
# The final_mutant parameter has a default value of "Magma".

def newMutants(first_mutant, second_mutant, final_mutant = "Magma"):
    print("Here are the new mutants!")
    print("The first mutant is " + first_mutant + ", then second is " + second_mutant + ", and lastly " + final_mutant + ".")

newMutants("Jubilee", "Iceman", "Wolfsbane")

# OUTPUT: Here are the new mutants!
# OUTPUT: The first mutant is Jubilee, then second is Iceman, and lastly Wolfsbane.
# Note the difference in the output depending on the position of the arguments!

# I'm gonna call the function again, but this time I'll include the keyword arguments and
# put them in order.

newMutants(first_mutant = "Boom-Boom", second_mutant = "Cannonball", final_mutant = "Sunspot")

# OUTPUT: Here are the new mutants!
# OUTPUT: The first mutant is Boom-Boom, then second is Cannonball, and lastly Sunspot.

# Finally, I'm going ahead and calling the function one last time by using only two positional
# arguments too see the default argument in action.

newMutants("Jubilee", "Iceman")

# OUTPUT: Here are the new mutants!
# OUTPUT: The first mutant is Jubilee, then second is Iceman, and lastly Magma.