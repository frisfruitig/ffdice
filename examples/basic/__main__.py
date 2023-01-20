# Import the class.
from src.Die import Die

# By omitting parameters in the instance creation, you'll create a die with 6 sides.
die = Die()

# For this instance, the `roll()` function will return a number between 1 and 6.
number = die.roll()
print("You rolled %d!" % number) 