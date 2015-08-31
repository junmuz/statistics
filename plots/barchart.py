"""Using Least Square Error for determining the output function"""
import numpy as np
import matplotlib.pyplot as plt

def main():
    """Main Module"""
    dataset = np.genfromtxt(open('Data/train.csv','r'), delimiter=',',
        dtype='f8')  
    y_var = dataset[:, 0]
    x_var = dataset[:, 1]
    plt.bar(x_var, y_var, 0.75, color="blue")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
