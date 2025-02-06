"""
Module that provides methods to find the type of matrices
A mathematical matrix in a real vector space is represented as nestled loops in Python.
Depending on their elements they can have different properties.
With a given matrix, depending on its elements and shape, it has different properties. It can be Stochastic, as in
belonging to a Markov probability chain, or orthogonal, implying all eigenvalues lie on the unit circle circle, and
many more. This file provides common operations for matrices and then allows the user to test for what kind of matrix
they input.
"""


class Matrix:

    def __init__(self):
        self.list_of_matrices = []

    """Matrices will be represented as nestled for loops, where each nestles loop is a row and their elements the 
    columns. The class Matrix() can store matrices in a list and provides all operations"""

    def save_matrix(self, matrix):
        """Saves the matrix within an attribute to the class that is list, returns the index within that list
        Time complexity O(1)"""
        self.list_of_matrices.append(matrix)
        idx = self.list_of_matrices.index(matrix)
        print("Matrix saved at index " + str(idx))
        return idx

    def get_saved_matrix(self, idx):
        """Retuns a saved matrix of an inputted index. Time complexity O(1)"""
        return self.list_of_matrices[idx]

    def zero(self, rows: int, columns: int):
        """Returns the square zero matrix with lengths size. Time complexity O(n^2)"""
        zero_matrix = []
        for i in range(rows):
            zero_matrix += [[0]*columns]
        return zero_matrix

    def identity(self, size):
        """Returns the identity matrix with lengths size. Time complexity O(n^2)"""
        identity = self.zero(size, size)    # O(n^2)
        for i in range(size):
            identity[i][i] = 1
        return identity

    def get_element(self, matrix, row, column):
        """Returns the element located at that row and column. Time complexity O(1)"""
        return matrix[row][column]

    def change_element(self, matrix, new_element, r, c):
        """Replaces the element at x,y with a new_element. Time complexity O(1)"""
        matrix[r][c] = new_element
        return matrix

    def show(self, matrix):
        """Prints the matrix as a proper matrix. Time complexity O(n^2)"""
        for row_idx, row in enumerate(matrix):
            for column_idx, _ in enumerate(row):
                print(matrix[row_idx][column_idx], end="\t")
            print()

    def show_linear(self, matrix):
        """Prints the matrix as lists. Time complexity O(n)"""
        for row in matrix:
            print(row)

    def addition(self, A, B):
        """Adds two non-empty matrices, returns the sum. Time complexity O(n^2)."""
        result = self.zero(len(A), len(A[0]))
        for row_index in range(len(A)):
            # iterates each row
            for column_index in range(len(A[0])):
                result[row_index][column_index] = A[row_index][column_index] + B[row_index][column_index]
        return result

    def multiplication(self, A, B):
        """If A and/or B is scalar multiplies perform scalarmultiplication.
        If A and B are matrices performs matrix multiplication. Returns the product
        Time complexity depends on multiplication type, either O(1), O(n^2) or O(n^3)"""
        if isinstance(A, int or float) and isinstance(B, int or float):
            product = A*B      # Standard multiplication
        elif isinstance(A, int or float) or isinstance(B, int or float):
            product = self._scalar_multiplication(A, B)
        else:
            product = self._matrix_multiplication(A, B)
        return product

    def _scalar_multiplication(self, A, B):
        """Performs scalar multiplication between A and B and returns the product. Time complexity: O(n^2)"""
        if isinstance(A, int or float):
            scalar = A
            matrix = B
        else:
            scalar = B
            matrix = A
        for row_index, row in enumerate(matrix):
            for column_index, column in enumerate(row):
                matrix[row_index][column_index] = matrix[row_index][column_index] * scalar
        return matrix

    def _matrix_multiplication(self, A, B):
        """Performs matrix multiplication between A and B in that order and returns the product.
        Time complexity: O(n^3)"""
        R = (len(A))   # Number of rows of product
        C = (len(B[0]))    # Number of columns of product
        result = self.zero(R, C)
        for i in range(len(A)):
            # Row by row in A
            for j in range(len(B[0])):
                # column by column in a given row
                for k in range(len(B)):
                    # Row by row in B
                    result[i][j] = result[i][j] + A[i][k] * B[k][j]
                    # i x k * k x j. Every ik meet a kj at a ij.
        return result

    def transpose(self, A):
        """Returns the transpose of input matrix A. Time complexity O(n^2)"""
        B = self.zero(len(A[0]), len(A))    # A copy of A in which results are stored
        for i in range(len(A)):
            for j in range(len(A[0])):
                B[j][i] = A[i][j]
        return B

    def _is_square(self, A):
        """Returns True if input matrix is square, else returns false. Time complexity: O(1) """
        height = range(len(A))
        width = range(len(A[0]))
        if width == height:
            return True
        return False

    def _is_identity(self, A):
        """Returns True if input matrix is the identity matrix, else returns false. Time complexity: O(n)"""
        for i in range(len(A)):
            for j in range(len(A[0])):
                if i == j:
                    if A[i][i] != 1:
                        return False
                else:
                    if A[i][j] != 0:
                        return False
        return True

    def type_of_matrix(self, A):
        """Prints  if the matrix is Involuntory, orthonormal, nilpotent, binary, normal, diagonal, stochastic
        or adjoint. Time complexity: O(n^4)"""
        print("Matrix is")
        print("Binary: " + str(self._is_binary(A)))
        print("Square: " + str(self._is_square(A)))
        if self._is_square(A):
            print("Diagonal: " + str(self._is_diagonal(A)))
            print("Nilpotent: " + str(self._is_nilpotent(A)))
            print("Involutory: " + str(self._is_involutory(A)))
            print("Symmetric: " + str(self._is_symmetric(A)))
            print("Unitary: " + str(self._is_orthonormal(A)))
            print("normal: " + str(self._is_normal(A)))
            if self._is_stochastic(A):
                print("Stochastic as: " + str(self._is_stochastic(A)))

    def _is_involutory(self, A):
        """Returns true if A is an involution, as in A^2 = I. Time complexity O(n^3) """
        product = self.multiplication(A, A)
        return(self._is_identity(product))

    def _is_diagonal(self, A):
        """Returns true if zero everywhere except diagonal. Time complexity O(n^2)"""
        for i in range(len(A)):
            for j in range(len(A[0])):
                if i != j:
                    if A[i][j] != 0:
                        return False
        return True

    def _is_nilpotent(self, A):
        """Returns true if zero matrix for an exponent of n and returns that n
        Uses the fact that the side length is the greatest value of n possible. Time complexity O(n^4)"""
        max_n = len(A)
        nil = self.zero(max_n, max_n)
        for n in range(max_n + 1):
            A = self._matrix_multiplication(A, A)     # O(n^3)
            if A == nil:
                return [True, n]
        return False

    def _is_symmetric(self, A):
        """Returns true if self-adjoint, aka symmetric. Time complexity O(n^2)"""
        B = A.copy()
        B = self.transpose(B)   # O(n^2)
        if B == A:
            return True
        return False

    def _is_normal(self, A):
        """Returns true if A*A^t = A^t * A. Time complexity: O(n^3)"""
        AT = A.copy()
        AT = self.transpose(AT)
        product1 = self.multiplication(A, AT)
        product2 = self.multiplication(AT, A)
        if product1 == product2:
            return True
        return False

    def _is_orthonormal(self, A):
        """Returns true if orthonormal in real vector space, as in its transpose is its inverse.
        Time complexity: O(n^3)"""
        AT = A.copy()
        AT = self.transpose(AT)
        product = self.multiplication(A, AT)
        identity = self.identity(len(A))
        if product == identity:
            return True
        return False

    def _summarize_rows_and_columns(self, A):
        """Sums each row and column within a square matrix A. Returns two list of each summation order respectively
        with all sums. Time complexity: O(n^2)"""
        # Sums each row and column
        sum_of_rows = []
        sum_of_columns = []
        for i in range(len(A)):
            sum_row = 0
            sum_column = 0
            for j in range(len(A[0])):
                sum_column += A[j][i]
                sum_row += A[i][j]
            sum_of_rows.append(sum_row)
            sum_of_columns.append(sum_column)
        return sum_of_rows, sum_of_columns

    def _is_binary(self, A):
        """Returns true if input A only contains values 0 and 1. Time complexity O(n^2)"""
        for row in range(len(A)):
            for column in range(len(A[0])):
                if A[row][column] not in [0, 1]:
                    return False
        return True


    def _is_nonnegative(self, A):
        """Returns true if all elements withing matrix A are non-negative. Time complexity: O(n^2)"""
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] < 0:
                    return False
        return True

    def _is_stochastic(self, A):
        """Returns a descriptive string if stochastic: as in all entries are nonnegative and each column or row sums to 1
        Else returns False
        Time complexity: O(n^2)"""
        # Tests if each value is non-negative
        if not self._is_nonnegative(A): return False
        # Tests the sum of each column and row to check if the matrix is left or right stochastic
        sum_of_rows, sum_of_columns = self._summarize_rows_and_columns(A)
        record = []
        for _ in range(len(sum_of_rows)):
            if "not right" not in record:
                if sum_of_rows[_] != 1:
                    record.append("not right")
            if "not left" not in record:
                if sum_of_columns[_] != 1:
                    record.append("not left")
        # Return messages
        if record == []:
            return "double stochastic"
        if "not left" in record and "not right" not in record:
            return "right stochastic"
        if "not right" in record and "not left" not in record:
            return "left stochastic"
        return False
