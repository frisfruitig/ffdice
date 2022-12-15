# -----------------------
# Random number generator
# -----------------------
# Can be included to return a random number between a given minimum and maximum value

class RNG:

  #region Attributes

  min: int = 1
  max: int = 6

  #endregion

  #region Public methods

  def generate(self):
    return (self.min, self.max)

  #endregion

  #region Constructor

  # Constructor with parameters
  # ---
  # @param min (int)  The generated minimum value.
  # @param max (int)  The generated maximum value.
  def __init__(self, min = 1, max = 6):
    self.min = min if min != None else 1
    self.max = max if max != None else 6

  #endregion