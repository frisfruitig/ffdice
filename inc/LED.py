# Set the RGB values for off (O) and on (X).
O = [0, 0, 0]
X  = [255, 255, 255]

# Define the matrix for each side of the die.
matrices = {
  1: [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, X, X, O, O, O,
    O, O, O, X, X, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
  ],
  2: [
    O, O, O, O, O, O, X, X,
    O, O, O, O, O, O, X, X,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    X, X, O, O, O, O, O, O,
    X, X, O, O, O, O, O, O,
  ],
  3: [
    O, O, O, O, O, O, X, X,
    O, O, O, O, O, O, X, X,
    O, O, O, O, O, O, O, O,
    O, O, O, X, X, O, O, O,
    O, O, O, X, X, O, O, O,
    O, O, O, O, O, O, O, O,
    X, X, O, O, O, O, O, O,
    X, X, O, O, O, O, O, O,
  ],
  4: [
    X, X, O, O, O, O, X, X,
    X, X, O, O, O, O, X, X,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    X, X, O, O, O, O, X, X,
    X, X, O, O, O, O, X, X,
  ],
  5: [
    X, X, O, O, O, O, X, X,
    X, X, O, O, O, O, X, X,
    O, O, O, O, O, O, O, O,
    O, O, O, X, X, O, O, O,
    O, O, O, X, X, O, O, O,
    O, O, O, O, O, O, O, O,
    X, X, O, O, O, O, X, X,
    X, X, O, O, O, O, X, X,
  ],
  6: [
    X, X, O, O, O, O, X, X,
    X, X, O, O, O, O, X, X,
    O, O, O, O, O, O, O, O,
    X, X, O, O, O, O, X, X,
    X, X, O, O, O, O, X, X,
    O, O, O, O, O, O, O, O,
    X, X, O, O, O, O, X, X,
    X, X, O, O, O, O, X, X,
  ]
}