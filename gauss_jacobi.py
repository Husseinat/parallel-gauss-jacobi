import multiprocessing
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
import random
import numpy as np
import hashlib

def iteration(tuple, value):
    return tuple[0](value)

class GaussJacobiBuilder:

    def verify():
        # verification method to run before solving
        # lines criteria
        # match solution size and matrix size
        pass

    def createSolver():
        return GaussJacobiBuilder()

    def withEquations(self, equationsMatrix):
        self.equationsMatrix = equationsMatrix
        return self

    def withSolution(self, solution):
        self.solution = solution
        return self

    def solve(self, iterations):
        # initializing one ThreadPoolExecutor
        executor = ThreadPoolExecutor()

        #every equation object is a tuple that has a polynome and an identifier
        equations = [(np.poly1d([1, 2, 3]), 1), (np.poly1d([1, 2, 3]), 2), (np.poly1d([1, 2, 3]), 3), (np.poly1d([1, 2, 3]), 4), (np.poly1d([1, 2, 3]), 5)]

        #populating the ThreadPoolExecutor

        future_to_equations = {executor.submit(iteration, equation, 0): equation for equation in equations}
        for future in concurrent.futures.as_completed(future_to_equations):
            equation = future_to_equations[future]
            try:
                data = future.result()
            except Exception as exc:
                print('%r generated an exception: %s' % (equation, exc))
            else:
                print('%r equation returned %s' % (equation, data))
