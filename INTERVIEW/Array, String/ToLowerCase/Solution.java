/**
 * @Topic 709. To Lower Case
 * @Author Yi Cai
 * @Tag Array / String
 * @Date 3/27/2020 3:14 PM
 **/


class Solution {
    public String toLowerCase(String str) {
        StringBuilder result = new StringBuilder();
        for (char ch : str.toCharArray()) {
            // If we meet upper case
            if (ch - 'a' < 0 && ch - 'A' >= 0) {
                result.append((char) (ch + 32));  // upper -> lower
            } else {
                result.append(ch);
            }
        }
        return result.toString();  // StringBuilder -> String
    }
}


// Time Complexity: O(n)
// Space Complexity: O(n)

