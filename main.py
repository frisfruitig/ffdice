from random import randint
from time import sleep

# In this case, use a simple dice.
# Generate a random number between 1 and 6.
min = 1
max = 6
sides = []
for i in range(min, max + 1):
  sides.append(i)

# Simulate a dice roll. Exclude the previous random number, as the random number should be different each time while the dice is still rolling.
last_rng = 0
i = 0

while (i < 10):
  filtered = list(filter(lambda x: x != last_rng, sides))
  index = randint(1, len(filtered))
  rng = filtered[index - 1]
  last_rng = rng
  i += 1
  print(rng)
  sleep(0.25)


# print(sides, filtered, len(filtered))

# number = randint(1, 6)

# # Generate a new number a couple of times to simulate a dice roll.
# # Since dice can't roll on the same number 
# i = 0
# last_value = 0

# while (i < 10):
#   number = randint(1, 6)
#   print(number)
#   i += 1 
#   sleep(0.5)

# # print(number)