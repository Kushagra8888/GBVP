__author__ = 'kushasharma'

import pandas as pd
from GBVP import GBVP

#Sample matrix as given in GBVP Navathe paper
SAMPLE_MAT = [[ 75,  25,  25,   0,  75,   0,  50,  25,  25,   0],
              [ 25, 110,  75,   0,  25,   0,  60, 110,  75,   0],
              [ 25,  75, 115,  15,  25,  15,  25,  75, 115,  15],
              [ 0,    0,  15,  40,   0,  40,   0,   0,  15,  40],
              [ 75,  25,  25,   0,  75,   0,  50,  25,  25,   0],
              [ 0,    0,  15,  40,   0,  40,   0,   0,  15,  40],
              [ 50,  60,  25,   0,  50,   0,  85,  60,  25,   0],
              [ 25, 110,  75,   0,  25,   0,  60, 110,  75,   0],
              [ 25,  75, 115,  15,  25,  15,  25,  75, 115,  15],
              [  0,   0,  15,  40,   0,  40,   0,   0,  15,  40]]

# USE_DATA = pd.read_csv("..\..\Data\\test data.csv", sep = ";")
# USE_DATA = pd.read_csv("..\..\Data\\slicing_table.csv")
# USE_DATA = pd.read_csv("..\..\Data\\slicing_table2.csv")
# USE_DATA = pd.read_csv("..\..\Data\\dataset2.csv")
USE_DATA = pd.read_csv("..\..\Data\\adult-dataset-data.csv")


def mean_square_contingency_coefficient(attr1, attr2):
    """
     Computes the mean square contingency coefficient between two attributes
     based on an empirical formula

     Input: Two lists representing two attributes
     Output: A  numerical value between 0 and 1 representing the correlation value.
    """
    length = len(attr1)
    combined = [(attr1[idx], attr2[idx]) for idx in range(length)]
    attr1_unq = list(set(attr1))
    attr2_unq = list(set(attr2))
    dom1 = len(attr1_unq)
    dom2 = len(attr2_unq)
    combined_unq = list(set(combined))
    mscc = 0.0
    for idx1 in range(dom1):
        for idx2 in range(dom2):
            f_ij = combined.count((attr1_unq[idx1], attr2_unq[idx2])) / float(length)
            f_i  = attr1.count(attr1_unq[idx1]) / float(length)
            f_j = attr2.count(attr2_unq[idx2]) / float(length)
            mscc += ((f_ij - f_i * f_j) ** 2 )/ (f_i * f_j)
    return mscc / (min(dom1, dom2) - 1)

def compute_correlation_distance_matrix(dataset):
    """
    Takes a set of attributes and computes the pairwise contingency coefficient

    Input:  A pandas dataframe
    Output: A dataframe with rows and columns corresponding to attributes and
            values representing mean square contingency coefficient between
            the pair of attributes.
    """
    col_names = dataset.columns
    data_values = dataset.values.T
    correlation_matrix = [[1 - mean_square_contingency_coefficient(data_values[idx1].tolist(), data_values[idx2].tolist()) for idx1 in range(len(data_values))] for idx2 in range(len(data_values))]
    return pd.DataFrame(correlation_matrix, columns = col_names, index = col_names)

def compute_gbvp_clusters(distance_matrix):
    """
    Paritions the attributes of a data frame using GBVP.

    Input:A dataftame representing a distance matrix between sets of attributes
    Output: A list of lists representing the partioned columns
    """
    return [[distance_matrix.columns[idx] for idx in a_partition] for a_partition in GBVP.get_components(distance_matrix.values.tolist())]


cor_mat = compute_correlation_distance_matrix(USE_DATA)
print cor_mat
print compute_gbvp_clusters(cor_mat)
