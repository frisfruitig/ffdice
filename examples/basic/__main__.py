# Import the class.
from src.Die import Die

# By omitting parameters in the instance creation, you'll create a die with 6 sides.
die_one = Die()
die_two = Die()

# For this instance, the `roll()` function will return a number between 1 and 6.
a = die_one.roll()
b = die_two.roll()
print("You rolled %d and %d, adding up to a total of %d!" % (a, b, a + b))
