import os
os.sys.path.append(".")
from model.data import Data
import model.euclid_k_median
import model.euclid_k_median_with_outlier
import model.draw

if __name__ == "__main__":
    data = Data()
    data.add_customer(dimension=2, size=8, mean=0, var=1)
    data.add_customer(dimension=2, size=8, mean=10, var=1)
    data.add_customer(dimension=2, size=8, mean=20, var=1)
    model_k_median = model.euclid_k_median.Model(data=data, max_candidate=3)
    model_k_median.solve()
    draw_k_median = model.draw.Draw(data=data, Model=model_k_median)
    draw_k_median.draw_k_median_result()