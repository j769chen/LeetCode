class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        HashSet<Integer> numberSet = new HashSet<>();
        HashSet<String> tripletSet = new HashSet<>();
        List<List<Integer>> sol = new ArrayList<>();
        
        if (nums.length < 3) {
            return sol;
        }
        if (nums.length == 3) {
            if ((nums[0] + nums[1] + nums[2]) == 0) {
                 List triplet = new ArrayList<>();
                triplet.add(nums[0]);
                triplet.add(nums[1]);
                triplet.add(nums[2]);
                sol.add(triplet);
                return sol;
            }
        }
        // System.out.println(nums.length);
        for (int i = 0; i < nums.length - 1; i++) {
            for (int j = i+1; j < nums.length; j++) {
                // System.out.println("curr index: " + i + "," + j + " " + nums[i] + " " + nums[j]);
                // System.out.println(-(nums[i] + nums[j]));
                if (numberSet.contains(-(nums[i] + nums[j]))) {   
                    List triplet = new ArrayList<>();
                    triplet.add(-(nums[i] + nums[j]));
                    triplet.add(nums[i]);
                    triplet.add(nums[j]);
                    Collections.sort(triplet);
                    if (tripletSet.add(" " + triplet.get(0) + triplet.get(1) + triplet.get(2))) {
                        sol.add(triplet);
                    }
                }   
            }
            numberSet.add(nums[i]);
        }
        return sol;
    }
}