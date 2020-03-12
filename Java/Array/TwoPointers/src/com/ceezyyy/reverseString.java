package com.ceezyyy;


/*
 * Topic: 344. Reverse String
 * Tag: Two Pointers / String
 * Updated date: 03/12/2020
 */


class Solution {
    public void reverseString(char[] s) {
        int left = 0;
        int right = s.length - 1;
        while (left <= right) {
            char temp = s[left];
            s[left++] = s[right];
            s[right--] = temp;
        }
    }
}


/*
Runtime: 1 ms, faster than 97.25% of Java online submissions for Reverse String.
Memory Usage: 43.9 MB, less than 98.82% of Java online submissions for Reverse String.
*/


/*
Time Complexity: O(n)
Space Complexity: O(1)
*/
