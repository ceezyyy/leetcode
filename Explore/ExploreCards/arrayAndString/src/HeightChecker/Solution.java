package HeightChecker;

import java.util.Arrays;

/**
 * 1051. Height Checker
 * https://leetcode.com/problems/height-checker
 * Easy
 *
 * @author ceezyyy
 */
class Solution {
    public int heightChecker(int[] heights) {

        // make a copy of origin array
        int[] originArray = Arrays.copyOf(heights, heights.length);

        int result = 0;

        Arrays.sort(heights);

        for (int i = 0; i < heights.length; i++) {
            if (heights[i] != originArray[i]) {
                result++;
            }
        }

        return result;

    }
}


// Time Complexity: O(nlogn)
// Space Complexity: O(n)
