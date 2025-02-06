"""
Visible tests of the types of matrix. Try any of these matrices with the method "type_of_matrix()"
to see the program printing the correct descriptions of each matrix. The correct descriptions are also noted
to the right of each matrix
"""

import matrix as Matrix
M = Matrix()

m0 = [[0, 0]]     # Binary
m1 = [[1, 2], [3, 3]]   # Square
m2 = [[1, 1, 0, 4, 3, 0, 5],    # Nothing
      [2, 0, 0, 5, 3, 2, 0],
      [1, 3, 2, 2, 0, 0, 4],
      [0, 1, 1, 3, 3, 2, 0]]
m3 = [[0.5, 0.2], [0.5, 0.8]]   # Square and left stochastic
m4 = [[0.5, 0.5], [0.5, 0.5]]   # Square, symmetric and double stochastic
m5 = [[2, -2], [2, 2]]      # Square, normal
m6 = [[0, 1], [-1, 0]]   # Square, unitary, normal
m7 = [[1, 2], [2, 1]]    # Square, symmetric, normal
m8 = [[1, 1], [0, 0], [1, 0]]     # Binary
m9 = [[1, -2, 1], [3, 0, 3], [-1, 2, -1]]    # Square, nilpotent degree 1
m10 = [[2]]     # Square, diagonal, symmetric, normal
m11 = [[2, 3], [-1, -2]]   # Square, involutory
M.type_of_matrix(m11)
