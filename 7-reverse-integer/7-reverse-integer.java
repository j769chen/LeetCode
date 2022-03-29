class Solution {
    public int reverse(int x) {
        boolean isNegative = false;
        int newVal;
        
        if (x < 0) {
            x *= -1;
            isNegative = true;
        }
        
        ArrayList<Character> digits = new ArrayList<>();
        
        char[] oldValArr = String.valueOf(x).toCharArray();
        
        char[] newValArr = new char[oldValArr.length];
        
        for (int i = oldValArr.length - 1; i >= 0; i--) {
            newValArr[oldValArr.length - 1 - i] = oldValArr[i];
        }
        
        try {
            newVal = Integer.parseInt(String.valueOf(newValArr));
        }
        catch (NumberFormatException e) {
            return 0;
        }
        
            
        if(isNegative) {
            newVal *= -1;
        }
        
        return newVal;
    }
}