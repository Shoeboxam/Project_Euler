import numpy as np
from numpy import linalg


def pythagorean_brute():
  for index_a in range(1, zone):
    for index_b in range(1, zone):
      for index_c in range(1, zone):
        if index_a + index_b + index_c == zone and index_a ** 2 + index_b ** 2 == index_c ** 2:
          return (index_a, index_b, index_c)
  return False

def pythagorean_primaries():
  def price_linear_transformation(matrix_library):

    #STORE pythagorean triples
    triple_store = []

    #CALCULATE dot product of input triple with transposed transform-matrix
    for triple in matrix_library:
      #print(triple)
      triple_store.append(triple * lin_trans_A.T)
      triple_store.append(triple * lin_trans_B.T)
      triple_store.append(triple * lin_trans_C.T)

    #print("~~~~")

    return triple_store


  #STORE Price transformation matrices
  lin_trans_A = np.matrix([[2, 1, -1], [-2, 2, 2], [-2, 1, 3]])
  lin_trans_B = np.matrix([[2, 1, 1], [2, -2, 2], [2, -1, 3]])
  lin_trans_C = np.matrix([[2, -1, 1], [2, 2, 2], [2, 1, 3]])

  matrix_library = [np.array([3,4,5])]
  solution = np.array([0,0,0])

  #LOOP until answer is found
  while (solution == np.array([0,0,0])).all():
    #CALCULATE new set of triples
    matrix_library = price_linear_transformation(matrix_library)

    #CHECK for triple that meets criteria
    for triple in matrix_library:
      if np.prod(triple) == zone:
        return triple

  return False


#main() ~~~~~~~~~
zone = 90167220
print(pythagorean_primaries())
#pythagorean_brute()
