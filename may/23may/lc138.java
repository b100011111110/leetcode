class Solution {
    public Node copyRandomList(Node head) {
        Map<Node,Node> map = new HashMap<>();
        Node temp = head;
        while(temp != null){
            map.put(temp,new Node(temp.val));
            temp = temp.next;
        }  
        map.put(null,null);     
        temp = head;
        Node t1 = new Node(0);
        Node t2 = t1;
        while(temp != null){
            Node node = map.get(temp);
            Node rand = map.get(temp.random);
            node.random = rand;
            t1.next = node;
            t1 = node;
            temp = temp.next;
        }
        return t2.next;
    }
}