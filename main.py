from gauss_jacobi import GaussJacobiBuilder

# input of solution array
solution = [int(num) for num in input().strip().split(' ')]

# input of matrix
matrix = []
try:
    while True:
        matrix.append([int(num) for num in input().strip().split(' ')])
except EOFError:
    pass

print(solution)
print(matrix)

# build and solve
GaussJacobiBuilder.createSolver().withSolution(solution).withEquations(matrix).solve(1)
