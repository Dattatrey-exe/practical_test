# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        res = dummy
        carry = 0

        while l1 or l2 or carry:
            total = carry

            if l1:
                total += l1.val
                l1 = l1.next

            if l2:
                total += l2.val
                l2 = l2.next

            carry = total // 10
            digit = total % 10

            dummy.next = ListNode(digit)
            dummy = dummy.next

        return res.next

def create_linked_list(arr):
    # "Convert list to linked list"
    dummy = ListNode()
    current = dummy
    for num in arr:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

def print_linked_list(node):
    while node:
        print(node.val, end= "->")
        node = node.next
    print("None")

#Test Code
l1 = create_linked_list([2,4,3])
l2 = create_linked_list([5,6,4])

solution = Solution()
result = solution.addTwoNumbers(l1, l2)

print("Result Linked List")
print_linked_list(result)

# O/p - Result Linked List
        # 7->0->8->None