# -----------------------
# Random number generator
# -----------------------
# Class that generates a random number between 1 and a given maximum value.
from random import randint

class RNG:

  #region Attributes

  __list: list = []
  __prev_rng: int = 0

  #endregion

  #region Public methods

  # Generate random number.
  # ---
  # Picks a random number from the list.
  # ---
  # @param unique (bool)  Determines whether the previously generated number should should be excluded as a possible outcome.
  # ---
  # @returns rng (int)          Randomly generated number
  def generate(self, unique: bool = False) -> int:
    match = 0 if unique == False else self.__prev_rng
    filtered = list(filter(lambda x: x != match, self.__list))
    index = randint(1, len(filtered))
    rng = filtered[index - 1]
    self.__prev_rng = rng
    return rng

  #endregion

  #region Constructor

  # Constructor with parameters.
  # ---
  # @param maximum (int)  The maximum value of the range.
  def __init__(self, maximum):
    try:
      for i in range(1, maximum + 1):
        self.__list.append(i)
    except Exception as err:
        print(err)

  #endregion