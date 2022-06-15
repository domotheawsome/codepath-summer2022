#  q1. 2.1
# what is the average run time complexity of isnerting an item into a hash table?

# o(n)

# q2 2.2
# what is the space complexity of the following algorithm?

# o(n)

# q4 2.4

# what is the time complexity of the following algoirthm?

# o(n)

def singleNumber(nums):
    # Write your code here
    numberDict = {}
    for i in range(0, len(nums)):
        if nums[i] not in numberDict:
            numberDict[nums[i]] = 1
        elif nums[i] in numberDict:
            numberDict[nums[i]] += 1

    for key,value in numberDict.items():
        if value == 1:
            return key

if __name__ == "__main__":
    print(singleNumber([2,2,1]))
