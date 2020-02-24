import os
os.sys.path.append(".")
from model.data import Data
import model.euclid_k_median_
import model.draw

if __name__ == "__main__":
    data = Data()
    data.add_customer(dimension=2, size=4, mean=0, var=1)
    data.add_customer(dimension=2, size=4, mean=10, var=1)
    data.add_customer(dimension=2, size=4, mean=20, var=1)
    model_k_median = model.euclid_k_median_.Model(data=data, max_candidate=3)
    model_k_median.solve()
    draw = model.draw.Draw(data=data, Model=model_k_median)
