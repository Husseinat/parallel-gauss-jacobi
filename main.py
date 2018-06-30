from gauss_jacobi import GaussJacobiBuilder

solution = [int(num) for num in input().strip().split(' ')]

matrix = []
try:
    while True:
        matrix.append([int(num) for num in input().strip().split(' ')])
except EOFError:
    pass

print(solution)
print(matrix)

GaussJacobiBuilder.createSolver().withSolution(solution).withEquations(matrix).withMaxIterations(3).solve()
