# --------
# BasicDie
# --------
# An RNG subclass that acts as a basic die.
# It may return a random number between 1 and 6, based on its sides.
from .RNG import RNG
from ._matrix import _matrix

class Die(RNG):

  #region Attributes

  __images: list

  #endregion

  #region Public methods

  # Roll the die.
  # ---
  # Picks a random side of the die each time.
  # By setting the `unique` argument to `True`, the roll is simulated in the sense that the die can't show the same number twice in a row.
  # (If it could, it wouldn't be rolling.)
  # ---
  # @param unique (bool)    Determines whether the previous outcome should be excluded.
  # ---
  # @returns rng (int)      Randomly generated number
  def roll(self, unique: bool = False) -> int:
    return super().generate(unique)

  # Roll the die (for LED display).
  # ---
  # Visual representation the `roll()` function.
  # Instead of returning an integer, return information that can be used to display on a LED matrix.
  # ---
  # @param unique (bool)    Determines whether the previous outcome should be excluded.
  # ---
  # @returns matrix (list)  List of color values that can be used on a LED display.
  def roll_image(self, unique: bool = False) -> list:
    rng = self.roll(unique)
    return self.__images[rng - 1]

  #endregion

  #region Instance special methods

  # Construct.
  # ---
  # Called after the instance is created by `__new__()`.
  # ---
  # @param images (list)    List of color values that can be used on a LED display.
  def __init__(self, images: list = []) -> None:
    if images != []:
      self.__images = images
    else:
      self.__images = _matrix
    super().__init__(len(self.__images))

  #endregion