# Q3. Palindrome Integer
# Problem Description
#
# Determine whether an integer is a palindrome. Do this without extra space.
#
# A palindrome integer is an integer x for which reverse(x) = x where reverse(x) is x with its digit reversed. Negative numbers are not palindromic.
#
# Example :
#
# Input : 12121
# Output : True
#
# Input : 123
# Output : False
class Solution:
    # @param A : integer
    # @return an integer
    def isPalindrome(self, A):
        # find the highest power
        if A < 0:
            return 0
        power = 1
        count = 0
        while (A / power) > 9:
            print("A / power", A / power)
            power *= 10
            count += 1
        print(power, count)
        while A and power >= 10:
            print("first and last vals", (A/power), A%10)
            if int(A / power) != int(A % 10):
                return 0
            A = int((A % power) / 10)
            power = power / 100
            # print("A, power", A, power)
        return 1


sol = Solution()
val1 = 12121
val2 = 2147447412
val3 = 12
val4 = 999
print(sol.isPalindrome(val4))
