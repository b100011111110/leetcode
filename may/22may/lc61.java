class Solution {
    int getCount(ListNode head){
        int n = 0;
        while(head != null){
            n++;
            head = head.next;
        }
        return n;
    }
    public ListNode rotateRight(ListNode head, int k) {
        int n = getCount(head);
        if(n == 0) return null;
        k %= n;
        if(k == 0) return head;
        k = n-k;
        ListNode temp = head;
        while(k-- > 1){
            head = head.next;
        }
        ListNode first = head.next;
        head.next = null;
        head = first;
        while(head.next != null){
            head = head.next;
        }
        head.next = temp;
        return first;
    }
}