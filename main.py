from inc.Die import Die
from time import sleep

# Create a basic die with 6 sides
die = Die()

# Simulate a rolling die by calling the `roll()` function a couple of times.
i = 0
while (i < 10):
  number = die.roll()
  print("Looks like it's going to be %d..." % (number))
  sleep(0.1)
  i += 1

# Use the last output as the definitive value.
print("You rolled %d!" % (number))