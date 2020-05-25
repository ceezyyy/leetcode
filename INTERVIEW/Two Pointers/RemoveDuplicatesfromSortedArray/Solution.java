/**
 * @Topic 26. Remove Duplicates from Sorted Array
 * @Author Yi Cai
 * @Tag Two Pointers
 * @Date 3/18/2020 9:30 AM
 **/

class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) return 0;
        int i = 0;  // slow pointer
        for (int j = 1; j < nums.length; j++) {  // fast pointer
            if (nums[j] != nums[i]) {  // unique
                nums[++i] = nums[j];
            }
        }
        return i + 1;  // the length
    }
}

/*
Time Complexity: O(n)
Space Complexity: O(1)
*/    
