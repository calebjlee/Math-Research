import math
import sys

""" 
    x1, x2, y1, y2, z represent the elements within the H(4) matrix:
    1  x1 x2  z
    0  1  0  y1
    0  0  1  y2
    0  0  0   1
"""
def calcHeisenburg(x1, y1, x2, y2, z):
  # Start out with our best solution that we want to minimize
  best_solution = sys.maxsize
  # f1 = f_{x1,y2}(z1)
  f1 = -1
  # f2 = f_{x2, y1}(z - z1)
  f2 = -1

  # Iterate through values of z1 up to z + 1
  for z1 in range(z + 1):

    # Calculating f1
    if y2 >= 0:
      if x1**2 >= z1:
        if x1 * y2 >= z1:
          f1 = x1 + y2
        else:
          f1 = 2 * math.ceil(z1 / x1) + x1 - y2
      else:
        f1 = 2 * math.ceil(2 * math.sqrt(z1)) - x1 - y2
    else:
      if x1 <= math.sqrt(z1 - x1 * y2):
        f1 = 2 * math.ceil(2 * math.sqrt(z1 - x1 * y2)) - x1 + y2
      else:
        f1 = 2 * math.ceil(2 * math.ceil(z1 / x1) + x1 - y2)

    # Calculating f2
    if y1 >= 0:

      if x2 <= math.sqrt(z - z1):
        f2 = 2 * math.ceil(2 * math.sqrt(z - z1)) - x2 + y1
      else:
        if x2 * y1 >= (z - z1):
          f2 = x2 + y1
        else:
          f2 = 2 * math.ceil((z - z1) / x2) + x2 - y1
      # y1 < 0
    else:
      
      if x2**2 <= z - z1 - x2 * y1:
        f2 = 2 * math.ceil(2 * math.sqrt(z - z1 - x2 * y1)) - x2 + y1
      else:
        f2 = 2 * math.ceil((z - z1) / x2) + x2 - y1

    best_solution = min(best_solution, f1 + f2)
  # Returns our best solution if z is a valid heisenberg matrix. Otherwise it returns -1, representing an error
  return best_solution if z >= 0 else -1

print(calcHeisenburg(1, 1, 1, 1, 8))