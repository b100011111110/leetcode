import java.util.*;

class lc75 {
    public void sortColors(int[] nums) {
        int i=0,j=0,k=nums.length-1;
        for(j=0;nums.length>j;j++){
            if(nums[j] == 0){
                int temp = nums[i];
                nums[i++] = nums[j];
                nums[j] = temp;
            }
            else if(nums[j] == 2){
                int temp = nums[k];
                nums[k--] = nums[j];
                nums[j] = temp;
            }
            System.out.println(Arrays.toString(nums));
        }
    }
    public static void main(String[] args) {
        lc75 s = new lc75();
        s.sortColors(new int[]{2, 0, 2, 1, 1, 0});
    }
}