import hashlib

# leetcode problem: https://leetcode.com/problems/top-k-frequent-elements/

## top k frequent items
# this problem has a bit of a trick to it; k isnt the number of occurences of a single item,
# it is the number of items that are the most frequent. so, for [1,2,3] and k = 3, the output
# would be [1,2,3].

# some notable edge cases are:
    # array is empty
    # array has one element
    # k = size of array

# here is my method of solving/pseudocode:
    # i see a dict as the most effective way
    # to reduce time complexity. thus, we initialize a dict
    
    # we then iterate through the list of nums and store their
    # number of occurences in the dict

    # we then iterate through the dict, sorting by descending values
    # and append the largest values to a dict and decrease k

    # when k == 0, we return the results list.


# implementation:

def find_k_elem(nums, k):

    hash = {}
    results = []

    for i in nums:
        if i not in hash:
            hash[i] = 1
        elif i in hash:
            hash[i] += 1
    
    for key, val in sorted(hash.items(), key=lambda item: item[1], reverse=True):
        if k!=0:
            results.append(key)
            k-=1

    print(results)
    return results


if __name__ == "__main__":
    find_k_elem([1,1,1,2,2,3], 2)