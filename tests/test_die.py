import unittest
from src.Die import Die

class TestDie(unittest.TestCase):
  
  # Basic test.
  # ---
  # Roll a couple of times to determine the highest outcome.
  # For a basic die, obviously, this can't be higher than 6.
  def test_default(self) -> None:
    die = Die()
    outcomes = []
    for i in range(50):
      outcomes.append(die.roll())
    self.assertEqual(max(outcomes), 6, "SIX!!!")

  # Single sided die.
  # ---
  # When passing a list with a single value, the only possible outcome is 1.
  def test_basic(self) -> None:
    die = Die([1])
    self.assertEqual(die.roll(), 1, "The expected output should be equal to 1.")
  
  # Unique outcomes.
  # ---
  # Pass `True` as an argument to the `roll()` method.
  # By doing so, no outcome should match its predecessor.
  def test_unique(self) -> None:
    die = Die()
    outcomes = []
    duplicate = False
    for i in range(50):
      rng = die.roll(True)
      if len(outcomes) > 0 and rng == outcomes[-1]:
        duplicate = True
        break
      else:
        outcomes.append(rng)
    self.assertEqual(duplicate, False, "The value of variable `duplicate` should remain `False`.")

if __name__ == '__main__':
  unittest.main()