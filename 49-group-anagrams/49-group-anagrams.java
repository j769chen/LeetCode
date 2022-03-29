class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> anagrams = new HashMap<>();
        
        for(String s: strs) {
            
            char[] charArray = s.toCharArray();
            Arrays.sort(charArray);
            String sorted = String.valueOf(charArray);
            
            if (anagrams.containsKey(sorted)) {
                anagrams.get(sorted).add(s);
            }
            else {
                ArrayList<String> putVal = new ArrayList<>();
                putVal.add(s);
                anagrams.put(sorted, putVal);
            }
        }
        
        List<List<String>> returnVal = new ArrayList<>();
        
        for (List<String> l: anagrams.values()) {
            returnVal.add(l);
        }
        
        return returnVal;
    }
}