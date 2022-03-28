class Solution {
    public int lengthOfLongestSubstring(String s) {
        
        if (s.length() == 1) {
            return 1;
        }
        
        int longest = 0;
        
        char[] arr = s.toCharArray();
        LinkedHashSet<Character> currSet = new LinkedHashSet<>();
        
        for (int i = 0; i < arr.length; i++) {
            if (!currSet.add(arr[i])) {
                Iterator<Character> iter = currSet.iterator();
                while(iter.next() != arr[i]) {
                    iter.remove();  
                    
                }
                currSet.remove(arr[i]);
                currSet.add(arr[i]);
            }
            
            if (currSet.size() > longest) {
                longest = currSet.size();
            }
        }
        
        return longest;
    }
}