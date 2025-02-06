# For square matrices

# In the course linear algebra 2 it was hell having to always figure out the type of each matrix before
# knowing what theorems you can throw at it. This API assumes you have some square matrix and wants to know its type.
# It also allows for all standard operations that would change its type, but.


def getIdentity(size: int) -> matrix:
    """Returns the identity matrix with lengths size"""
    pass

def getZero(size: int) -> matrix:
    """Returns the square zero matrix with lengths size"""
    pass

def getElement(x, y):
    """Returns the element placed at the given x,y coordinate in the matrix"""
    pass

def changeElement(x, y, new_element):
    """Replaces the element at x,y with a new_element"""
    pass

def printMatrix():
    """Prints the matrix"""
    pass

def multiplication(A, B):
    """If A and/or B is scalar multiplies perform scalarmultiplication.
    If A and B are matrices performs matrix multiplication. Returns the resultant matrix"""
    pass

def addition()
    """Adds two matrices, returns sum matrix"""
    pass
def typeOfMatrix():
    """Returns a table telling if the matrix is Involuntory, unitary, nilpotent, binary, normal, diagonal, stochastic
    or adjoint"""
def _isInvolutory(A)
    """Returns true if A is an involution, as in A^2 = I """
    pass
def _isunitary()
    """Returns true if unitary. Will assume scalarproduct and check if columns make an orthonormal base"""
    pass
def _isnilpotent()
    """Returns true if zero matrix for an exponent of n. Uses the fact that the side length is the greatest value
    of n possible"""
    pass
def _isbinary():
    """Returns true if only contains values 0 and 1"""
    pass
def _isnormal(A)
    """Returns true if A*A^t = A^t * A"""
    pass
def _isdiagonal()
    """Returns true if zero everywhere except diagonal"""
    pass
def _isstochastic()
    """Returns true if stochastic: as in all entries are nonnegative, each column sums to 1"""
    pass
def _issymmetric():
    """Returns true if selfadjoint, aka symmetric"""
    pass
