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
        time.sleep(0.1)
        sum = self.solution[line]
        return (line, sum)

    def callback(self, doneFuture):
        print("Finished task! With result " + str(doneFuture.result()))

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

        for i in range(maxIterations):
            # initializing one ThreadPoolExecutor
            executor = ThreadPoolExecutor()

            #initializing iteration result array
            self.itResult = [0 for eq in range(len(self.solution))]

            #populating the ThreadPoolExecutor
            for eq in range(len(self.solution)):
                executor.submit(self.iteration, eq, 0).add_done_callback(self.callback)

            print("Waiting the iteration to finish...")

            # the executor will be finished once all tasks are done
            executor.shutdown(wait=True)

            print("Finished!")
        return self.itResult
