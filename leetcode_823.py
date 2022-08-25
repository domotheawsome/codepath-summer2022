def isPowerOfThree(n):
        while n > 1:
            n /= 3
            if n == 1:
                return True
        return False

if __name__ == "__main__":
    print(isPowerOfThree(28))