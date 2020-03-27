/**
 * @Topic 27. Remove Element
 * @Author Yi Cai
 * @Tag Two Pointers
 * @Date 3/18/2020 5:51 PM
 **/

class Solution {
    public int removeElement(int[] nums, int val) {
        if (nums.length == 0 || (nums.length == 1 && nums[0] == val)) return 0;
        int i = 0;  // slow pointer
        for (int j = 0; j < nums.length; j++) {  // fast pointer
            if (nums[j] != val) {
                nums[i++] = nums[j];
            }
        }
        return i;
    }
}


// Time Complexity: O(n)
// Space Complexity: O(1)
