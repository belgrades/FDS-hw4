def jaccard(s1, s2):
    return len(s1.intersection(s2))*1.0/len(s1.union(s2))
