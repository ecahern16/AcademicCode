from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC


def SKLearnKnnClassifier(training, testing, training_labels, testing_labels, k):
    '''leverage Scikit-learn to implement the k nearest neighbors algorithm
    Args:
        training: the subset of data corresponding to the training data as a numpy matrix
        testing:  the subset of data corresponding to the testing data as a numpy matrix
        training_labels: the labels for the training data as a numpy array
        testing_labels: the labels for the testing data as a numpy array
        k: the number of nearest neighbors to use

    This should instantiate the class from scikit learn, then call
    `.fit` and `.predict`. It should then compare results similar to
    NNClassifier to return a % correct.
    
    See how easy it is to use scikit learn?
    '''
    # instantiate model
    model = KNeighborsClassifier(n_neighbors=k)

    # fit model to training data
    model.fit(training, training_labels)

    # predict test labels
    predict_test_labels = model.predict(testing)

    # return % where prediction matched actual
    return sum(predict_test_labels == testing_labels) / len(testing_labels) * 100


def SKLearnSVMClassifier(training, testing, training_labels, testing_labels):
    '''leverage Scikit-learn to implement the support vector machine classifier
    Args:
        training: the subset of data corresponding to the training data as a numpy matrix
        testing:  the subset of data corresponding to the testing data as a numpy matrix
        training_labels: the labels for the training data as a numpy array
        testing_labels: the labels for the testing data as a numpy array

    This should instantiate the class from scikit learn, then call
    `.fit` and `.predict`. It should then compare results similar to
    NNClassifier to return a % correct.
    
    See how easy it is to use scikit learn?
    '''
    # instantiate model
    model = SVC()

    # fit model to training data
    model.fit(training, training_labels)

    # predict test labels
    predict_test_labels = model.predict(testing)

    # return % where prediction matched actual
    return sum(predict_test_labels == testing_labels) / len(testing_labels) * 100
