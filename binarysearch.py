# we are going to implement this via recursion.
# thus, our parameters are the array to be recursed, the target elem, the first elem, and the last elem


# the way bin search intuitively works is by finding the middle element of each half of the array.
# compare the middle element of the array to the target
# if the middle element is equal to the target, return
# if it is greater, continue search in first half (start, middle)
# it it is less, continue search in second half (middle, end)
# this is divide and conquer, thus o(log n)

# also if left half, middle + 1. 
# right half, middle - 1

def bin_search(arr, target, start, end):
    
    print(arr, target, start, end)
    # determining the middle index of the array

    # checking if key was not found
    if start >= end:
        return -1
        
    mid = (end+start)//2
    print(mid)

    # return index if key found
    if arr[mid] == target:
        return mid

    # recurse through first half
    if arr[mid] > target:
        return bin_search(arr, target, start, mid-1)
    
    # recurse through second half
    if arr[mid] < target:
        return bin_search(arr, target, mid+1, end)

def search_insert(arr, target):

    # checking if key was not found
    start = 0
    end = len(arr)
    
    while start < end:
        
        mid = (end+start)//2
        print(mid)

        # recurse through first half
        if arr[mid] >= target:
            end = mid
        
        # recurse through second half
        else:
            start = mid+1

    return start

def missing_number(nums):

        found_nums = {}

        for i in range(0, len(nums)+1):
            found_nums[i] = 0
            
        for i in nums:
            found_nums[i] = 1
        
        for i in found_nums:
            if found_nums[i] == 0:
                return i

def missing_number_improved(nums):
        length = len(nums)
        # calculate factorial of range
        range_total = (length+1)*length//2
        
        for i in nums:
            # subtract each nums element from range total
            range_total -= i
        
        # now we have our missing element
        return range_total
    

def firstBadVersion(n):
        start = 1
        end = n
        
        while start <= end:
            
            mid = (start+end)//2
            
            # if mid is true, we move to the left
            if isBadVersion(mid):
                end = mid-1
            # if mid is false, we move to the right
            else:
                start=mid+1
        
        if(isBadVersion(mid)):
            return mid
        else:
            return mid+1


def intersection_twoArrays(nums1, nums2):
    res =[]
    dict={}
    for i in nums1:
        dict[i] +=1
    for j in nums2:
        if j in dict:
            res.append(j)
            del dict[j]
    return res



if __name__ == "__main__":
    sample_arr = [1,2,3,4,5,6,7,8]
    print("the index of your target is: ", bin_search(sample_arr, 6, 0, len(sample_arr)-1))
