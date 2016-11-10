import numpy as np


def jaccard(s1, s2):
    """
    Calculates the jaccard similarity between two sets.
    Assuming s1 and s2 are sets.
    :param s1: Set 1.
    :param s2: Set 2.
    :return: Returns the Jaccard similarity between two sets s1 and s2.
    """
    if isinstance(s1, set) and isinstance(s2, set):
        return len(s1.intersection(s2))*1.0/len(s1.union(s2))
    else:
        raise "s1 or s2 are not sets. Exit!"


def wordcount(filename):
    """
    Compute a wordcount of the content of filename.
    :param filename: Name of the file to count.
    :return: Python dict associating to each word that happens in filename the number of its occurrences.
    """
    import re
    from collections import Counter
    import string

    # Open file using encoding utf-8
    file = open(filename, "r", encoding="ISO-8859-1")

    lines = file.read()

    # Replace every char that is not numeric or letter to space
    clean = lines
    clean = clean.replace('\n', ' ')
    clean = clean.replace('\t', ' ')
    clean = clean.replace('\r', ' ')
    clean = re.sub('[{}]'.format(string.punctuation), " ", clean)

    # Close file
    file.close()

    return dict(Counter(clean.lower().strip().split()))


def bag(wc, threshold=1):
    """
    Creates a bag of words from the given word count dictionary.
    :param wc: Wordcount wc, output of method wordcount(filename)
    :param threshold: The word is in the bag if occurred at least threshold times.
    :return:  Python set containing all the words who satisfy the criteria.
    """
    return set([k for (k, v) in wc.items() if v >= threshold])


def single_linkage(D, k=2):
    """
    Implementation of the single-linkage clustering algorithm.
    :param D: Matrix nxn of distances.
    :param k: Number of clusters.
    :return: Array or list whose i-th entry is the cluster ID of the i-th element.
    """
    shape = D.shape
    N = shape[0]
    di = np.diag_indices(N)
    D[di] = 1.0
    clusters = np.array(range(N))

    while N > k:
        idx = np.array(range(N))
        N -= 1
        p = N - 1
        ci, cj = np.unravel_index(D.argmin(), D.shape)
        nidx = idx[(idx != ci) & (idx != cj)]
        M = np.ones((N, N))
        M[0:p, 0:p] = D[np.ix_(nidx, nidx)]

        for id, elem in enumerate(nidx):
            value = min(D[elem, ci], D[elem, cj])
            M[id, p], M[p, id] = value, value

        # Update clusters
        mone = np.where((clusters > ci) & (clusters < cj))[0]
        mtwo = np.where(clusters > cj)[0]
        pmaxi = np.where(clusters == cj)[0]
        pmini = np.where(clusters == ci)[0]

        clusters[mone] -= 1
        clusters[mtwo] -= 2
        clusters[pmaxi] = p
        clusters[pmini] = p

        D = M

    return clusters