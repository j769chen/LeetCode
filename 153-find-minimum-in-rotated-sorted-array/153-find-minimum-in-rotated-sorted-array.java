class Solution {
    public int findMin(int[] nums) {
        int min = 5001;
        
        int left = 0;
        int right = nums.length - 1;
        int mid;
        
        if (nums.length == 1) {
            return nums[0];
        }
        
        while (left <= right) {
            mid = left + (right-left)/2;
            if (nums[mid] < min) {
                min = nums[mid];
            }
            
            
            // we know that the left side is sorted
            if (nums[left] <= nums[mid]) {
                if (nums[left] < min) {
                    min = nums[left];
                }
                
                left = mid + 1;
            }
            else if (nums[right] > nums[mid]) {
                right = mid - 1;
            }
        }
        
        return min;
    }
}