import sys
import numpy as np
import lib1743734 as lib


def create_matrix(bags, N):
    """
    Method that creates the matrix of distances given the Jaccard similarity.
    :param bags: Array of bags.
    :param N: Size of the matrix.
    :return: The distance Jaccard similarity matrix J.
    """
    D = np.ones([N, N])
    for (i, bag1) in enumerate(bags):
        for(j, bag2) in enumerate(bags):
            D[i, j] -= lib.jaccard(bag1, bag2)

    return D


def create_bag_output(bags):
    """
    Creates the sorted array of occurrences given the bags.
    :param bags: Array of bags.
    :return: The sorted array of the lengths of bags.
    """
    return sorted([len(mini_bag) for mini_bag in bags], reverse=True)


def create_clusters(clusters_list):
    """
    Creates the clusters structure. Inside each cluster we have the indices of the elements of each cluster.
    :param clusters_list: Output of method single_linkage.
    :return: The array of indices on each cluster.
    """
    clusters = {}
    for i, elem in enumerate(clusters_list):
        exist = clusters.get(elem, None)
        if exist is None:
            clusters[elem] = [i]
        else:
            clusters[elem].append(i)

    to = []
    for value in clusters.values():
        to.append(value)

    return to


def main():
    np.set_printoptions(precision=2)

    file_names = sys.argv[1:]

    '''
    1. Compute a bag of words for each document, ignoring words occurring less than 10 times.
    '''
    bags = [lib.bag(wc=lib.wordcount(filename=file), threshold=10) for file in file_names]
    print(create_bag_output(bags))

    '''
    2. Use libID.jaccard() to compute the nxn matrix J (Jaccard distance).
    '''
    J = create_matrix(bags=bags, N=len(file_names))
    print(J)
    print(J.mean(axis=None))

    '''
    3. Cluster the documents according to J, using libID.single_linkage() with k=3
    '''
    clusters = lib.single_linkage(D=J, k=3)
    print(create_clusters(clusters_list=clusters))


if __name__ == '__main__':
    main()