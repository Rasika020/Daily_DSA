class Solution {
    //first approach nlogn
    public boolean numHasEvenDigit(int num){
        int digitCount = 0;
        while(num!=0){
            num = num/10;
            digitCount++;
        }
        return digitCount%2 ==0;
    }
    public int findNumbers(int[] nums) {
        int even_count = 0;
        for(int i=0;i<nums.length;i++){
            if(numHasEvenDigit(nums[i])){
                even_count++;
            }

        } 
        return even_count;
    }
}
public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
    
    int[][] testCases = {
        {12,345,2,6,7896},
        {555,901,482,1771},
        {1,22,333,4444,55555}
    };
    
    for (int i = 0; i < testCases.length; i++) {
        int result = solution.findNumbers(testCases[i]);
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