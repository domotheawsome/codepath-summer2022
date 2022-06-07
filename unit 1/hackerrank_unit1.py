## question 1. 1.1

## As part of the Understand step in the UMPIRE method, what should you not be doing?

# I. Ask clarifying questions
# II. Talk through an input/output case
# III. Write some pseudocode

# Answer: III

# question 2. 1.2

## What are some helpful steps to take during the Plan step of the UMPIRE method?

# I. Think about whether any helper methods would make the solution easier to implement
# II. Draw out diagrams to hep visualize your approach
# III. Run through an example input to demonstrate how your approach would work to get the desire output

# I, II

# question 4. 1.4

# Complete the 'fizzbuzz' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def fizzbuzz(nums):
    # Write your code here
    # for loop to iterate through nums
    
    for i in range(0, len(nums)):
        if (nums[i] % 3 == 0 and nums[i] % 5 == 0):
            print("fizzbuzz")
        elif (nums[i] % 3 == 0):
            print("fizz")
        elif (nums[i] % 5 == 0):
            print("buzz")
        else:
            print(nums[i])
    
    
    # use if statements to check truth values
    # print corresponding conditions
    
# question 5. 1.5

#
# Complete the 'fibonacci' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER n as parameter.
def fibonacci(n):
    sumlist = []
    if n == 0:
        return 0;
    
    for i in range(0, n):
        sum_ = 0;
        if i ==0 or i==1:
            sumlist.append(1)
        else:
            print(i)
            sum_ += sumlist[i-2] + sumlist[i-1]
            print(sum_)
            sumlist.append(sum_)
    return sumlist[n-1]
    # Write your code here
