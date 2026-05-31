class ListNode{
    int val;
    ListNode next;
    public ListNode(){}
    public ListNode(int val){}
    public ListNode(int val,ListNode node){}
}

class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode cur = new ListNode();
        ListNode temp = cur;
        while(list1 != null && list2 != null){
            if(list1.val < list2.val){
                cur.next = list1;
                list1 = list1.next;
            }
            else{
                cur.next = list2;
                list2 = list2.next;
            }
            cur = cur.next;
        }
        if(list1 == null) 
            cur.next = list2;
        else
            cur.next = list1;
        return temp.next;
    }
}