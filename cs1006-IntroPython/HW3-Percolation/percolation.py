import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import os


def read_grid(input_file):
    """Create a site vacancy matrix from a text file.

    input_file is a file object associated with the
    text file to be read. The method should return
    the corresponding site vacancy matrix represented
    as a numpy array
    """
    return (np.loadtxt(input_file, skiprows = 1)).astype(int)


def write_grid(filename, sites):
    """Write a site vacancy matrix to a file.

    filename is a String that is the name of the
    text file to write to. sites is a numpy array
    representing the site vacany matrix to write
    """
    if os.path.isfile(filename):
        os.remove(filename)
        
    fp = open(filename, "w")
    print(format(len(sites), "d"), end='', file=fp)
    for i in sites:
        print("\n", end='', file=fp)
        for x in i:
            print(format(x, "d"), end = '', file=fp)
            print(" ", end = '', file=fp)
    fp.close()


# row, col
south = (1, 0)
east  = (0, 1)
west = (0,-1)
directions = [south, east, west]

def percolate(mat, x, y):
    ''' recursive!! '''
    
     # if x == len(mat) then you have gone below the matrix and return
    if x >= len(mat):
        return

    #if y == len(mat) then you have gone too far to the right
    if y >= len(mat):
        return

    #if x is past the first column, stop
    if x < 0:
        return

    #if y is past the first row, stop
    if y < 0:
        return

    # if 0 return because block
    if mat.item((x, y)) == 0:
        return

    # if 2 then has already been visited and return
    if mat.item((x, y)) == 2:
        return

    # if 1 then change value to 2 and explore all directions except north
    if mat.item((x, y)) == 1:
        mat.itemset((x, y), 2)

    for direction in directions:
        row = direction[0]
        col = direction[1]
        percolate(mat, x + row, y + col)


def flow(sites):
    """Returns a matrix of vacant/full sites (0=full, 1=vacant)

    sites is a numpy array representing a site vacancy matrix. This
    function should return the corresponding flow matrix generated
    through vertical percolation
    """

    for i in range(len(sites)):
        percolate(sites, 0, i)
        
    return sites



def percolates(flow_matrix):
    """Returns a boolean if the flow_matrix exhibits percolation

    flow_matrix is a numpy array representing a flow matrix
    """
    lastRow = len(flow_matrix) - 1
    for i in range(len(flow_matrix)):
        if flow_matrix.item((lastRow, i)) == 2:
            return True 
        else:
            return False


def make_sites(n, p):
    """Returns an nxn site vacancy matrix

    Generates a numpy array representing an nxn site vacancy
    matrix with site vaccancy probability p
    """
    return (np.random.random((n,n)) > p).astype(int)


def plot(before, after):
    """Plots the before and after matrices using matplotlib
    """
    fig, axes = plt.subplots(1, 2)

    axes[0].pcolor(before, cmap='Greys_r')
    axes[0].set_ylim(before.shape[0], 0)

    l = ListedColormap(['black', 'white', 'blue'])
    axes[1].pcolor(after, cmap=l)
    axes[1].set_ylim(before.shape[0], 0)
    plt.show()
