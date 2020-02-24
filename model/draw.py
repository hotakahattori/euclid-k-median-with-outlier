import matplotlib.pyplot as plt

class Draw():

    def __init__(self, data, Model):
        self.data = data
        self.model = Model

    def draw_k_median_result(self):
        if self.data.dimension == 2:
            self._draw_customers()
            self._draw_candidates()
            self._draw_cluster()
            self._show()

    def _draw_customers(self):
        customers_for_plot = [[] for i in range(self.data.dimension)]
        for i in range(len(self.data.customers)):
            for d in range(self.data.dimension):
                customers_for_plot[d].append(self.data.customers[i][d])
        customers_x = customers_for_plot[0]
        customers_y = customers_for_plot[1]
        plt.plot(customers_x, customers_y, ".")

    def _draw_candidates(self):
        candidates_for_plot = [[] for i in range(self.data.dimension)]
        for i in range(len(self.model.x)):
            for d in range(self.data.dimension):
                candidates_for_plot[d].append(self.model.x[i][d].value())
        candidates_x = candidates_for_plot[0]
        candidates_y = candidates_for_plot[1]
        plt.plot(candidates_x, candidates_y, "*")

    def _draw_cluster(self):
        cluster = [[[] for d in range(self.data.dimension)] for i in range(self.model.max_candidate)]
        c = 0
        for i in range(self.model.max_candidate):
            for j in range(len(self.data.customers)):
                c += 1
                if self.model.y[i][j].value() == 1:
                    for d in range(self.data.dimension):
                        cluster[i][d].append(self.data.customers[j][d])
        for i in range(self.model.max_candidate):
            cluster_x = cluster[i][0]
            cluster_y = cluster[i][1]
            plt.plot(cluster_x, cluster_y, "x")

    def _show(self):
        plt.show()
        plt.clf()