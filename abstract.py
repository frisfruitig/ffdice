# from inc.ColorDie import ColorDie as Die
from inc.Die import Die
from time import sleep

# Create a basic die with 6 sides.
die = Die()
spins = 1
threshold = 2

# Main functionality.
i = 0
while i < spins:
  # Simulate a rolling die by calling the `roll()` function a couple of times.
  # Set its argument `animate` to `True` in order to prevent the same number from being generated twice in a row.
  number = die.roll_image(True)
  print(number)
  i += 1
  sleep(0.1)