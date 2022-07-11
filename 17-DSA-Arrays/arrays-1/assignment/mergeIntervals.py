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
    def insert(self, intervals, new_interval):
        n, i = len(intervals), 0
        new_intervals = []
        newVal = []
        if new_interval[0] > new_interval[1]:
            newVal.append(new_interval[1])
            newVal.append(new_interval[0])
        else:
            newVal.append(new_interval[0])
            newVal.append(new_interval[1])
        if newVal[1] < intervals[0][0]:
            new_intervals.append(newVal)
        while i < n:
            count = 0
            while i < n and (
                    intervals[i][0] <= newVal[0] <= intervals[i][1] or intervals[i][0] <= newVal[1] <= intervals[i][1]):
                count += 1
                i += 1
            if count == 0:
                new_intervals.append(intervals[i])
                i += 1
            else:
                interval = [0 for k in range(2)]
                interval[0] = min(intervals[i - count][0], newVal[0])
                interval[1] = max(newVal[1], intervals[i-1][1])
                new_intervals.append(interval)
        if newVal[0] > intervals[n - 1][1]:
            new_intervals.append(newVal)
        return new_intervals


# A = [(1, 2), (3, 6)]
# B = (10, 8)

# A = [[1, 3], [6, 9]]
# B = [2, 5]

A = [1, 3], [6, 9]
B = [2, 6]

sol = Solution()
print(sol.insert(A, B))
