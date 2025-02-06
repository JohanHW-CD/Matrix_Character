"""
Python file for testing all methods withing matrix.py. Raises assertion error if any method does not produce
expected result
"""

import matrix as Matrix
import random as r


def main():
    # Test class attribute, get and save functions.
    M = Matrix()
    assert(M.list_of_matrices == [])
    m1 = []
    m2 = [[1, 2], [3, 3]]
    m3 = [[1, 2, 3, 5, 1], [2, 5, 9, 2, 4]]
    indices = []
    indices.append(M.save_matrix(m1))
    indices.append(M.save_matrix(m2))
    indices.append(M.save_matrix(m3))
    assert(len(M.list_of_matrices) == 3)
    assert(M.list_of_matrices[1] == M.get_saved_matrix(1))
    assert(M.get_saved_matrix(2) == [[1, 2, 3, 5, 1], [2, 5, 9, 2, 4]])

    # Test creation of identity matrices
    assert(M.identity(3) == [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    assert(M.identity(1) == [[1]])
    assert((M.identity(0)) == [])

    # Test creation of zero matrices
    assert(M.zero(3, 3) == [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    assert(M.zero(1, 2)) == [[0, 0]]
    assert(M.zero(1, 1) == [[0]])
    assert((M.zero(0, 0)) == [])

    # Test printing methods (visible), getting at indices and changing matrices at indices with new class instances
    M2 = Matrix()
    m4 = M.zero(3, 3)
    for i in range(3):
        for j in range(3):
            c = r.randint(0, 100)
            m4[i][j] = c
    M2.show(m4)
    m4 = M2.change_element(m4, 10, 1, 1)
    assert(m4[1][1] == 10)
    M = Matrix()
    m4 = M.change_element(m4, 1000, 0, 2)
    assert(M.get_element(m4, 0, 2) == 1000)
    assert(isinstance(M.get_element(m4, r.randint(0, 2), r.randint(0, 2)), int))
    M2.show_linear(m4)

    # Test addition
    M = Matrix()
    m1 = [[1, 2, 2], [3, 1, 4], [4, 4, 0], [1, 1, 1]]
    m2 = [[2, 5, 3], [3, 0, -3], [10, -4, 0], [2, 1, 0]]
    assert(M.addition(m1, m2) == [[3, 7, 5], [6, 1, 1], [14, 0, 0], [3, 2, 1]])
    m1 = [[0, 0], [0, 1]]
    m2 = [[1000, 0], [0, 0]]
    assert(M.addition(m1, m2) == [[1000, 0], [0, 1]])

    # Test multiplication
    k = 5
    plain_multiplication = M.multiplication(k, k)
    assert(plain_multiplication == 25)

    m1 = [[2, 1], [3, 4]]
    m2 = [[1, 0], [2, 2]]
    result1 = M.multiplication(m1, k)
    assert(result1 == [[10, 5], [15, 20]])
    result2 = M.multiplication(k, m1)
    result3 = M.multiplication(k, m2)
    assert(result1 == result2)
    assert(result3 != result2)

    m3 = [[1, 1], [2, -1], [-2, 4]]
    m4 = [[2], [1]]
    result3 = M.multiplication(m3, m4)
    assert(result3 == [[3], [3], [0]])

    m1 = [[1, 0, 3, 4],
          [2, 3, 0, 0],
          [1, 3, 5, 5]]
    m2 = [[1, 1, 0, 4, 3, 0, 5],
          [2, 0, 0, 5, 3, 2, 0],
          [1, 3, 2, 2, 0, 0, 4],
          [0, 1, 1, 3, 3, 2, 0]]
    m3 = M._multiplication(m1, m2)
    assert(m3 == [[4, 14, 10, 22, 15, 8, 17],
                  [8, 2, 0, 23, 15, 6, 10],
                  [12, 21, 15, 44, 27, 16, 25]])

    # Test transpose method
    m1 = [[1]]
    assert(M.transpose(m1) == [[1]])
    m2 = [[1, 2, 3], [1, 4, 5]]
    assert(M.transpose(m2) == [[1, 1], [2, 4], [3, 5]])
    m3 = [[1, 2], [3, 4]]
    assert(M.transpose(m3) == [[1, 3], [2, 4]])

    # Test _is_square
    m1 = [[1, 1], [2, 2]]
    assert(M._is_square(m1))
    m1 = [[1, 1, 3], [2, 2, 3]]
    assert(not M._is_square(m1))

    # Test _is_identity
    m1 = [[1]]
    assert(M._is_identity(m1))
    m1 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    assert(M._is_identity(m1))
    m1 = [[1, 1], [1, 1]]
    assert(not M._is_identity(m1))

    # Testing _is_involutory
    assert(M._is_involutory([[1]]))
    assert(M._is_involutory([[2, 3], [-1, -2]]))
    assert(not M._is_involutory([[2, 2], [-1, 3]]))

    # Testing _is_diagonal
    assert(M._is_diagonal([[2]]))
    assert(M._is_diagonal([[2, 0], [0, -5]]))
    assert(not M._is_diagonal([[2, 0], [-5, 0]]))

    # Testing _is_nilpotent,
    assert(M._is_nilpotent([[1, -2, 1], [3, 0, 3], [-1, 2, -1]]))
    assert(M._is_nilpotent([[0, 0], [0, 0]]))
    assert(M._is_nilpotent([[0]]))
    assert(not M._is_nilpotent([[2, -4], [1, -3]]))

    # Testing _is_symmetric,
    assert(M._is_symmetric([[1]]))
    assert(M._is_symmetric([[1, 2], [2, 1]]))
    assert(not M._is_symmetric([[1, 2, 3], [1, 2, 3]]))

    # Testing _is_normal
    assert(M._is_normal(M.identity(4)))
    assert(M._is_normal([[2, -2], [2, 2]]))
    assert(not M._is_normal([[1, 0], [1, 1]]))

    # Testing _is_orthonormal
    assert(M._is_orthonormal([[0, 1], [-1, 0]]))
    assert(M._is_orthonormal([[2/3, -2/3, 1/3], [1/3, 2/3, 2/3], [2/3, 1/3, -2/3]]))

    # Testing _is_binary
    assert(M._is_binary([[0]]))
    assert(not M._is_binary([[2]]))
    assert(M._is_binary([[1, 1], [0, 0], [1, 0]]))
    assert(not M._is_binary([[1, 1], [2, 0], [1, 0]]))

    # Testing is_nonnegative, summarize_rows_and_columns, _is_stochastic
    m1 = [[1, 2], [3, 3]]
    m2 = [[-1, 0], [3, 4]]
    m3 = [[0.5, 0.5], [0.2, 0.8]]
    m4 = [[0.5, 0.2], [0.5, 0.8]]
    m5 = [[0.5, 0.5], [0.5, 0.5]]

    assert(M._is_nonnegative(m1))
    assert(not M._is_nonnegative(m2))
    assert(M._is_nonnegative(m3))

    assert(M._summarize_rows_and_columns(m1) == ([3, 6], [4, 5]))
    assert(M._summarize_rows_and_columns(m2) != ([3, 5], [3, 4]))

    assert(not M._is_stochastic(m1))
    assert(not M._is_stochastic(m2))
    assert(M._is_stochastic(m3) == "right stochastic")
    assert(M._is_stochastic(m4) == "left stochastic")
    assert(M._is_stochastic(m5) == "double stochastic")


main()
