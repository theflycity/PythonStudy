from ListNode import ListNode
class Solution(object):
   def addTwoNumbers(self, l1, l2):
       """
       :type l1: Optional[ListNode]
       :type l2: Optional[ListNode]
       :rtype: Optional[ListNode]
       """
       head = ListNode()
       tail = head
       arr = 0 #进位
       while l1 or l2 or arr:
           if l1:
               arr += l1.val
               l1 = l1.next
           if l2:
               arr +=l2.val
               l2 = l2.next
           sub_node = ListNode(arr%10)
           arr //=10
           tail.next = sub_node
           tail = sub_node
       return head.next