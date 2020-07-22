package FindAllNumbersDisappearedinanArray;

import java.util.ArrayList;
import java.util.List;

/**
 * 448. Find All Numbers Disappeared in an Array
 * https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
 * Easy
 *
 * @author ceezyyy
 */
class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {

        // the 'right place' of current element
        int rightPlace = 0;

        List<Integer> result = new ArrayList<>();

        // corner case
        if (nums.length == 0 || nums == null) {
            return result;
        }

        // all the elements of [1, n]
        // e.g: 1 -> nums[0], 2 -> nums[1], 3 -> nums[2]
        // each element has its own place
        for (int i = 0; i < nums.length; i++) {

            // find the place of current element
            if (nums[i] < 0) {
                rightPlace = -nums[i];
            } else {
                rightPlace = nums[i];
            }

            rightPlace--;

            if (nums[rightPlace] > 0) {
                // mark this negative
                // which means the corresponding element already exists
                nums[rightPlace] = -nums[rightPlace];
            }
            // else do nothing
        }

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > 0) {
                // the corresponding element does not exist
                result.add(i + 1);
            }
        }

        return result;

    }
}


// Time Complexity: O(n)
// Space Complexity: O(1)
