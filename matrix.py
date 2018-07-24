import random

from copy import deepcopy



class Matrix():

    def __init__(self, nrows, ncols):
        """Construct a (nrows X ncols) matrix"""
        self.m = nrows
        self.n = ncols
        self.matrix = [[random.randint(0,9) for i in range(nrows)] for j in range(ncols)]
 #       pass

    def add(self, m):
        """return a new Matrix object after summation"""
        self.new_matrix = [[random.randint(0,9) for i in range(self.m)] for j in range(self.n)]
        for i in range(self.m):
            for j in range(self.n):
                print(self.matrix[i][j],end='  ')
                
            print("")
        
   #     pass

    #def sub(self, m):
    #    """return a new Matrix object after substraction"""
    #    pass

    #def mul(self, m):
    #    """return a new Matrix object after multiplication"""
    #    pass

    #def transpose(self):
    #    """return a new Matrix object after transpose"""
    #    pass
    
    def display(self):
    #    """Display the content in the matrix"""
        for i in range(self.m):
            for j in range(self.n):

                print(self.matrix[i][j],end='  ')
                
            print("")
    #    pass

nrow = 3
ncol = 3
A = Matrix(nrow,ncol)
B = Matrix(nrow,ncol)
A.display()
print(" "*5)
B.display()

A.add(B)

