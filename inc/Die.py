# ---
# Die
# ---
# A class that acts as a random number generator.
# It can be included to return a random number between a given minimum and maximum value, based on the number of sides of the die.
from random import randint

class Die:

  #region Attributes

  __sides: int
  __sides_list: list = []
  __prev_rng: int = 0

  #endregion

  #region Private methods

  # Generate all sides of the die
  # ---
  def __generate_sides(self):
    for i in range(1, self.__sides + 1):
      self.__sides_list.append(i)

  #endregion

  #region Public methods

  # Simulate dice roll
  # ---
  # Exclude the previous random number, as the random number should be different each time while the dice is still rolling.
  # ---
  # @returns rng (int)  Randomly generated number that differs from any previous RNG
  def roll(self) -> int:
    filtered = list(filter(lambda x: x != self.__prev_rng, self.__sides_list))
    index = randint(1, len(filtered))
    rng = filtered[index - 1]
    self.__prev_rng = rng
    return rng

  #endregion

  #region Constructor

  # Constructor with parameters
  # ---
  # @param sides (int)  The amount of sides of the die.
  def __init__(self, sides: int = 6):
    self.__sides = int(sides)
    self.__generate_sides()

  #endregion