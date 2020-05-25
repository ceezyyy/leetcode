/**
 * @Topic 242. Valid Anagram
 * @Author Yi Cai
 * @Tag Array / String
 * @Date 3/27/2020 2:53 PM
 **/


class Solution {
    public boolean isAnagram(String s, String t) {
        // Corner case
        if (s.length() != t.length()) return false;

        // The string contains only lowercase alphabets
        int[] map = new int[26];
        for (char ch : s.toCharArray()) {
            map[(int) ch - 97]++;  // 'a' -> 97 (ASCII)
        }
        for (char ch : t.toCharArray()) {
            map[(int) ch - 97]--;
            if (map[(int) ch - 97] < 0) return false;
        }
        return true;
    }
}


// Time Complexity: O(n)
// Space Complexity: O(1)

