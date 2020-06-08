# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

# # Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def addTwoNumbers(self, l1, l2):
        self.l1 = l1
        self.l2 = l2
        temp = self.l1.val + self.l2.val
        carry = temp // 10
        temp %= 10
        result = ListNode(val=temp)
        node = result
        if self.l1.next == None and self.l2.next == None and carry:
            node.next = ListNode(val=carry)
            node = node.next
        self.l1 = self.l1.next
        self.l2 = self.l2.next
        while self.l1 and self.l2:
            temp = self.l1.val + self.l2.val + carry
            carry = temp // 10
            temp %= 10
            node.next = ListNode(val=temp)
            node = node.next
            if self.l1.next == None and self.l2.next == None and carry:
                node.next = ListNode(val=carry)
                break

            self.l1 = self.l1.next
            self.l2 = self.l2.next

        if not self.l1:
            while self.l2:
                temp = self.l2.val + carry
                carry = temp // 10
                temp %= 10
                node.next = ListNode(val=temp)
                node = node.next
                if self.l2.next == None and carry:
                    node.next = ListNode(val=carry)
                    break
                self.l2 = self.l2.next

        elif not self.l2:
            while self.l1:
                temp = self.l1.val + carry
                carry = temp // 10
                temp %= 10
                node.next = ListNode(val=temp)
                node = node.next
                if self.l1.next == None and carry:
                    node.next = ListNode(val=carry)
                    break
                self.l1 = self.l1.next

        return result
