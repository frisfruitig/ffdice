from inc.Die import Die
from inc.LED_alt import matrices as matrix
from sense_hat import SenseHat
from time import sleep

# Create a basic die with 6 sides.
die = Die()
hat = SenseHat()

# Ideally, we could cycle through the list of rotations with itertools.
rotation = [0, 90, 180, 270]
rotation_index = 0

try:
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
        hat.set_rotation(rotation[rotation_index], False)
        rotation_index = rotation_index + 1 if rotation_index != len(rotation) - 1 else 0
        sleep(0.1)
        i += 1

      # Log the last output as the definitive value.
      print("You rolled %d!" % (number))
      sleep(0.1)
finally:
  # Clear LEDs when closing the program.
  hat.clear()