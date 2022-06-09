class Solution:
    # Q1. Amazing Subarrays
    # You are given a string S, and you have to find all the amazing substrings of S.
    # An amazing Substring is one that starts with a vowel (a, e, i, o, u, A, E, I, O, U).
    #
    # Input
    #
    # Only argument given is string S.
    # Output
    #
    # Return a single integer X mod 10003, here X is the number of Amazing Substrings in given the string.
    # Constraints
    #
    # 1 <= length(S) <= 1e6
    # S can have special characters
    # Example
    #
    # Input
    # ABEC
    #
    # Output
    # 6
    #
    # Explanation
    # Amazing substrings of given string are :
    # 1. A
    # 2. AB
    # 3. ABE
    # 4. ABEC
    # 5. E
    # 6. EC
    # here number of substrings are 6 and 6 % 10003 = 6.
    # @param A : string
    # @return an integer
    def countAmazingSubstrings(self, A):
        n = len(A)
        count = 0
        vowels = "aeiouAEIOU"
        for i in range(n):
            if vowels.find(A[i]) != -1:
                print(A[i], i)
                count += (n - i)
        return count % 10003

    # Q2. Count Occurrences
    # Problem Description
    # Find the number of occurrences of bob in string A consisting of lowercase English alphabets.
    #
    #
    #
    # Problem Constraints
    # 1 <= |A| <= 1000
    #
    #
    # Input Format
    # The first and only argument contains the string A, consisting of lowercase English alphabets.
    #
    #
    # Output Format
    # Return an integer containing the answer.
    #
    #
    # Example Input
    # Input 1:
    #
    # "abobc"
    # Input 2:
    #
    # "bobob"
    #
    #
    # Example Output
    # Output 1:
    #
    # 1
    # Output 2:
    #
    # 2
    #
    #
    # Example Explanation
    # Explanation 1:
    #
    # The only occurrence is at second position.
    # Explanation 2:
    #
    # Bob occures at first and third position.
    # @param A : string
    # @return an integer
    def countBobOccurences(self, A):
        count = 0
        for i in range(0, len(A) - 2):
            if A[i:i + 3] == "bob":
                count += 1
        return count

    # Q3. Change character
    # Problem Description
    # You are given a string A of size N consisting of lowercase alphabets.
    #
    # You can change at most B characters in the given string to any other lowercase alphabet such that the number of distinct characters in the string is minimized.
    #
    # Find the minimum number of distinct characters in the resulting string.
    #
    #
    #
    # Problem Constraints
    # 1 <= N <= 100000
    #
    # 0 <= B < N
    #
    #
    #
    # Input Format
    # The first argument is a string A.
    #
    # The second argument is an integer B.
    #
    #
    #
    # Output Format
    # Return an integer denoting the minimum number of distinct characters in the string.
    #
    #
    #
    # Example Input
    # A = "abcabbccd"
    # B = 3
    #
    #
    #
    # Example Output
    # 2
    #
    #
    #
    # Example Explanation
    # We can change both 'a' and one 'd' into 'b'.So the new string becomes "bbcbbbccb".
    # So the minimum number of distinct character will be 2.
    def changeChar(self, A, B):
        alphabetCountMap = {}
        for i in range(len(A)):
            if A[i] in alphabetCountMap.keys():
                alphabetCountMap[A[i]] += 1
            else:
                alphabetCountMap[A[i]] = 1
        distCount = len(alphabetCountMap)
        while B > 0 and len(alphabetCountMap) > 0:
            minValKey = min(alphabetCountMap, key=lambda k: alphabetCountMap[k])
            minVal = alphabetCountMap[minValKey]
            if minVal > B:
                break
            alphabetCountMap.pop(minValKey)
            distCount -= 1
            B -= minVal
        return distCount

    # Q4. Closest Palindrome
    # Problem Description
    # Groot has a profound love for palindrome which is why he keeps fooling around with strings.
    # A palindrome string is one that reads the same backward as well as forward.
    #
    # Given a string A of size N consisting of lowercase alphabets, he wants to know if it is possible to make the given string a palindrome by changing exactly one of its character.
    #
    #
    #
    # Problem Constraints
    # 1 <= N <= 105
    #
    #
    #
    # Input Format
    # The first and only argument is a string A.
    #
    #
    #
    # Output Format
    # Return the string YES if it is possible to make the given string a palindrome by changing exactly 1 character. Else, it should return the string NO.

    # @param A : string
    # @return a strings
    def closestPalindrome(self, A):
        n = len(A)
        count = 0
        for i in range(int(n / 2)):
            if A[i] != A[n - i - 1]:
                count += 1
            if count > 1:
                return "NO"
        if count == 1:
            return "YES"
        if count == 0:
            if n % 2 == 1:
                return "YES"
            else:
                return "NO"
        return "NO"

    # Q5. Longest Common Prefix
    # Problem Description
    # Given the array of strings A, you need to find the longest string S, which is the prefix of ALL the strings in the array.
    #
    # The longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1 and S2.
    #
    # Example: the longest common prefix of "abcdefgh" and "abcefgh" is "abc".
    #
    #
    #
    # Problem Constraints
    # 0 <= sum of length of all strings <= 1000000
    #
    #
    #
    # Input Format
    # The only argument given is an array of strings A.
    #
    #
    #
    # Output Format
    # Return the longest common prefix of all strings in A.
    #
    #
    #
    # Example Input
    # Input 1:
    #
    # A = ["abcdefgh", "aefghijk", "abcefgh"]
    # Input 2:
    #
    # A = ["abab", "ab", "abcd"];
    #
    #
    # Example Output
    # Output 1:
    #
    # "a"
    # Output 2:
    #
    # "ab"
    #
    #
    # Example Explanation
    # Explanation 1:
    #
    # Longest common prefix of all the strings is "a".
    # Explanation 2:
    #
    # Longest common prefix of all the strings is "ab".
    # @param A : list of strings
    # @return a strings

    def longestCommonPrefix(self, A):
        minLen = len(A[0])
        for val in A:
            if len(val) < minLen:
                minLen = len(val)
        commonStr = ""
        for j in range(minLen):
            charFlag = True
            for i in range(1, len(A)):
                if A[i][j] != A[0][j]:
                    charFlag = False
            if charFlag:
                commonStr += A[0][j]
        return commonStr

    # Q6. String operations
    # Problem Description
    # Akash likes playing with strings. One day he thought of applying following operations on the string in the given order:
    #
    # Concatenate the string with itself.
    #     Delete all the uppercase letters.
    # Replace each vowel with '#'.
    #     You are given a string A of size N consisting of lowercase and uppercase alphabets. Return the resultant string after applying the above operations.
    #
    # NOTE: 'a' , 'e' , 'i' , 'o' , 'u' are defined as vowels.
    #
    #
    #
    # Problem Constraints
    #
    # 1<=N<=100000
    #
    #
    # Input Format
    #
    # First argument is a string A of size N.
    #
    #
    #
    # Output Format
    #
    # Return the resultant string.
    #
    #
    #
    # Example Input
    #
    # A="AbcaZeoB"
    #
    #
    #
    # Example Output
    #
    # "bc###bc###"
    #
    #
    #
    # Example Explanation
    #
    # First concatenate the string with itself so string A becomes "AbcaZeoBAbcaZeoB".
    # Delete all the uppercase letters so string A becomes "bcaeobcaeo".
    # Now replace vowel with '#'.
    #     A becomes "bc###bc###".
    # @param A : string
    # @return a strings
    def stringOps(self, A):
        # 1. concatenate
        A += A
        # print("1 : ", A)
        # 2. delete uppercase letters
        newA = []
        for char in A:
            if not 'A' <= char <= 'Z':
                newA.append(char)
        # print("2 : ", newA)
        # 3. replace vowels with #
        for i in range(len(newA)):
            if "aeiou".find(newA[i]) != -1:
                newA[i] = '#'
        # print("3 : ", newA)
        return ''.join(newA)

    # Q7. Lexicographically Largest
    # You are given a string S. You want to change it to the lexicographically largest possible string by changing some
    # of its characters. But you can only use characters of the string T as a replacement for characters of S.
    # Formally, find the lexicographically largest string you can form by replacing some(or none) of the characters of S
    # by using only the characters of string T. Note: Each character of T can be used at the most once.
    # Constraints:
    #
    # 1.   1 <= Length of S and T <= 50
    # 2.   All the alphabets of S and T are lower case (a - z)
    # Input: A string A containing S and T separated by "_" character. (See example below)
    #
    # Output: Lexicographically largest string P that can be formed by changing some or (none) characters of S using the characters of T.
    #
    # Example:
    #
    # Input:
    #
    # A : "abb_c"
    # This implies S is "abb" and T is "c".
    #
    # Output:
    #
    # P = "cbb"
    # @param A : string
    # @return a strings
    def getLargest(self, A):
        i = A.index('_')
        S = list(A[:i])
        T = sorted(A[i + 1:], reverse=True)
        # print("S,T", S, T)
        Ti = 0
        for j in range(0,len(S)):
            if Ti >= len(T):
                break
            if ord(T[Ti]) > ord(S[j]):
                S[j] = T[Ti]
                Ti += 1
        return ''.join(S)


sol = Solution()
# print(sol.countAmazingSubstrings("ABEC"))
# print(sol.countBobOccurences("bobabtbobl"))
# print(sol.changeChar("ircvscxggbwkfnqd", 2))
# print(sol.changeChar("hq", 0))
# print(sol.longestCommonPrefix(["abcdefgh", "aefghijk", "abcefgh"]))
# print(sol.stringOps("hgUe"))
print(sol.getLargest("abb_c"))