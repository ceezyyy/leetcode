package RemoveDuplicatesfromSortedArray;

class Solution {
    /**
     * 26. Remove Duplicates from Sorted Array
     * https://leetcode.com/problems/remove-duplicates-from-sorted-array/
     * Easy
     *
     * @param nums
     * @return
     */
    public int removeDuplicates(int[] nums) {

        // slow pointer
        // keep tracking the unique element
        int i = 0;

        // fast pointer
        // keep scanning each element
        int j = 1;

        for (j = 0; j < nums.length; j++) {

            // if meet duplicate
            if (nums[i] != nums[j]) {
                i++;
                nums[i] = nums[j];
            }
            // else do nothing

        }

        return i + 1;

    }
}


// Time Complexity: O(n)
// Space Complexity: O(1)
