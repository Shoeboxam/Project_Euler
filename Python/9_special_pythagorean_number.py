import numpy as np
from numpy import linalg

def pythagorean_brute(zone):
  for index_a in range(1, zone):
    for index_b in range(1, zone):
      for index_c in range(1, zone):
        if index_a + index_b + index_c == zone and index_a ** 2 + index_b ** 2 == index_c ** 2:
          return (index_a, index_b, index_c)
  return False

def price_linear_transformation(matrix_library, depth):
  for calculate in matrix_library[-1:]:
    calculate = [base * linear_transformation[0].T, base * linear_transformation[1].T, base * linear_transformation[2].T]
    matrix_library[depth].append(calculate)
  print matrix_library
  return matrix_library


  #if depth >= 1:
  #  print price_linear_transformation(base * linear_trans_A.T, depth)
  #  print price_linear_transformation(base * linear_trans_B.T, depth)
  #  print price_linear_transformation(base * linear_trans_C.T, depth)

zone = 60
ceiling = 8
depth = 0
base = np.matrix([5,12,13])

#used in price linear matrix function
linear_transformation= [np.matrix('2 1 -1; -2 2 2; -2 1 3'),
                        np.matrix('2 1 1; 2 -2 2; 2 -1 3'),
                        np.matrix('2 -1 1; 2 2 2; 2 -1 1')]

matrix_library = [0] * depth
#unfortunately used an array of lists of matrices
while depth <= ceiling:
  matrix_library = price_linear_transformation(matrix_library, depth)
  depth += 1
else:
  print matrix_library

print price_linear_transformation(base, depth)

total = 1
indices = False
if indices != False:
  for value in indices:
    total *= value
  print total
else:
  pass #print "No Pythagorean triple found"
