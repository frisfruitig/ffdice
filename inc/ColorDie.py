# --------
# ColorDie
# --------
# A subclass for dice with colored sides instead numbers.
from .Die import Die

class ColorDie(Die):

   #region Attributes

  __colors: list = []

  #endregion

  #region Public methods

  # Roll the die (for LED display).
  # ---
  # Visual representation the super `roll()` function.
  # Instead of returning an integer, return information that can be used to display on a LED matrix.
  # ---
  # @param unique (bool)    Determines whether the previous outcome should be excluded.
  # ---
  # @returns matrix (list)  List of color values that can be used on a LED display.
  def roll_image(self, unique: bool = False) -> list:
    rng = self.roll(unique)
    O = [  0,   0,   0]
    X = [255, 255, 255]
    C = self.__colors[rng - 1]
    matrix = [
      X, X, X, X, X, X, X, O,
      X, X, C, C, C, X, X, O,
      X, C, C, C, C, C, X, O,
      X, C, C, C, C, C, X, O,
      X, C, C, C, C, C, X, O,
      X, X, C, C, C, X, X, O,
      X, X, X, X, X, X, X, O,
      O, O, O, O, O, O, O, O,
    ]
    return matrix

  #endregion

  #region Constructor

  # Constructor with parameters.
  # ---
  # @param colors (list)    List of RGB color values for each side.
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
    super().__init__(self.__colors)

  #endregion