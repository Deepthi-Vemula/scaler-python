class BitManipulation:
    def __init__(self):
        pass

    # Assignment Q1
    # Given an array of integers A,
    # every element appears twice except for one.
    # Find that integer that occurs once.
    #
    # NOTE: Your algorithm should have a linear runtime complexity.
    # Could you implement it without using extra memory?
    def findMissingNumber(self, arr):
        val = arr[0]
        for i in range(1, len(arr)):
            val = val ^ arr[i]
        return val

    # Assignment Q2
    # Write a function that takes an integer and returns the number of 1 bits it has.
    def find1Bits(self, num):
        cnt = 0
        while num > 0:
            if num & 1 == 1:
                cnt = cnt + 1
            num = num >> 1
        return cnt

    # Homework Q1
    # Given two binary strings, return their sum (also a binary string).
    def addBinaryStrings1(self, A, B):
        minLen = min(len(A), len(B))
        Ai = len(A) - 1
        Bi = len(B) - 1
        C = ""
        c = 0
        baseAsciiVal = ord('0')
        for i in range(minLen):
            a = ord(A[Ai]) - baseAsciiVal
            b = ord(B[Bi]) - baseAsciiVal
            sumBit = (a ^ b) ^ c
            c = (a & b) | (c & (a | b))
            C = C + chr(sumBit)
        # TODO: add values of largest string
        C = C + chr(c)
        C = C[::-1]
        return C

    def addBinaryStrings2(self, A, B):
        A = int(A, 2)
        B = int(B, 2)
        C = A + B
        binC = bin(C)[2:]
        return binC

    # Homework Q2
    # Given a positive integer A,
    # the task is to count the total number of set bits
    # in the binary representation of all the numbers from 1 to A.
    # Return the count modulo 109 + 7.
    def countSetBitsTillA(self, A):
        count = 0
        for i in range(1, A + 1):
            count = count + self.find1Bits(i)
        return count


bm = BitManipulation()
arr = [1, 2, 2, 4, 1, 3, 4, 5, 6, 6, 3]
print(bm.findMissingNumber(arr))
print(bm.find1Bits(11))
print(bm.addBinaryStrings2("100", "111"))
print(bm.countSetBitsTillA(1))
