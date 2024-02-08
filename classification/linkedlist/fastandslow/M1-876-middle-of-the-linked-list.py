class Solution:
     # lct:linkedlist,fastandslow;
     # lcd:M1;
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head , head
        while fast and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow 
        