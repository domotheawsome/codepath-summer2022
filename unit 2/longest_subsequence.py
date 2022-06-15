# leetcode problem: https://leetcode.com/problems/longest-consecutive-sequence/

## edge cases: 
    # array is empty
    # no consecutive subsequence
    # duplicates of numbers

## method of solving/pseudocode:
    # i plan on using a dict to store each occurence of the elements
    # sort the dict by keys, increment a temp var if the next key is 
    # key+1, otherwise set the temp var to 0.
    # return this temp var, this will be the length of the longest
    # subsequence

## implementation:

def longest_subsequence(nums):

    hash = {}
    longest_length = 0
    curr_length = 0
    if nums[i] == nums[i+1]-1
    #for i in nums:
     #   if i not in hash:
      #      hash[i] = 1
       # elif i in hash:
        #   hash[i] += 1
        

  #  for key, val in sorted(hash.items()):
   #     print(key)


    return 0

if __name__ == "__main__":
    longest_subsequence([100,4,200,1,3,2])