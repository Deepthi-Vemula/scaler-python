# coding=utf-8
class Solution:

    #     Q1. Change Date Format
    #     Given a date string in the format Day Month Year, where:
    #
    #     Day is in the set {1st, 2nd, 3rd, 4th, 5th, 6th, 7th, 8th, 9th, …, 29th, 30th, 31th}.
    #     Month is in the set {Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec}.
    #     Year is in the inclusive range [1900, 3000].
    #
    #     Convert the date string to the format YYYY-MM-DD, where:
    #
    #     YYYY denotes the 4 digit year.
    #     MM denotes the 2 digit month.
    #     DD denotes the 2 digit day.
    #     For example:
    #
    #     1st Mar 1984 → 1984-03-01
    #     2nd Feb 2013 → 2013-02-02 4th Apr 1900 → 1900-04-04
    #
    #
    #
    #     Input Format
    #
    #     The only argument given is a String, a date in the above-mentioned format.
    #     Output Format
    #
    #     Return a String, i.e date in YYYY-MM-DD format.
    #     Constraints
    #
    #     The values of Day, Month, and Year are restricted to the value ranges specified above.
    #     The given dates are guaranteed to be valid, so no error handling is necessary.
    #     Sample Test 1
    #
    #     Input:
    #     A = 16th Mar 2068
    #     Output:
    #     2068-03-16
    #     Sample Test 2
    #
    #     Input:
    #     A = 6th Jun 1933
    #     Output:
    #     1933-06-06

    def parseDate(self, dateStr):
        dateVal = ""
        if len(dateStr) == 3:
            dateVal = "0" + dateStr[0]
        elif len(dateStr) == 4:
            dateVal = dateStr[0] + dateStr[1]
        return dateVal

    def parseMonth(self, monthStr):
        months = {
            "Jan": '01',
            "Feb": '02',
            "Mar": '03',
            "Apr": '04',
            "May": '05',
            "Jun": '06',
            "Jul": '07',
            "Aug": '08',
            "Sep": '09',
            "Oct": '10',
            "Nov": '11',
            "Dec": '12'
        }
        return months[monthStr]

    def parseYear(self, yearStr):
        return yearStr

    # @param A : string
    # @return a strings
    def changeDateFormat(self, A):
        dateArray = A.split()
        print (dateArray)
        date = self.parseDate(dateArray[0])
        month = self.parseMonth(dateArray[1])
        year = self.parseYear(dateArray[2])
        ansArray = year + "-" + month + "-" + date
        return ansArray

    # Q2. Is Dictionary?
    # Problem Description
    # Surprisingly, in an alien language, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.
    #
    # Given an array of words A of size N written in the alien language, and the order of the alphabet denoted by string B of size 26, return 1 if and only if the given words are sorted lexicographically in this alien language else, return 0.
    #
    #
    #
    # Problem Constraints
    # 1 <= N, length of each word <= 105
    #
    # Sum of the length of all words <= 2 * 106
    #
    #
    #
    # Input Format
    # The first argument is a string array A of size N.
    #
    # The second argument is a string B of size 26, denoting the order.
    #
    #
    #
    # Output Format
    # Return 1 if and only if the given words are sorted lexicographically in this alien language else, return 0.
    #
    #
    #
    # Example Input
    # Input 1:
    #
    # A = ["hello", "scaler", "interviewbit"]
    # B = "adhbcfegskjlponmirqtxwuvzy"
    # Input 2:
    #
    # A = ["fine", "none", "no"]
    # B = "qwertyuiopasdfghjklzxcvbnm"
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
    # The order shown in string B is: h < s < i for the given words. So return 1.
    # Explanation 2:
    #
    # "none" should be present after "no". Return 0.
    # @param A : list of strings
    # @param B : string
    # @return an integer
    def isDictionary(self, A, B):
        for i in range(1, len(A)):
            # we have 2 strings - A[i-1], A[i]
            minLen = min(len(A[i-1]), len(A[i]))
            for j in range(minLen):
                if B.find(A[i-1][j]) > B.find(A[i][j]):
                    return 0
                if B.find(A[i-1][j]) < B.find(A[i][j]):
                    break
            if len(A[i-1]) > len(A[i]):
                return 0
        return 1


    # Q3. Perfect Cards
    #     Problem Description
    # Tom and Harry are given N numbers, with which they play a game as a team.
    #
    # Initially, Tom chooses a particular number P from the N numbers, and he takes away all the numbers that are equal to P.
    #
    # Next, Harry chooses a different number Q, different from what Tom chose, and takes away all the numbers equal to Q from the remaining N numbers.
    #
    # They win the game if they can take all the numbers by doing the above operation once and if each of them has the same amount of numbers towards the end.
    #
    # If they win, return the string "WIN", else return "LOSE".
    #
    #
    #
    # Problem Constraints
    # 2 <= N <= 100
    #
    # 1 <= A[i] <= 100
    #
    #
    #
    # Input Format
    # The first and the only argument of input contains an integer array, A.
    #
    #
    #
    # Output Format
    # Return a string, denoting the answer.
    #
    #
    #
    # Example Input
    # Input 1:
    #
    # A = [1, 2]
    # Input 2:
    #
    # A = [1, 1, 2, 2, 3]
    #
    #
    # Example Output
    # Output 1:
    #
    # "WIN"
    # Output 2:
    #
    # "LOSE"
    #
    #
    # Example Explanation
    # Explanation 1:
    #
    # In the his turn, Tom can take 1 away, and then Harry take take 2 away. The array is empty and both of them have equal number of cards, so we can say that they have won the game.
    # Explanation 2:
    #
    # No matter how they take away the elements, >= 1 card will always remain, hence, they lose.
    # @param A : list of integers
    # @return a strings
    def solve(self, A):
        hashMap = {}
        keys = []
        for el in A:
            if el in hashMap.keys():
                hashMap[el] += 1
            else:
                hashMap[el] = 1
                keys.append(el)
        if len(keys)==2 and hashMap[keys[0]] == hashMap[keys[1]]:
            return "WIN"
        return "LOSE"


    # Q4. Colorful Number
    # Problem Description
    # Given a number A, find if it is COLORFUL number or not.
    #
    # If number A is a COLORFUL number return 1 else, return 0.
    #
    # What is a COLORFUL Number:
    #
    # A number can be broken into different contiguous sub-subsequence parts.
    # Suppose, a number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245.
    # And this number is a COLORFUL number, since product of every digit of a contiguous subsequence is different.
    #
    #
    # Problem Constraints
    # 1 <= A <= 2 * 109
    #
    #
    #
    # Input Format
    # The first and only argument is an integer A.
    #
    #
    #
    # Output Format
    # Return 1 if integer A is COLORFUL else return 0.
    #
    #
    #
    # Example Input
    # Input 1:
    #
    # A = 23
    # Input 2:
    #
    # A = 236
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
    # Possible Sub-sequences: [2, 3, 23] where
    # 2 -> 2
    # 3 -> 3
    # 23 -> 6  (product of digits)
    # This number is a COLORFUL number since product of every digit of a sub-sequence are different.
    # Explanation 2:
    #
    # Possible Sub-sequences: [2, 3, 6, 23, 36, 236] where
    # 2 -> 2
    # 3 -> 3
    # 6 -> 6
    # 23 -> 6  (product of digits)
    # 36 -> 18  (product of digits)
    # 236 -> 36  (product of digits)
    # This number is not a COLORFUL number since the product sequence 23  and sequence 6 is same.
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        hashMap = {}
        numStr = str(A)
        n = len(numStr)
        for i in range(n):
            pdt = 1
            for j in range(i, n):
                pdt *= int(numStr[j])
                if pdt in hashMap.keys():
                    return 0
                hashMap[pdt] = 1
        return 1

A1 = "16th Mar 2068"
A2 = "6th Jun 1933"
sol = Solution()
# print (sol.changeDateFormat(A1))

A3= ["hello", "scaler", "interviewbit"]
B3 = "adhbcfegskjlponmirqtxwuvzy"
A4 = ["fine", "none", "no"]
B4 = "qwertyuiopasdfghjklzxcvbnm"
# print (sol.isDictionary(A4, B4))


A5 = 12
print(sol.colorful(A5))

