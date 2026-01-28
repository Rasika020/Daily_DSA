class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int max=0;
        int count = 0;
        for(int i=0;i<nums.length;i++){
            if (nums[i]==1){
                count+=1;
            }
            else{
                max = Math.max(max, count);
                count = 0;
            }
        }
        return Math.max(max, count);
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
    
    int[][] testCases = {
        {1, 1, 0, 1, 1, 1},
        {1, 0, 1, 1, 0, 1},
        {0, 0, 0},
        {1, 1, 1, 1}
    };
    
    for (int i = 0; i < testCases.length; i++) {
        int result = solution.findMaxConsecutiveOnes(testCases[i]);
        System.out.print("Test case " + (i + 1) + ": [");
        for (int j = 0; j < testCases[i].length; j++) {
            System.out.print(testCases[i][j]);
            if (j < testCases[i].length - 1) System.out.print(", ");
        }
        System.out.println("]");
        System.out.println("Output: " + result);
        System.out.println();
    }
}