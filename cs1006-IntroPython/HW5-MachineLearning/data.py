import numpy as np
import sklearn
from sklearn.neighbors import NearestNeighbors, KNeighborsClassifier
from sklearn.svm import SVC


def postProcessCSV(dataset):
    '''
    Takes the dataset as an N x M numpy array.

    Modifies the dataset to:
        - strip the client ID
        - convert the float columns to be floats instead of strings
    Returns:
        - list of labels (m or b) as 1xN vector
        - rest of data as N x (M-1) matrix of floats
    '''
    # strip first column
    noFirstColumn = np.delete(dataset, [0], 1)

    # grab labels
    labels = noFirstColumn[:, 0]

    # get rest as float
    rest = noFirstColumn[:, 1:]
    rest = rest.astype(np.float)
    return labels, rest


def datasetInfo(data, labels):
    '''
    Takes the dataset and labels vector.

    Returns the following statistics as a dictionary:
        rows: N from above, as an integer
        columns: M from above, as an integer
        benign: Number of benign entries in dataset
        malignant: Number of malignant entries in dataset
    '''

    rows = data.shape[0]
    columns = data.shape[1]
    benign = 0
    mal = 0
    for n in labels:
        if n == 'B':
            benign = benign + 1
        elif n == 'M':
            mal = mal + 1
    # return a dictionary
    ret = {"rows": rows, "columns": columns, "benign": benign, "malignant": mal}

    return ret


def splitDataset(dataset, test_percentage=20):
    '''
    Takes the dataset as an N x M list of lists.

    Returns 2 subsets of the dataset:
        the first is the testing part, which should be test_percentage percent of N
        the second is the training part, which should be 100-test_percentage percent of N
    '''
    total_length = len(dataset)
    test_rows = int(total_length*(float(test_percentage)/100))
    test, train = dataset[:test_rows], dataset[test_rows:]
    return test, train