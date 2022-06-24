# Q3. Construct Array

# Problem Description

# Simba has an integer array of length A. Despite having insisted alot, He is not ready to reveal the array to his friend Expert. But now, he is ready to reveal some hints about the array and challenges Expert to find the values of his hidden array. The hints revealed are as follows:

# The array is sorted by values in ascending order.
# All the elements in the array are distinct and positive (greater than 0).
# The array contains two elements B and C such that B < C.
# Difference between all adjacent (consecutive) elements are equal.
# Among all the arrays satisfying the above conditions, his array has the minimum possible maximum element value.
# If there are multiple possible arrays, his array will have minimum possible minimum element value.
# Can you help Expert to construct such an array and surprise Simba?



# Problem Constraints

# 2 <= A <= 50

# 1 <= B < C <= 50



# Input Format

# First argument is an integer A.

# Second argument is an integer B.

# Third argument is an integer C.



# Output Format

# Return a sorted integer array having length N, denoting Simba's Secret Array.

# Example Input

# Input 1:

#  A = 5
#  B = 20
#  C = 50 
# Input 2:

#  A = 2
#  B = 2
#  C = 3 


# Example Output

# Output 1:

#  [10, 20, 30, 40, 50]
# Output 2:

#  [2, 3]


# Example Explanation

# Explanation 1:

#  Sorted array = [10, 20, 30, 40, 50] satisfies all the conditions having maximum value = 50 minimum possible.
#  Other arrays such as [20, 30, 40, 50, 60] having max value = 60 or [20, 50, 80, 120] having max value = 120, also satisfy conditions but their maximum value is not minimum possible(As minimum possible max value is 50). 
# Explanation 2:

#  As the array has only 2 elements, [2, 3] is the only possible candidate.
def generateAP(start, diff, count):
    A = []
    for i in range(count):
        A.append(start + (i*diff))
    return A
def getFactors(val):
    A = []
    n = 1
    while n*n <= val:
        if int(val/n) == val/n:
            A.append(n)
            A.append(int(val/n))
        n += 1
    A.sort()
    return A
        
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        diff = C - B
        #check for all the factors of the difference between these numbers
        val = 1
        factors = getFactors(diff)
        # print("factors:",factors)
        for val in factors:
            maxVal = B + (A-1)*val
            # print("diff, val", diff, val)
            if maxVal >= C:
                # print("yes, factor")
                if maxVal == C:
                    return generateAP(B, val, A)
                else:
                    #prepend to the array
                    n1 = A - (int(diff/val) + 1)
                    tempn = n1
                    A1, A2, AP = [], [], []
                    s1, s2 = B - val, C + val
                    # print("n1", n1, s1, s2)
                    while s1>0 and n1>0:
                        A1.append(s1)
                        s1 -= val
                        n1 -= 1
                    # print("pre array", n1, A1)
                    #append to the array
                    while n1>0:
                        A2.append(s2)
                        s2 += val
                        n1 -= 1
                    # print("val left ", A-tempn)
                    AP = A1[::-1]
                    AP += generateAP(B, val, A - tempn)
                    AP += A2
                    # print("post array", n1, A2)
                    # print("whole array", AP)
                    return AP
        return []
sol = Solution()
A, B, C = 5, 20, 50
A2, B2, C2 = 5, 17, 32
A3, B3, C3 = 10, 39, 68
print(sol.solve(A3, B3, C3))