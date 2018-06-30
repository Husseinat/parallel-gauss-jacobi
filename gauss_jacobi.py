import multiprocessing
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
import random
import numpy as np

import time

class GaussJacobiBuilder:

    def createSolver():
        return GaussJacobiBuilder()

    def iteration(self, line, value):
        sum = self.solution[line]
        for i in range(len(self.solution)):
            if i != line:
                sum -= self.equationsMatrix[line][i]*self.itResult[i]
        return (line, sum/self.equationsMatrix[line][line])

    def callback(self, doneFuture):
        line, result = doneFuture.result()
        self.itResult[line] = result

    def verify(self):
        # verification method to run before solving
        # lines criteria
        # match solution size and matrix size
        # matrix and solution has been set
        return True


    def withEquations(self, equationsMatrix):
        self.equationsMatrix = equationsMatrix
        return self

    def withSolution(self, solution):
        self.solution = solution
        return self

    def solve(self, maxIterations):
        # make verification
        if not self.verify():
            return None

        self.maxIterations = maxIterations

        #initializing iteration result array
        self.itResult = [0 for eq in range(len(self.solution))]

        for i in range(maxIterations):
            # initializing one ThreadPoolExecutor
            executor = ThreadPoolExecutor()

            #populating the ThreadPoolExecutor
            for eq in range(len(self.solution)):
                executor.submit(self.iteration, eq, 0).add_done_callback(self.callback)

            # the executor will be finished once all tasks are done
            executor.shutdown(wait=True)

            print(self.itResult)
        return self.itResult
