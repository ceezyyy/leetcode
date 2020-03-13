import java.util.HashSet;

/**
 * @Topic 3. Longest Substring Without Repeating Characters
 * @Author Yi Cai
 * @Tag Two Pointers / Sliding Window /  HashSet
 * @Date 3/13/2020 9:00 PM
 **/

class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.length() == 1) {  // corner case
            return 1;
        }
        int left = 0;  // left pointer
        int right = 0;  // right pointer
        int res = 0;
        HashSet<Character> set = new HashSet<Character>();
        while (left <= right && right < s.length()) {
            if (!set.contains(s.charAt(right))) {
                set.add(s.charAt(right++));  // move forward the right pointer
                // keep tracking the max length
                // because each character of the string may be unique
                res = Math.max(right - left, res);
            } else {  // we meet repeating character
                set.remove(s.charAt(left++));  // move forward the left pointer
            }
        }
        return res;
    }
}

/*
Time Complexity: O(n)
Space Complexity: O(n)
*/    
