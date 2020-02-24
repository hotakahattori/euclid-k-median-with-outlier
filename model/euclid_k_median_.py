import pulp

class Model:

    def __init__(self, data, max_candidate):
        self.data = data
        self.max_candidate = max_candidate
        self.make_model(max_candidate)

    def make_model(self, max_candidate):
        self.prob = pulp.LpProblem("Problem", pulp.LpMinimize)

        candidate_index = [index for index in range(max_candidate)]
        customer_index = [index for index in range(len(self.data.customers))]
        dimension_index = [i for i in range(self.data.dimension)]

        Big_M = 100

        self.x = pulp.LpVariable.dicts("x", (candidate_index, dimension_index))

        self.y = pulp.LpVariable.dicts("y", (candidate_index, customer_index), lowBound=0, upBound=1, cat="Binary")

        self.d = pulp.LpVariable.dicts("d", (candidate_index, customer_index, dimension_index), lowBound=0)

        obj = 0
        for i in candidate_index:
            for j in customer_index:
                for d in dimension_index:
                    obj += self.d[i][j][d]
        self.prob += obj

        for j in customer_index:
            self.prob += pulp.lpSum(self.y[i][j] for i in candidate_index) >= 1

        for j in customer_index:
            for i in candidate_index:
                for d in dimension_index:
                    self.prob += self.x[i][d] - self.data.customers[j][d] - Big_M * (1 - self.y[i][j]) <= self.d[i][j][d]
                    self.prob += self.data.customers[j][d] - self.x[i][d] - Big_M * (1 - self.y[i][j]) <= self.d[i][j][d]

    def solve(self):
        solver = pulp.solvers.CPLEX_CMD()
        self.prob.solve(solver)
        print(self.prob.status)
        for i in range(3):
            for j in range(12):
                print(self.y[i][j].value())
                print("a")