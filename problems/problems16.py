# problems : 16 list merge + alternate

def merge_alternate(list1, list2):
    """Return a new list with elements from list1 and list2 alternated."""
    merged = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        merged.append(list1[i])
        merged.append(list2[j])
        i += 1
        j += 1

    # add remaining elements
    while i < len(list1):
        merged.append(list1[i])
        i += 1
    while j < len(list2):
        merged.append(list2[j])
        j += 1

    return merged


if __name__ == '__main__':
    print(merge_alternate([1,2,3,4],[10,20,30]))
    print(merge_alternate([1,3,5,7], [2,4,6]))