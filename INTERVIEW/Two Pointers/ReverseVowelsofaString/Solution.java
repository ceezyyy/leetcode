/**
 * @Topic 345. Reverse Vowels of a String
 * @Author Yi Cai
 * @Tag Two Pointers
 * @Date 3/29/2020 10:09 AM
 **/


class Solution {
    public String reverseVowels(String s) {
        // Two pointers
        int left = 0;
        int right = s.length() - 1;

        // Convert string to char array
        char[] charArray = s.toCharArray();
        String vowels = "aeiouAEIOU";

        while (left < right) {
            if (vowels.indexOf(charArray[left]) != -1 && vowels.indexOf(charArray[right]) != -1) {
                // Swap two vowels
                char temp = charArray[left];
                charArray[left] = charArray[right];
                charArray[right] = temp;
                // Continue our process
                left++;
                right--;
            } else if (vowels.indexOf(charArray[left]) != -1) {
                right--;
            } else {
                left++;
            }
        }
        return new String(charArray);
    }
}


// Time Complexity: O(n)
// Space Complexity: O(n)

