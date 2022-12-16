from inc.Die import Die
from inc.LED import matrices as matrix
from time import sleep

# print(matrix[1])

# Create a basic die with 6 sides.
die = Die()

# Simulate a rolling die by calling the `roll()` function a couple of times.
# Set its argument `animate` to `True` in order to prevent the same number from being generated twice in a row.
i = 0
while (i < 10):
  number = die.roll(True)
  print("Looks like it's going to be %d..." % (number))
  sleep(0.1)
  i += 1

# Use the last output as the definitive value.
print("You rolled %d!" % (number))