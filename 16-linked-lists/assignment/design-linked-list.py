# Q2. Design Linked list
# Problem Description
# Given a matrix A of size Nx3 representing operations.
# Your task is to design the linked list based on these operations.
#
# There are four types of operations:
#
# 0 x -1: Add a node of value x before the first element of the linked list.
# After the insertion, the new node will be the first node of the linked list.
# 1 x -1: Append a node of value x to the last element of the linked list.
# 2 x index: Add a node of value x before the indexth node in the linked list.
# If index equals to the length of linked list, the node will be appended to the end of linked list.
# If index is greater than the length, the node will not be inserted.
# 3 index -1: Delete the indexth node in the linked list, if the index is valid.
# A[i][0] represents the type of operation.
#
# A[i][1], A[i][2] represents the corresponding elements with respect to type of operation.
#
# Note: Indexing is 0 based.
#
#
# Problem Constraints
# 1 <= Number of operations <= 1000
# 1 <= All node values <= 109
#
#
# Input Format
# The only argument given is matrix A.
#
#
# Output Format
# Return the pointer to the starting of the linked list.
#
#
# Example Input
# Input 1:
# A = [   [0, 1, -1]
#         [1, 2, -1]
#         [2, 3, 1]   ]
# Input 2:
# A = [   [0, 1, -1]
#         [1, 2, -1]
#         [2, 3, 1]
#         [0, 4, -1]
#         [3, 1, -1]
#         [3, 2, -1]  ]
#
#
# Example Output
# Output 1:
# 1->3->2->NULL
#
# Output 2:
# 4->3->NULL



class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        head = None
        size_of_ll = 0
        n = len(A)
        for i in range(n):
            # 0 x -1: Add a node of value x before the first element of the linked list.
            # After the insertion, the new node will be the first node of the linked list.
            if A[i][0] == 0 and A[i][2] == -1:
                temp = ListNode(A[i][1])
                temp.next = head
                head = temp
                size_of_ll += 1
                # Append a node of value x to the last element of the linked list.
            elif A[i][0] == 1 and A[i][2] == -1:
                temp = ListNode(A[i][1])
                if size_of_ll == 0:
                    temp.next = head
                    head = temp
                else:
                    headPtr = head
                    while headPtr.next is not None:
                        headPtr = headPtr.next
                    headPtr.next = temp
                size_of_ll += 1
                # Add a node of value x before the indexth node in the linked list. If index equals to the length of linked list,
            # the node will be appended to the end of linked list.
            # If index is greater than the length, the node will not be inserted.
            elif A[i][0] == 2:
                position = A[i][2]
                if position >= 0 and position <= size_of_ll:
                    temp = ListNode(A[i][1])
                    if position == 0:
                        temp.next = head
                        head = temp
                    else:
                        count = 0
                        prev = head
                        while count < position - 1:
                            prev = prev.next
                            count += 1
                        temp.next = prev.next
                        prev.next = temp
                    size_of_ll += 1
            # Delete the indexth node in the linked list, if the index is valid.
            elif A[i][0] == 3 and A[i][2] == -1:
                position = A[i][1]
                if position >= 0 and position < size_of_ll:
                    temp = None
                    if position == 0:
                        temp = head
                        head = head.next
                    else:
                        count = 0
                        prev = head
                        while count < position - 1:
                            prev = prev.next
                            count += 1
                        temp = prev.next
                        prev.next = prev.next.next
                    size_of_ll -= 1
        return head


def print_ll(A):
    tmp = A
    ans = []
    while tmp is not None:
        ans.append(str(tmp.val))
        tmp = tmp.next
    print(" ".join(ans))


A = [
    [1, 13, -1],
    [3, 0, -1],
    [3, 1, -1],
    [2, 15, 0],
    [3, 0, -1],
    [1, 12, -1],
    [3, 0, -1],
    [1, 19, -1],
    [1, 13, -1],
    [3, 0, -1],
    [0, 12, -1],
    [1, 13, -1],
    [3, 2, -1]]

A1 = [
        [2, 18, 0],
        [2, 5, 1],
        [2, 8, 0],
        [1, 7, -1],
        [1, 5, -1]
    ]
sol = Solution()
val = sol.solve(A1)
print_ll(val)
