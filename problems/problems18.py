# problem : 18 merge alternate practice
# 2. when one list is lger than other
def merge_alternate(list1,list2):
    merged = []
    i = 0
    j = 0 
    while i < len(list1) and j < len(list2):
        merged.append(list1[i])
        merged.append(list2[j])
        i = i+1
        j = j+1
        while i < len(list1): ## matonsathi same yake hakodh andre uldiro elements add madakay means yav list uddha ede adhrudh copy paste madkobeku
         merged.append(list1[i])
         i = i + 1
        return merged
print(merge_alternate([5,6,7],[50]))