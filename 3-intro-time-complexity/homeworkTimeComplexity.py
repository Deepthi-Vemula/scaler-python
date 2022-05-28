# Q1. AMORTIZED2
# What is the time complexity of the following code :
#
# int j = 0;
# for(i = 0; i < n; ++i) {
#     while(j < n && arr[i] < arr[j]) {
#     j++;
#     }
# }
#
# Ans: O(n^2)
#
# Q2. AMORTIZED1
# What is the time complexity of the following code :
#
# int j = 0;
# for(int i = 0; i < n; ++i) {
#     while(j < n && arr[i] < arr[j]) {
#         j++;
#     }
# }
# Ans: O(n^2)
#
# Q3. DSA - 01
# An algorithm consists of two independent piece of code,
# having complexities f(n) and g(n) respectively.
#     What would be the complexity of the complete algorithm
# Ans: MAX( f(n), g(n) )
#
# Q4. REC_CMPL1
#
# What is the worst case time complexity of the following code :
#
#     /* * V is sorted * V.size() = N
# The function is initially called as searchNumOccurrence(V, k, 0, N-1) */
#
#                                     int searchNumOccurrence(vector &V, int k, int start, int end) {
# if (start > end) return 0;
# int mid = (start + end) / 2;
# if (V[mid] < k) return searchNumOccurrence(V, k, mid + 1, end);
# if (V[mid] > k) return searchNumOccurrence(V, k, start, mid - 1);
# return searchNumOccurrence(V, k, start, mid - 1) + 1 + searchNumOccurrence(V, k, mid + 1, end);
# }
# Ans: O(log N) - binary search algorithm
#
