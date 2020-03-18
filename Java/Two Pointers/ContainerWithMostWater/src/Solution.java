/**
 * @Topic 11. Container With Most Water
 * @Author Yi Cai
 * @Tag Two Pointers
 * @Date 3/18/2020 8:47 PM
 **/


class Solution {
    public int maxArea(int[] height) {
        int i = 0;
        int j = height.length - 1;
        int result = 0;
        int currentArea = 0;
        while (i < j) {
            currentArea = Math.min(height[i], height[j]) * (j - i);
            result = result < currentArea ? currentArea : result;  // keep tracking the max area
            if (height[i] < height[j]) {  // depends on the shorter line
                i++;  // forwards
            } else {
                j--;  // backwards
            }
        }
        return result;
    }
}


// Time Complexity: O(n)
// Space Complexity: O(1)

