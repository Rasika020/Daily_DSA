class Solution {
    public int[] sortedSquares(int[] nums) {
        for(int i=0;i<nums.length;i++){
            nums[i] = nums[i]*nums[i];
        }
        Arrays.sort(nums);
        return nums;
    }
}
import java.util.Arrays;
public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums = {-4,-1,0,3,10};
        int[] result = solution.sortedSquares(nums);
        System.out.println("Output: " + Arrays.toString(result));
    }
}