import java.util.*;

class Solution {
    List<Integer> arr;
    public Solution(ListNode head) {
        arr = new ArrayList<>();
        while(head != null){
            arr.add(head.val);
            head = head.next;
        }
    }
    
    public int getRandom() {
        Random rand = new Random();
        int randomIndex = rand.nextInt(arr.size());
        return arr.get(randomIndex);
    }
}