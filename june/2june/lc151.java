class Solution {
    public String reverseWords(String s) {
        String[] arr = s.split(" ");
        StringBuilder b = new StringBuilder("");
        for(int i=arr.length-1;0<=i;i--){
            if(arr[i].equals("")) continue;
            b.append(arr[i]);
            b.append(" ");
        }
        b.deleteCharAt(b.length()-1);
        return b.toString();
    }
}