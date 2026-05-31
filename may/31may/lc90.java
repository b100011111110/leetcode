import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;

class Solution {
    List<List<Integer>> ans = new ArrayList<>();    
    void traverse(List<Integer> uniqueNums, Map<Integer, Integer> counts, int i, List<Integer> arr) {
        if (i == uniqueNums.size()) {
            ans.add(new ArrayList<>(arr));
            return;
        }
        int currentNum = uniqueNums.get(i);
        int maxCount = counts.get(currentNum);
        for (int k = 0; k <= maxCount; k++) {
            for (int count = 0; count < k; count++) {
                arr.add(currentNum);
            }
            traverse(uniqueNums, counts, i + 1, arr);
            for (int count = 0; count < k; count++) {
                arr.remove(arr.size() - 1);
            }
        }
    }
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Map<Integer, Integer> counts = new HashMap<>();
        for (int num : nums) {
            counts.put(num, counts.getOrDefault(num, 0) + 1);
        }   
        List<Integer> uniqueNums = new ArrayList<>(counts.keySet());
        List<Integer> arr = new ArrayList<>();
        traverse(uniqueNums, counts, 0, arr);
        return ans;
    }
}