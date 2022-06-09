import math


class Solution:
    # Q1. Reverse the String
    # Problem Description
    # You are given a string A of size N.
    #
    # Return the string A after reversing the string word by word.
    #
    # NOTE:
    #
    # A sequence of non-space characters constitutes a word.
    # Your reversed string should not contain leading or trailing spaces, even if it is present in the input string.
    # If there are multiple spaces between words, reduce them to a single space in the reversed string.
    #
    #
    # Problem Constraints
    # 1 <= N <= 3 * 105
    #
    #
    #
    # Input Format
    # The only argument given is string A.
    #
    #
    #
    # Output Format
    # Return the string A after reversing the string word by word.
    #
    #
    #
    # Example Input
    # Input 1:
    # A = "the sky is blue"
    # Input 2:
    # A = "this is ib"
    #
    #
    # Example Output
    # Output 1:
    # "blue is sky the"
    # Output 2:
    # "ib is this"
    #
    #
    # Example Explanation
    # Explanation 1:
    # We reverse the string word by word so the string becomes "the sky is blue".
    # Explanation 2:
    # We reverse the string word by word so the string becomes "this is ib".

    def reverseString(self, A, start, end):
        if start >= end:
            return A
        mid = int((start+end)/2)
        for i in range(start, mid+1):
            temp = A[i]
            A[i] = A[end]
            A[end] = temp
            end -= 1
        return A

    # @param A : string
    # @return a strings
    def reverseWords(self, A):
        A = list(A)
        n = len(A)
        revString = []
        # reverse the whole string
        A = self.reverseString(A, 0, n - 1)
        # reverse words
        index = 0
        in1 = 0
        while index < n:
            while index < n and A[index] == ' ':
                index += 1
            start = index
            while index < n and A[index] != ' ':
                index += 1
            A = self.reverseString(A, start, index-1)
            revString.append(''.join(A[start:index]))
            index += 1
        revString = ' '.join(revString)
        # remove preceding and trailing spaces
        return revString

    # Q2. Simple Reverse
    # Problem Description
    # Given a string A, you are asked to reverse the string and return the reversed string.
    #
    #
    #
    # Problem Constraints
    # 1 <= |A| <= 105
    #
    # String A consist only of lowercase characters.
    #
    #
    #
    # Input Format
    # First and only argument is a string A.
    #
    #
    #
    # Output Format
    # Return a string denoting the reversed string.
    #
    #
    #
    # Example Input
    # Input 1:
    #
    # A = "scaler"
    # Input 2:
    #
    # A = "academy"
    #
    #
    # Example Output
    # Output 1:
    #
    # "relacs"
    # Output 2:
    #
    # "ymedaca"
    #
    #
    # Example Explanation
    # Explanation 1:
    #
    # Reverse the given string.

    # @param A : string
    # @return a strings
    def solve2(self, A):
        A = list(A)
        n = len(A)
        # reverse the whole string
        A = self.reverseString(A, 0, n - 1)
        return ''.join(A)


    # Q3. Rotate string
    # Problem Description
    # Given a string A, rotate the string B times in clockwise direction and return the string.
    #
    #
    #
    # Problem Constraints
    #
    # 1 <= |A| <= 105
    #
    # 1 <= B <= 109
    #
    # String A consist only of lowercase characters.
    #
    #
    #
    # Input Format
    #
    # First and only argument is a string A.
    #
    #
    #
    # Output Format
    #
    # Return a string denoting the rotated string.
    #
    #
    #
    # Example Input
    #
    # Input 1:
    #
    # A = "scaler"
    # B = 2
    # Input 2:
    #
    # A = "academy"
    # B = 7
    #
    #
    # Example Output
    #
    # Output 1:
    #
    # "erscal"
    # Output 2:
    #
    # "academy"
    #
    #
    # Example Explanation
    #
    # Explanation 1:
    #
    # Rotate the given string twice so the string becomes "erscal".
    # @param A : string
    # @param B : integer
    # @return a strings
    def rotateClockWise(self, A, B):
        A = list(A)
        n = len(A)
        revString = []
        # reverse the whole string
        B = B%n
        A = self.reverseString(A, 0, n - 1)
        A = self.reverseString(A, 0, B-1)
        A = self.reverseString(A, B, n-1)
        return ''.join(A)

    # Q4. tolower()
    # Problem Description
    # You are given a function to_lower() which takes a character array A as an argument.
    #
    # Convert each character of A into lowercase characters if it exists. If the lowercase of a character does not exist, it remains unmodified.
    # The uppercase letters from A to Z are converted to lowercase letters from a to z respectively.
    #
    # Return the lowercase version of the given character array.
    #
    #
    #
    # Problem Constraints
    # 1 <= |A| <= 105
    #
    #
    #
    # Input Format
    # The only argument is a character array A.
    #
    #
    #
    # Output Format
    # Return the lowercase version of the given character array.
    #
    #
    #
    # Example Input
    # Input 1:
    #
    # A = ['S', 'c', 'A', 'l', 'e', 'r', 'A', 'c', 'a', 'D', 'e', 'm', 'y']
    # Input 2:
    #
    # A = ['S', 'c', 'a', 'L', 'e', 'r', '#', '2', '0', '2', '0']
    #
    #
    # Example Output
    # Output 1:
    #
    # ['s', 'c', 'a', 'l', 'e', 'r', 'a', 'c', 'a', 'd', 'e', 'm', 'y']
    # Output 2:
    #
    # ['s', 'c', 'a', 'l', 'e', 'r', '#', '2', '0', '2', '0']
    #
    #
    # Example Explanation
    # Explanation 1:
    #
    # All the characters in the returned array are in lowercase alphabets.
    # @param A : list of characters
    # @return a list of characters
    def to_lower(self, A):
        n = len(A)
        for i in range(n):
            if 'A' <= A[i] <= 'Z':
                A[i] = chr(ord('a') + ord(A[i]) - ord('A'))
        return A

    # Q5. toupper()
    # Problem Description
    # You are given a function to_upper() consisting of a character array A.
    #
    # Convert each charater of A into Uppercase character if it exists. If the Uppercase of a character does not exist, it remains unmodified.
    # The lowercase letters from a to z is converted to uppercase letters from A to Z respectively.
    #
    # Return the uppercase version of the given character array.
    #
    #
    #
    # Problem Constraints
    # 1 <= |A| <= 105
    #
    #
    #
    # Input Format
    # Only argument is a character array A.
    #
    #
    #
    # Output Format
    # Return the uppercase version of the given character array.
    #
    #
    #
    # Example Input
    # Input 1:
    #
    # A = ['S', 'c', 'A', 'L', 'E', 'r', 'A', 'c', 'a', 'D', 'e', 'm', 'y']
    # Input 2:
    #
    # A = ['S', 'c', 'a', 'L', 'e', 'R', '#', '2', '0', '2', '0']
    #
    #
    # Example Output
    # Output 1:
    #
    # ['S', 'C', 'A', 'L', 'E', 'R', 'A', 'C', 'A', 'D', 'E', 'M', 'Y']
    # Output 2:
    #
    # ['S', 'C', 'A', 'L', 'E', 'R', '#', '2', '0', '2', '0']
    #
    #
    # Example Explanation
    # Explanation 1:
    #
    # All the characters in the returned array are in uppercase alphabets.
    # @param A : list of characters
    # @return a list of characters
    def to_upper(self, A):
        n = len(A)
        for i in range(n):
            if 'a' <= A[i] <= 'z':
                A[i] = chr(ord('A') + ord(A[i]) - ord('a'))
        return A

    # Q6. Isalnum()
    # Problem Description
    # You are given a function isalpha() consisting of a character array A.
    #
    # Return 1 if all the characters of a character array are alphanumeric (a-z, A-Z, and 0-9) else, return 0.
    #
    #
    #
    # Problem Constraints
    # 1 <= |A| <= 105
    #
    #
    #
    # Input Format
    # Only argument is a character array A.
    #
    #
    #
    # Output Format
    # Return 1 if all the characters of the character array are alphanumeric (a-z, A-Z and 0-9), else return 0.
    #
    #
    #
    # Example Input
    # Input 1:
    #
    # A = ['S', 'c', 'a', 'l', 'e', 'r', 'A', 'c', 'a', 'd', 'e', 'm', 'y', '2', '0', '2', '0']
    # Input 2:
    #
    # A = ['S', 'c', 'a', 'l', 'e', 'r', '#', '2', '0', '2', '0']
    #
    #
    # Example Output
    # Output 1:
    #
    # 1
    # Output 2:
    #
    # 0
    #
    #
    # Example Explanation
    # Explanation 1:
    #
    # All the characters are alphanumeric.
    # Explanation 2:
    #
    # All the characters are NOT alphabets i.e ('#').
    # @param A : list of characters
    # @return an integer
    def Isalnum(self, A):
        n = len(A)
        for i in range(n):
            if not('a' <= A[i] <= 'z' or 'A' <= A[i] <= 'Z' or '0' <= A[i] <= '9'):
                return 0
        return 1

    # Q7. Isalpha()
    # Problem Description
    # You are given a function isalpha() consisting of a character array A.
    #
    # Return 1 if all the characters of the character array are alphabetical (a-z and A-Z), else return 0.
    #
    #
    #
    # Problem Constraints
    #
    # 1 <= |A| <= 105
    #
    #
    #
    # Input Format
    #
    # Only argument is a character array A.
    #
    #
    #
    # Output Format
    #
    # Return 1 if all the characters of the character array are alphabetical (a-z and A-Z), else return 0.
    #
    #
    #
    # Example Input
    #
    # Input 1:
    #
    # A = ['S', 'c', 'a', 'l', 'e', 'r', 'A', 'c', 'a', 'd', 'e', 'm', 'y']
    # Input 2:
    #
    # A = ['S', 'c', 'a', 'l', 'e', 'r', '#', '2', '0', '2', '0']
    #
    #
    # Example Output
    #
    # Output 1:
    #
    # 1
    # Output 2:
    #
    # 0
    #
    #
    # Example Explanation
    #
    # Explanation 1:
    #
    # All the characters are alphabets.
    # Explanation 2:
    #
    # All the characters are NOT alphabets i.e ('#', '2', '0', '2', '0').
    # @param A : list of characters
    # @return an integer
    def Isalpha(self, A):
        n = len(A)
        for i in range(n):
            if not('a' <= A[i] <= 'z' or 'A' <= A[i] <= 'Z'):
                return 0
        return 1

sol = Solution()
str1 = "crulgzfkif gg ombt vemmoxrgf qoddptokkz op xdq hv "
print(sol.reverseWords(str1))
