class Solution {
    public ListNode swapPairs(ListNode head) {
        ListNode temp = new ListNode(0,head);
        ListNode cur = temp;
        while(cur != null && cur.next != null && cur.next.next != null){
            ListNode a = cur.next;
            ListNode b = cur.next.next;
            ListNode c = cur.next.next.next;
            cur.next = b;
            b.next = a;
            a.next = c;
            cur = a;
        }
        return temp.next;
    }
}