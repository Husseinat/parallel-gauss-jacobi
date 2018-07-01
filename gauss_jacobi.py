import multiprocessing
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
import numpy as np
import time

import sys

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

        # if match solution size and matrix size
        # matrix and solution has been set
        isValid = hasattr(self, 'equationsMatrix') and hasattr(self, 'solution') and len(self.equationsMatrix) == len(self.solution)
        if not isValid:
            return False

        # verifying if all lines have the same amount of elements
        firstLine = self.equationsMatrix[0]
        for line in self.equationsMatrix:
            if len(line) != len(firstLine):
                return False

        # if match the lines criteria
        maxNumber = (np.sum(self.equationsMatrix[0]) - self.equationsMatrix[0][0])/self.equationsMatrix[0][0]
        for lineIndex in range(1, len(self.equationsMatrix)):
            candidate = (np.sum(self.equationsMatrix[lineIndex]) - self.equationsMatrix[lineIndex][lineIndex])/self.equationsMatrix[lineIndex][lineIndex]
            if candidate > maxNumber:
                maxNumber = candidate
        if maxNumber < 1:
            return True

        # if match the columns criteria
        col = [self.equationsMatrix[i][0] for i in range(len(self.equationsMatrix))]
        maxNumber = (np.sum(col) - self.equationsMatrix[0][0])/self.equationsMatrix[0][0]
        for colIndex in range(1, len(self.equationsMatrix)):
            col = [self.equationsMatrix[i][colIndex] for i in range(len(self.equationsMatrix))]
            candidate = (np.sum(col) - col[colIndex])/col[colIndex]
            if candidate > maxNumber:
                maxNumber = candidate
        if maxNumber < 1:
            return True
        return False

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
        return self.itResult
