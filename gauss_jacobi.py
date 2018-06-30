import multiprocessing
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
import random
import numpy as np

import time

class GaussJacobiBuilder:

    def iteration(self, line, value):
        time.sleep(2)
        return 1

    def callback(self, doneFuture):
        print("Finished task! With result " + str(doneFuture.result()))

    def verify():
        # verification method to run before solving
        # lines criteria
        # match solution size and matrix size
        # matrix and solution has been set
        pass

    def createSolver():
        return GaussJacobiBuilder()

    def withEquations(self, equationsMatrix):
        self.equationsMatrix = equationsMatrix
        return self

    def withSolution(self, solution):
        self.solution = solution
        return self

    def withMaxIterations(self, maxIterations):
        self.maxIterations = maxIterations
        return self

    def solve(self):
        # initializing one ThreadPoolExecutor
        executor = ThreadPoolExecutor()

        #initializing iteration counter
        self.itCounter = [0 for eq in range(len(self.solution))]

        #populating the ThreadPoolExecutor
        for eq in range(len(self.solution)):
            executor.submit(self.iteration, eq, 0).add_done_callback(self.callback)

        print("Waiting the operation to finish...")

        # the executor will be finished once all tasks are done
        executor.shutdown(wait=True)

        print("Finished!")
