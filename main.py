from gauss_jacobi import GaussJacobiBuilder

#input of number of iterations
maxIterations = int(input().strip())

# input of solution array
solution = [int(num) for num in input().strip().split(' ')]

# input of matrix
matrix = []
try:
    while True:
        matrix.append([int(num) for num in input().strip().split(' ')])
except EOFError:
    pass

# build and solve
result = GaussJacobiBuilder.createSolver().withSolution(solution).withEquations(matrix).solve(maxIterations)
print(result)
