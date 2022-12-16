# ---
# Die
# ---
# A class that acts as a random number generator.
# It can be included to return a random number between 1 and maximum value, based on the number of sides of the die.
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

  # Roll the die.
  # ---
  # Picks a random side of the die each time.
  # By setting the `animate` argument to `True`, the roll is simulated in the sense that the die can't show the same number twice in a row. If it could, it wouldn't be rolling.
  # ---
  # @param animate (bool)   Determines whether the previous outcome should be excluded.
  # ---
  # @returns rng (int)      Randomly generated number
  def roll(self, animate: bool = False) -> int:
    match = 0 if animate == False else self.__prev_rng
    filtered = list(filter(lambda x: x != match, self.__sides_list))
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