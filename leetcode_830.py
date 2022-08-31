#2d matrix practice

# write a program to display a matrix

def displayMatrix(matrix):
    for i in matrix:
        print("####")
        for j in i:
          
          print(j)

def sumMatrixElem(matrix):
    sum_ = 0
    for i in matrix:
        sum_ += sum(i)
    return sum_

def addTwoMatrices(matrix):
    sum_ = 0
    


if __name__ == "__main__":
    print(sumMatrixElem([[1,2,3],[2,3,4],[3,4,5]]))