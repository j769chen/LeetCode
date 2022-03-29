class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> numsMap = new HashMap<>();
        
        int[] ans = new int[2];
        
        for (int i = 0; i < nums.length; i++) {
            if(numsMap.containsKey(target-nums[i])) {
                ans[0] = numsMap.get(target-nums[i]);
                ans[1] = i;
                return ans;
            }
            numsMap.put(nums[i], i);
        }
        
        return ans;
    }
}