from inc.Die import Die
from inc.led_matrix import led_matrix
from sense_hat import SenseHat
from time import sleep
from itertools import cycle
import atexit

# Create a basic die with 6 sides.
die = Die()
hat = SenseHat()
degrees = cycle([0, 90, 180, 270])
spins = 15
threshold = 2

# Reset the LEDs when exiting the program.
def reset() -> None:
  hat.clear()
atexit.register(reset)

# Main functionality.
while True:
  # Allow the LED display to be cleared with the joystick.
  hat.stick.direction_middle = reset
  # Roll the die when the SenseHat is being shaked.
  acceleration = hat.get_accelerometer_raw()
  x = abs(acceleration['x'])
  y = abs(acceleration['y'])
  z = abs(acceleration['z'])
  if (x > threshold or y > threshold or z > threshold):
    # Simulate a rolling die by calling the `roll()` function a couple of times.
    # Set its argument `animate` to `True` in order to prevent the same number from being generated twice in a row.
    i = 0
    while (i < spins):
      number = die.roll(True)
      hat.set_pixels(matrix[number])
      # Rotate display and update the index to cycle through the rotation values.
      rotation = next(degrees)
      hat.set_rotation(rotation, False)
      i += 1
      sleep(0.1)