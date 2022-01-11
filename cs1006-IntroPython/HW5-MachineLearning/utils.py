import numpy as np

def parseCSV(filename):
    '''
    Read the file called "filename", expected to be a csv file.
    Return the data as a list-of-lists
    '''
    file1 = open(filename, 'r')
    Lines = file1.readlines()

    ret = []    # Strips the newline character
    for line in Lines:
        my_row = line.split(",")
        ret.append(my_row)
    # return a list of lists
    return np.array(ret)


def askConfig():
    '''
    Ask the user for the following config variables:
        filename: the name of the csv file
        testpercentage: percentage of dataset to reserve for testing
        classifier: Which classifier to use in {knn, sklearn-knn, svm}

    Returns the information as a dictionary
    '''
    # return a dictionary
    filename = input("Please enter a file name:")
    testpercentage = input("Please enter a test percentage:")
    classifier = input("Please enter a classifier {knn, sklearn-knn, svm}:")

    ret = {"filename": filename, "testpercentage": testpercentage, "classifier": classifier}

    return ret
