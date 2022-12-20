from inc.Die import Die
from inc.LED import matrices as matrix
from sense_hat import SenseHat
from time import sleep
from itertools import cycle
import atexit

# Create a basic die with 6 sides.
die = Die()
hat = SenseHat()
degrees = cycle([0, 90, 180, 270])

# Reset the LEDs when exiting the program.
def quit() -> None:
  hat.clear()
atexit.register(quit)

# Main functionality.
while True:
  # Roll the die each time the SenseHat joystick is pressed
  event = hat.stick.wait_for_event()
  if(event.action == "pressed" and event.direction == "middle"):
    # Simulate a rolling die by calling the `roll()` function a couple of times.
    # Set its argument `animate` to `True` in order to prevent the same number from being generated twice in a row.
    i = 0
    while (i < 10):
      number = die.roll(True)
      hat.set_pixels(matrix[number])
      # Rotate display and update the index to cycle through the rotation values.
      rotation = next(degrees)
      hat.set_rotation(rotation, False)
      i += 1
      sleep(0.1)