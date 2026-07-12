# problem:17 merge and alter practice
# 1.Write a Python function to merge two lists alternately.
def merge_alternate(list1,list2):
    merged = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        merged.append(list1[i])
        merged.append(list2[j])
        i = i+1
        j = j+1
    return merged
print(merge_alternate([1,2,3],[10,20,30]))
