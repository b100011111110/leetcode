class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int c = 0;
        ListNode temp = new ListNode(0);
        ListNode cur = temp;
        while(l1 != null || l2 != null || c == 1){
            temp.next = new ListNode(0);
            temp = temp.next;
            if(l1!=null){
                temp.val += l1.val;
                l1 = l1.next;
            }
            if(l2!=null){
                temp.val += l2.val;
                l2 = l2.next;
            }
            temp.val += c;
            c = temp.val / 10;
            temp.val %= 10;
        }
        return cur.next;
    }
}