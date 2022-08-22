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



if __name__ == "__main__":
    sample_arr = [1,2,3,4,5,6,7,8]
    print("the index of your target is: ", bin_search(sample_arr, 6, 0, len(sample_arr)-1))
