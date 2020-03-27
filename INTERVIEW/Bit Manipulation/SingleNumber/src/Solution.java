/**
 * @Topic 136. Single Number
 * @Author Yi Cai
 * @Tag Bit Manipulation
 * @Date 3/20/2020 12:16 PM
 **/


/*
 * Input: [4,1,2,1,2]
 * Explanation: (1 ^ 1) ^ (2 ^ 2) ^ 4 = 0 ^ 0 ^ 4 = 0 ^ 4 = 4
 * Output: 4
 * */


class Solution {
    public int singleNumber(int[] nums) {
        int a = 0;
        for (int num : nums) {
            a ^= num;
        }
        return a;
    }
}


// Time Complexity: O(n)
// Space Complexity: O(1)

