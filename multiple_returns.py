# Sometimes, I get greedy and I want to return more than one value from a function!
# I can return several values by separating them with a comma.

# Here's a function that allows users to see the inventions of Reed Richards 
# in the Fantastic 4 app!

inventions_ofReedRichards = [
    'Negative Zone Prison', 
    'The Bridge', 
    'Afterlife Transporter', 
    'Atomic Space Displacer',
    'Parker Particles',
    'Anti-Matter Injection System']

def reedRichards_inventionList(invention):
    firstInvention = "An alternate dimension designed to house inmates: " + invention[0]
    secondInvention = "A device that allows anyone to look into different realities: " + invention[1]
    thirdInvention = "A machine capable of transporting anyone to the afterlife: " + invention[2]
    fourthInvention = "A device similar to that of a nuclear weapon: " + invention[3]
    fifthInvention = "A hyper-kinetic form of energy that is tied to the expanding universe: " + invention[4]
    sixthInvention = "A technology, reverse-engineered, composed of two devices: " + invention[5]
    return firstInvention, secondInvention, thirdInvention, fourthInvention, fifthInvention, sixthInvention

# This function takes in a set of data in the form of a list for a user to see.
# I can get my returned function values by assigning them to variables when I call the function --

theFirst, theSecond, theThird, theFourth, theFifth, theSixth = reedRichards_inventionList(inventions_ofReedRichards)

print(theFirst)
print(theSecond)
print(theThird)
print(theFourth)
print(theFifth)
print(theSixth)

# OUTPUT: An alternate dimension designed to house inmates: Negative Zone Prison
# OUTPUT: A device that allows anyone to look into different realities: The Bridge        
# OUTPUT: A machine capable of transporting anyone to the afterlife: Afterlife Transporter
# OUTPUT: A device similar to that of a nuclear weapon: Atomic Space Displacer
# OUTPUT: A hyper-kinetic form of energy that is tied to the expanding universe: Parker Particles
# OUTPUT: A technology, reverse-engineered, composed of two devices: Anti-Matter Injection System

# Here's another function that displays Iron Man's favorite activities for a user 
# through the J.A.R.V.I.S. app!

def ironMans_topActivities():
    first = "Birdwatching"
    second = "Fishing"
    third = "Painting"
    fourth = "Stargazing"
    return first, second, third, fourth

top1, top2, top3, top4 = ironMans_topActivities()

print(top1)
print(top2)
print(top3)
print(top4)

# OUTPUT: Birdwatching
# OUTPUT: Fishing
# OUTPUT: Painting
# OUTPUT: Stargazing