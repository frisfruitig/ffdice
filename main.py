from inc.Die import Die
from inc.LED import matrices as matrix
from sense_hat import SenseHat
from time import sleep

# Create a basic die with 6 sides.
die = Die()
hat = SenseHat()

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
      # print("Looks like it's going to be %d..." % (number))
      sleep(0.1)
      i += 1

    # Log the last output as the definitive value.
    print("You rolled %d!" % (number))
    sleep(0.1)