# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (l1.next == None) & (l2.next == None):
            summed = l1.val + l2.val
            if summed >=10:
                node = ListNode(val = summed-10,next=ListNode(val=1,next=None))
            else:
                node = ListNode(val=summed,next=None)
        elif (l1.next != None) & (l2.next == None):
            summed = l1.val + l2.val
            if summed <10:
                
                node = ListNode(summed,l1.next)

            else:
                node = ListNode(summed-10,None)
                node.next = self.addTwoNumbers(l1.next,ListNode(1,None))
        elif (l1.next == None) & (l2.next != None):
            summed = l1.val + l2.val
            if summed <10:
                node = ListNode(summed,l2.next)
            else:
                node = ListNode(summed-10,None)
                node.next = self.addTwoNumbers(l2.next,ListNode(1,None))
        else:
            summed = l1.val + l2.val
            if summed <10:
                node = ListNode(summed,None)
                node.next = self.addTwoNumbers(l1.next,l2.next)
            else:
                node = ListNode(summed-10,None)
                l2.next.val+=1
                node.next = self.addTwoNumbers(l1.next,l2.next)
        return node
        