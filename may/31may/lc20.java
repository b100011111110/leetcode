import java.util.Stack;

class Solution {
    public boolean isValid(String s) {
        Stack<Character> st = new Stack<>();
        for(char i:s.toCharArray()){
            try{
                if(i == '(' || i == '[' || i == '{') st.push(i);
                else if(i == ')' && st.pop() != '(') return false;
                else if(i == ']' && st.pop() != '[') return false;
                else if(i == '}' && st.pop() != '{') return false;
            }catch(Exception e){
                return false;
            }
        }
        return st.isEmpty();
    }
}