from inc.ColorDie import ColorDie
from inc.LED import matrices as matrix
from time import sleep

# Create a basic die with 6 sides.
die = ColorDie()
spins = 1
threshold = 2

# Main functionality.
i = 0
while i < spins:
  # Simulate a rolling die by calling the `roll()` function a couple of times.
  # Set its argument `animate` to `True` in order to prevent the same number from being generated twice in a row.
  number = die.roll(True)
  print(number)
  i += 1
  sleep(0.1)