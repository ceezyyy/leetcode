package ReplaceElementswithGreatestElementonRightSide;

/**
 * 1299. Replace Elements with Greatest Element on Right Side
 * https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
 * Easy
 *
 * @author ceezyyy
 */
class Solution {
    public int[] replaceElements(int[] arr) {

        // the greatest element on right side
        int maxOfRight = -1;
        int temp = -1;

        // walk through from right to left
        for (int i = arr.length - 1; i >= 0; i--) {

            // store the value of arr[i]
            temp = arr[i];

            // replace
            arr[i] = maxOfRight;

            if (temp > maxOfRight) {
                maxOfRight = temp;
            }
        }

        return arr;

    }
}


// Time Complexity: O(n)
// Space Complexity: O(1)