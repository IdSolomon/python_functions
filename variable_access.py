# When it comes to variable access, if other functions can't have access to them,
# things can get messy with errors.
# We call the part of the program where a variable can be accessed its scope!
# The scope of a variable is only inside a function.

# def avengerCount():
#     ogAvengers = "Captain America, Iron Man, Hulk, Thor, Hawkeye, Black Widow"
#     print("There are six OG members of The Avengers")

# def showOGAvengers():
#     print("The OG Avengers are: " + ogAvengers)

# avengerCount()
# showOGAvengers()

# OUTPUT: NameError: name 'ogAvengers' is not defined. Did you mean: 'showOGAvengers'?
# The variable ogAvengers is not available for use because it's in another function.
# This is a scope issue.
# But if the scope is fixed so that both functions can access it --

ogAvengers = "Captain America, Iron Man, Hulk, Thor, Hawkeye, Black Widow"

def avengerCount():
    ogAvengers = "Captain America, Iron Man, Hulk, Thor, Hawkeye, Black Widow"
    print("There are six OG members of The Avengers")

def showOGAvengers():
    print("The OG Avengers are: " + ogAvengers)

avengerCount()
showOGAvengers()

# OUTPUT: There are six OG members of The Avengers
# The OG Avengers are: Captain America, Iron Man, Hulk, Thor, Hawkeye, Black Widow