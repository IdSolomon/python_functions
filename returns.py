# Functions can also return a value to the program so that a value can be modified
# or used later - The Python keyword "return" allows us to do this!

def calculate_exchange_usd(us_dollars, exchange_rate):
    return us_dollars * exchange_rate

dominican_republic_exchange = calculate_exchange_usd(100, 56.65)

print("100 dollars in US currency would give you " + str(dominican_republic_exchange) + " Dominican Pesos!")

# OUTPUT: 100 dollars in US currency would give you 5665.0 Dominican Pesos!
# Saving our values returned from a function like I did with dominican_republic_exchange allows us
# to reuse the value, in the form of a variable, throughout the rest of the program.

# HERE'S SOME MORE - Enjoy!

tonyStarks_currentBudget = 50000000.00

def print_remainingBudget(budget):
    print("Tony, your remaining budget is: $" + str(budget))

print_remainingBudget(tonyStarks_currentBudget)

# OUTPUT: Tony, your remaining budget is: $50000000.0

def deduct_expense(budget, expense):
    return budget - expense

bugattiExpense = 18100000.00
newBudget_afterBugatti = deduct_expense(tonyStarks_currentBudget, bugattiExpense)
print_remainingBudget(newBudget_afterBugatti)

# OUTPUT: Tony, your remaining budget is: $31900000.0
# Tony had a budget of $50 Million dollars. But the street-legal hypercar,
# the Bugatti La Voiture Noire, caught his eye and he immediately bought it
# costing him $18.1 Million dollars.
# Now, Tony's budget is down to $31.9 Million dollars.
