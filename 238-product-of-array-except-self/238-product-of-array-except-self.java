class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] forwards = new int[nums.length-1];
        int[] backwards = new int[nums.length-1];
        
        int[] solution = new int[nums.length];
        
        int temp = 1;
        
        //find all products up to ith element forward
        for (int i = 0; i < nums.length - 1; i++) {
            temp *= nums[i];
            forwards[i] = temp;
        }
        
        temp = 1;
        
        //do the same reverse
        for (int i = nums.length-1; i > 0; i--) {
            temp *= nums[i];
            backwards[i-1] = temp;
        }
        
//         for (int i = 0; i < forwards.length; i++) {
//             System.out.println(forwards[i]);
//         }
        
//         for (int i = backwards.length-1; i >= 0; i--) {
//            System.out.println(backwards[i]);
//         }
        solution[0] = backwards[0];
        solution[nums.length-1] = forwards[forwards.length-1];
        for (int i = 1; i < nums.length-1; i++) {
            solution[i] = forwards[i-1] * backwards[i];
        }
        
        return solution;
    }
}