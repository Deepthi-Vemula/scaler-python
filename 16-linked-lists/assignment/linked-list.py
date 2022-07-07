# Q1. Linked-List
# Problem Description
# Design and implement a Linked List data structure.
# A node in a linked list should have the following attributes
# - an integer value and a pointer to the next node. It should support the following operations:
#
# insert_node(position, value) - To insert the input value at the given position in the linked list.
# delete_node(position) - Delete the value at the given position from the linked list.
# print_ll() - Print the entire linked list, such that each element is followed by a single space.
# Note:
#
# If an input position does not satisfy the constraint, no action is required.
# Each print query has to be executed in a new line.
#
#
# Problem Constraints
# 1 <= position <= n where, n is the size of the linked-list.
#
#
#
# Input Format
# First line contains an integer denoting number of cases, let's say t.
# Next t line denotes the cases.
#
#
# Output Format
# When there is a case of print_ll(),  Print the entire linked list,
# such that each element is followed by a single space.
# NOTE: You don't need to return anything.
#
#
# Example Input
# 5
# i 1 23
# i 2 24
# p
# d 1
# p
#
#
# Example Output
# 23 24
# 24
#
#
# Example Explanation
# After first two cases linked list contains two elements 23 and 24.
# At third case print: 23 24.
# At fourth case delete value at first position, only one element left 24.
# At fifth case print: 24.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


head = None
size_of_ll = 0


def insert_node(position, value):
    global head
    global size_of_ll
    if 1 <= position <= size_of_ll + 1:
        temp = ListNode(value)
        if position == 1:
            temp.next = head
            head = temp
        else:
            count = 1
            prev = head
            while count < position - 1:
                prev = prev.next
                count += 1
            temp.next = prev.next
            prev.next = temp
        size_of_ll += 1


def delete_node(position):
    global head
    global size_of_ll
    if position >= 1 and position <= size_of_ll:
        temp = None
        if position == 1:
            temp = head
            head = head.next
        else:
            count = 1
            prev = head
            while count < position - 1:
                prev = prev.next
                count += 1
            temp = prev.next
            prev.next = prev.next.next
        size_of_ll -= 1


def print_ll():
    global head
    tmp = head
    ans = []
    while tmp is not None:
        ans.append(str(tmp.val))
        tmp = tmp.next
    print(" ".join(ans))


