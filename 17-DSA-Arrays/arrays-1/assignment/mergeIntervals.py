# Q4. Merge Intervals
# Problem Description
# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
#
# You may assume that the intervals were initially sorted according to their start times.
#
#
#
# Problem Constraints
# 0 <= |intervals| <= 105
#
#
#
# Input Format
# First argument is the vector of intervals
#
# second argument is the new interval to be merged
#
#
#
# Output Format
# Return the vector of intervals after merging
#
#
#
# Example Input
# Input 1:
#
# Given intervals [1, 3], [6, 9] insert and merge [2, 5] .
# Input 2:
#
# Given intervals [1, 3], [6, 9] insert and merge [2, 6] .
#
#
# Example Output
# Output 1:
#
# [ [1, 5], [6, 9] ]
# Output 2:
#
# [ [1, 9] ]
#
#
# Example Explanation
# Explanation 1:
#
# (2,5) does not completely merge the given intervals
# Explanation 2:
#
# (2,6) completely merges the given intervals
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        n, i = len(intervals), 0
        newIntervals = []
        if newInterval[0] > newInterval[1]:
            newInterval[0] = newInterval[1]
            newInterval[1] = newInterval[0]
        if n == 0:
            interValList = []
            interValList.append(newInterval)
            return interValList

        while i < n:
            if newInterval[1] < intervals[i][0]:
                newIntervals.append(newInterval)
            count = 0
            while i < n and (
                    intervals[i][0] <= newInterval[0] <= intervals[i][1] or
                    intervals[i][0] <= newInterval[1] <= intervals[i][1] or
                    newInterval[0] <= intervals[i][0] <= newInterval[1] or
                    newInterval[0] <= intervals[i][1] <= newInterval[1]):
                count += 1
                i += 1
            if count == 0:
                newIntervals.append(intervals[i])
                i += 1
            else:
                interval = [0, 0]
                interval[0] = min(intervals[i - count][0], newInterval[0])
                interval[1] = max(newInterval[1], intervals[i-1][1])
                newIntervals.append(interval)
        if newInterval[0] > intervals[n - 1][1]:
            newIntervals.append(newInterval)
        return newIntervals


# A = [(1, 2), (3, 6)]
# B = (10, 8)

# A = [[1, 3], [6, 9]]
# B = [2, 5]


# A = [Interval(1, 2), Interval(3, 6)]
# B = Interval(10, 8)
# A = [ (1, 2), (8, 10) ]
# B = (3, 6)


A = [ (6037774, 6198243), (6726550, 7004541), (8842554, 10866536), (11027721, 11341296), (11972532, 14746848), (16374805, 16706396), (17557262, 20518214), (22139780, 22379559), (27212352, 28404611), (28921768, 29621583), (29823256, 32060921), (33950165, 36418956), (37225039, 37785557), (40087908, 41184444), (41922814, 45297414), (48142402, 48244133), (48622983, 50443163), (50898369, 55612831), (57030757, 58120901), (59772759, 59943999), (61141939, 64859907), (65277782, 65296274), (67497842, 68386607), (70414085, 73339545), (73896106, 75605861), (79672668, 84539434), (84821550, 86558001), (91116470, 92198054), (96147808, 98979097) ]
B = (36210193, 61984219)




sol = Solution()
print(sol.insert(A, B))
