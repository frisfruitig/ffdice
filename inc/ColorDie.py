# --------
# ColorDie
# --------
# A Die subclass that displays a color instead of a numeric value.
from .Die import Die

class ColorDie(Die):

   #region Attributes

  __colors: list = []

  #endregion

  #region Public methods

  # Roll the die.
  # ---
  # @param animate (bool)   Determines whether the previous outcome should be excluded.
  # ---
  # @returns RGB (list)     RGB color mapped to the randomly generated number index in `__colors`.
  def roll(self, animate: bool = False) -> list:
    rng = super().roll(animate)
    return self.__colors[rng - 1]

  #endregion

  #region Constructor

  # Constructor with parameters
  # ---
  # @param colors (list)  The RGB values of each side.
  def __init__(self, colors: list = []):
    if colors != []:
      self.__colors = colors
    else:
      self.__colors = [
        [240, 240, 240], # Off-white
        [215,  40,  60], # Red
        [250, 130,  90], # Orange
        [240, 220,  60], # Yellow
        [ 60, 215, 100], # Green
        [ 60, 100, 215], # Blue
      ]
    super().__init__(len(self.__colors))
    print(self.__colors)

  #endregion