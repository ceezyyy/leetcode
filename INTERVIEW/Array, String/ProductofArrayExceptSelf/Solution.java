package com.company;

class Solution {
    public int[] productExceptSelf(int[] nums) {
        // Initialization
        int n = nums.length;
        int[] left = new int[n];
        int[] right = new int[n];
        int[] res = new int[n];

        left[0] = 1;
        right[n - 1] = 1;

        // Left -> Right
        for (int i = 1; i < n; i++) {
            left[i] = nums[i - 1] * left[i - 1];
        }

        // Right -> Left
        for (int i = n - 2; i > -1; i--) {
            right[i] = nums[i + 1] * right[i + 1];
        }

        for (int i = 0; i < n; i++) {
            res[i] = left[i] * right[i];
        }
        return res;
    }
}
