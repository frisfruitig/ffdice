# Import the class.
from src.Die import Die

# Define colors.
colors = ("black", "white", "purple", "blue", "green", "yellow", "orange", "red")

# Create a die with as much sides as there are colors.
die = Die(len(colors))

# Use the output of the `roll()` method to pick the appropriate color.
index = die.roll()
color = colors[index - 1]
print("You rolled %s!" % color)
