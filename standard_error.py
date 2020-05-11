"""

    Ben Schedin
    Statistical Theory
    Standard Error

"""

import math
from matplotlib import pyplot as plt


def main():
    n = 1000
    sigma = 1
    samples = []

    for i in range(1, n + 1):
        samples.append(i)

    x = samples.copy()
    y = []

    for value in x:
        y.append(compute_se(value, sigma))

    plt.cla()
    plt.plot(x, y)
    plt.title("Standard Error of the Mean\nn = {}, sigma = {}".format(n, sigma))
    plt.xlabel("Sample Size")
    plt.ylabel("Standard Error")
    plt.grid()
    plt.hlines(0, 0, n)
    plt.vlines(0, 0, max(y))
    plt.vlines(30, 0, max(y))
    plt.vlines(100, 0, max(y))
    plt.show()


def compute_se(n, sigma):
    return sigma / math.sqrt(n)


if __name__ == "__main__":
    main()
