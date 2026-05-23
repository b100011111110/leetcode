class Solution {
    public ListNode reverseLL(ListNode head){
        ListNode temp = null;
        while(head != null){
            ListNode x = head;
            head = head.next;
            x.next = temp;
            temp = x;
        }
        return temp;
    }
    public ListNode removeNodes(ListNode head) {
        head = reverseLL(head);
        ListNode temp = head;
        while(head != null){
            int max = head.val;
            while(head.next != null && head.next.val < max){
                head.next = head.next.next;
            }
            head = head.next;
        }
        return reverseLL(temp);
    }
}