"""Plotting Histogram"""
import numpy as np
import matplotlib.pyplot as plt

def main():
    """Main Module"""
    dataset = np.genfromtxt(open('Data/train.csv','r'), delimiter=',',
        dtype='f8')  
    y_var = dataset[:, 0]
    x_var = dataset[:, 1]
    pdf, bins, patches = plt.hist(x_var, 11, normed=1, facecolor="blue", alpha=1.0, cumulative=True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
