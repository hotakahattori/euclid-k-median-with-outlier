import numpy as np

class Data:

    def __init__(self):
        self.customers = []

    def add_customer(self, dimension, size, mean, var):
        self.customers += self._get_points(dimension, size, mean, var)
        self.dimension = dimension

    def _get_points(self, dimension, size, mean, var):
        points = []
        for i in range(size):
            point = np.random.normal(loc=mean, scale=var, size=dimension)
            points.append(point)
        return points
