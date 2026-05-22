class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        ListNode temp = new ListNode(0,head);
        ListNode prev = temp;
        while(head != null){
            boolean flag = false;
            while(head.next != null && head.val == head.next.val){
                flag = true;
                head.next = head.next.next;
            }
            if(flag){
                prev.next = head.next;
            }
            else{
                prev = head;
            }
            head = head.next;
        }
        return temp.next;
    }
}