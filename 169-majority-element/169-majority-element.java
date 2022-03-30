class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer, Integer> numCounts = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            if (numCounts.containsKey(nums[i])) {
                numCounts.put(nums[i], numCounts.get(nums[i]) + 1);
            }
            else {
                numCounts.put(nums[i], 1);
            }
        }
        
        for (Integer i: numCounts.keySet()) {
            if (numCounts.get(i) > nums.length/2) {
                return i;
            }
        }
        
        return 0;
    }
}