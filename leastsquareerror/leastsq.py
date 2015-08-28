"""Using Least Square Error for determining the output function"""
import numpy as np
import matplotlib.pyplot as plt

def main():
    """Main Module"""
    dataset = np.genfromtxt(open('Data/train.csv','r'), delimiter=',',
        dtype='f8')  
    y_var = dataset[:, 0]
    x_var = dataset[:, 1]
    a_mat = np.vstack([x_var, np.ones(len(x_var))]).T
    slope, intercept = np.linalg.lstsq(a_mat, y_var)[0]
    print "Y =", slope, "X", intercept
#    plt.plot(x_var, y_var, 'o', label='Original data', markersize=10)
#    plt.plot(x_var, slope*x_var + intercept, 'r', label='Fitted line')
#    plt.legend()
#    plt.show()

if __name__ == "__main__":
    main()
