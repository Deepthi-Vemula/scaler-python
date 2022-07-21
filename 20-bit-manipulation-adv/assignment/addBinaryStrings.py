# Q4. Add Binary Strings
# Problem Description
# Given two binary strings, return their sum (also a binary string).
# Example:
#
# a = "100"
#
# b = "11"
# Return a + b = "111".
class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, A, B):
        # reversing the strings to add them easily
        A = A[::-1]
        B = B[::-1]
        carry = False
        sumVal = ""
        al, ai, bl, bi = len(A), 0, len(B), 0
        while ai < al and bi < bl:
            if A[ai] == "1" and B[bi] == "1":
                if carry:
                    sumVal += "1"
                else:
                    sumVal += "0"
                carry = True

            elif A[ai] == "1" and B[bi] == "0":
                if carry:
                    sumVal += "0"
                else:
                    sumVal += "1"
                    carry = False

            elif A[ai] == "0" and B[bi] == "0":
                if carry:
                    sumVal += "1"
                    carry = False
                else:
                    sumVal += "0"
            else:
                if carry:
                    sumVal += "0"
                    carry = True
                else:
                    sumVal += "1"
            ai += 1
            bi += 1

        while ai < al:
            if A[ai] == "1":
                if carry:
                    sumVal += "0"
                else:
                    sumVal += "1"
            else:
                if carry:
                    sumVal += "1"
                    carry = False
                else:
                    sumVal += "0"
            ai += 1

        while bi < bl:
            if B[bi] == "1":
                if carry:
                    sumVal += "0"
                else:
                    sumVal += "1"
            else:
                if carry:
                    sumVal += "1"
                    carry = False
                else:
                    sumVal += "0"
            bi += 1

        if carry:
            sumVal += "1"

        sumVal = sumVal[::-1]
        return sumVal


# A = "100"
# B = "11"

A = "1010110111001101101000"
B = "1000011011000000111100110"
sol = Solution()
print(sol.addBinary(A, B))
