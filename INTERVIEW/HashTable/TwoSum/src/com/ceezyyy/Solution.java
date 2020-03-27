package com.ceezyyy;

/*
 * Topic: 1. Two Sum
 * Tag: HashMap
 * Updated time: 3/13/2020
 */

import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[2];
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(target - nums[i])) {
                result[0] = i;
                result[1] = map.get(target - nums[i]);
                return result;
            }
            map.put(nums[i], i);
        }
        return result;
    }
}


/*
Time Complexity: O(n)
Space Complexity: O(n)
*/
