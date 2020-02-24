import pulp

class Model:

    def __init__(self, data, max_candidate):
        self.data = data
        self.make_model(max_candidate)

    def make_model(self, max_candidate):
        self.prob = pulp.LpProblem("Problem", pulp.LpMinimize)

        candidate_index = [index for index in range(max_candidate)]
        customer_index = [index for index in range(len(self.data.customer))]
        dimension_index = [i for i in range(self.data.dimension)]

        Big_M = 100000

        self.x = pulp.LpVariable.dicts("x", (candidate_index, customer_index, dimension_index))

        self.y = pulp.LpVariable.dicts("y", (candidate_index, customer_index), 0, 1, "Binary")

        self.d = pulp.LpVariable.dicts("d", (candidate_index, customer_index, dimension_index))

        obj = 0
        for i in candidate_index:
            for j in customer_index:
                for d in dimension_index:
                    obj += self.d[i][j][d]
        self.prob += obj

        for j in customer_index:
            self.prob += pulp.lpSum(self.y[i][j] for i in candidate_index) == 1

        for d in dimension_index:
            for j in customer_index:
                for i_1 in candidate_index:
                    for i_2 in candidate_index:
                        if i_1 != i_2:
                            self.prob += self.x[i_1][j][d] - self.data.customer[j][d] - Big_M * (1 - self.y[i_2][j]) <= self.d[i_2][j][d]
                            self.prob += self.data.customer[j][d] - self.x[i_1][j][d] - Big_M * (1 - self.y[i_2][j]) <= self.d[i_2][j][d]

    def solve(self):
        solver = pulp.solvers.CPLEX_CMD()
        self.prob.solve(solver)
