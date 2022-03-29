class Solution {
    public int romanToInt(String s) {
        HashMap<Character, Integer> romanToInt = new HashMap<>(); 
        romanToInt.put('I', 1);
        romanToInt.put('V', 5);
        romanToInt.put('X', 10);
        romanToInt.put('L', 50);
        romanToInt.put('C', 100);
        romanToInt.put('D', 500);
        romanToInt.put('M', 1000);
        
        int num = 0;
        
        for(int i = s.length() - 1; i >= 0; i--) {
            char curr = s.charAt(i);
            int numToAdd = romanToInt.get(curr);
            
            if (i != 0) {
                char next = s.charAt(i-1);
                if ((curr == 'V' || curr == 'X') && next == 'I') {
                    numToAdd--;
                    i--;
                }
                else if ((curr == 'L' || curr == 'C') && next == 'X') {
                    numToAdd -= 10;
                    i--;
                }
                else if ((curr == 'D' || curr == 'M') && next == 'C') {
                    numToAdd -= 100;
                    i--;
                }
            }
            num += numToAdd;
        }
        
        return num;
    }
}