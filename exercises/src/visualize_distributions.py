#%%
"""Visualize the distribution of different samples."""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def plot_histogram(sample, title, bins=16, **kwargs):
    """Plot the histogram of a given sample of random values.

    Parameters
    ----------
    sample : pandas.Series
        raw values to build histogram
    title : str
        plot title/header
    bins : int
        number of bins in the histogram
    kwargs : dict 
        any other keyword arguments for plotting (optional)
    """
    # TODO: Plot histogram
    plt.hist(sample, bins=bins, density=True, alpha=0.6, color='g')

    # TODO: show the plot
    plt.show()

    return


def test_run():
    """Test run plot_histogram() with different samples."""
    # Load and plot histograms of each sample
    # Note: Try plotting them one by one if it's taking too long
    A = pd.read_csv("A.csv", header=None, squeeze=True)
    plot_histogram(A, title="Sample A")
    
    B = pd.read_csv("B.csv", header=None, squeeze=True)
    plot_histogram(B, title="Sample B")
    
    C = pd.read_csv("C.csv", header=None, squeeze=True)
    plot_histogram(C, title="Sample C")
    
    D = pd.read_csv("D.csv", header=None, squeeze=True)
    plot_histogram(D, title="Sample D")


if __name__ == '__main__':    
    ##test_run()

    # Create a random number generator with a fixed seed for reproducibility
    sample = pd.DataFrame(np.random.randint(0, 100, size=(1000, 1)))
    print(sample)

    # sample.hist(bins=3)

    # Plot the histogram
    plt.hist(sample, bins=10, density=True, alpha=0.6)

    # Plot the normal distribution curve
    mu, std = norm.fit(sample)
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    plt.plot(x, p, 'k', linewidth=2)

    # Add a legend and labels
    plt.legend(['Normal Distribution Curve', 'Histogram'])
    plt.xlabel('Random Integers')
    plt.ylabel('Frequency')
    plt.title('Histogram with Normal Distribution Curve')

    # Show the plot
    plt.show()

# %%