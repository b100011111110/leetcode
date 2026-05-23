class Solution {
    public ListNode oddEvenList(ListNode head) {
        if(head == null || head.next == null) return head;
        ListNode odd = new ListNode(0),even = new ListNode(0);
        ListNode ot = odd,et = even;
        while(head != null && head.next != null){
            odd.next = head;
            even.next = head.next;
            odd = odd.next;
            even = even.next;
            head = head.next.next;
        }
        even.next = null;
        if(head != null){
            odd.next = head;
            odd = odd.next;
        }
        odd.next = et.next;
        return ot.next;
    }
}