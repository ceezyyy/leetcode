class Solution {
    public void rotate(int[] nums, int k) {
        // make a copy of array
        int n = nums.length;
        int[] arrayCopy = nums.clone();
        // assignment
        for (int i = 0; i < n; i++) {
            nums[(i + k) % n] = arrayCopy[i];
        }
    }
}


// Time complexity: O(n)
// Space complexity: O(n)