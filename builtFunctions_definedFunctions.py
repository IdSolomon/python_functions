# So, I've been using User Defined Functions - functions that are written by users
# such as ourselves. Then there are Built-in Functions - functions that come built
# into Python for us to use.
# I am going to use THREE built-in functions!

# I go to an online Bazaar and see a list of prices for some of the available items:

arrowPrice = 10.75
deku_seedPrice = 14.25
wooden_shieldPrice = 25.50
iron_shieldPrice = 55.47
smallseed_satchelPrice = 25.25
small_quiverPrice = 35.75
recovery_heartPrice = 10.25
hylian_shieldPrice = 100.25
deku_stickPrice = 8.75

# To get the maximum price out of this list, I will use the built-in function, max() --

maxPrice = max(
    arrowPrice,
    deku_seedPrice,
    wooden_shieldPrice,
    iron_shieldPrice,
    smallseed_satchelPrice,
    small_quiverPrice,
    recovery_heartPrice,
    hylian_shieldPrice,
    deku_stickPrice
)

print(maxPrice)

# OUTPUT: 100.25 (hylian_shieldPrice)
# Obviously the most expensive item in the store is the Hylian Shield!

# The next built-in function is min() --

minPrice = min(
    arrowPrice,
    deku_seedPrice,
    wooden_shieldPrice,
    iron_shieldPrice,
    smallseed_satchelPrice,
    small_quiverPrice,
    recovery_heartPrice,
    hylian_shieldPrice,
    deku_stickPrice
)

print(minPrice)

# OUTPUT: 8.75 (deku_stickPrice)
# And the most minimally priced item is the Deku stick!
# 8.75?!? WHAT A RIPOFF!! You can find those anywhere in the world for FREE!!!

# Up next, round() --

roundedPrices = round (
    hylian_shieldPrice
)

print(roundedPrices)

# OUTPUT: 100
# The Hylian Shield is rounded to 100.
# Also, the round() built-in function takes in two arguments.
# The first argument is the number we want to round, followed by an argument 
# on how many decimal places we want to round it.
# I just didn't use an argument here.