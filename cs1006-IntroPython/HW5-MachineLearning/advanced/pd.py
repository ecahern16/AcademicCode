import pandas as pd


def advancedStats(data, labels):
    '''Advanced stats should leverage pandas to calculate
    some relevant statistics on the data.

    data: numpy array of data
    labels: numpy array of labels
    '''
    # convert to dataframe
    df = pd.DataFrame(data)

    # print skew and kurtosis for every column
    skewness = df.skew(axis=0)
    kurtosis = df.kurt(axis=0)

    for i in range(0, len(data[0])):
        print("Column {} statistics: ".format(i))
        print("\tSkewness: {} \tKurtosis: {}".format(skewness[i], kurtosis[i]))

    # assign in labels
    df["labels"] = labels

    print("\n\nDataframe statistics")

    # groupby labels into "benign" and "malignant"
    df.groupby("labels")

    # collect means and standard deviations for all columns,
    # grouped by label
    mean = df.groupby("labels").mean()
    stddev = df.groupby("labels").std()

    # Print mean and stddev for Benign
    print("Benign Stats:")
    print("Mean:")
    print(mean.loc['B']) # Todo: find by label
    print("Std:")
    print(stddev.loc['B'])

    print("\n")

    # Print mean and stddev for Malignant
    print("Malignant Stats:")
    print("Mean:")
    print(mean.loc['M'])
    print("Std:")
    print(stddev.loc['M'])
