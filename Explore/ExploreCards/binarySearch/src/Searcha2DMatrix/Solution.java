package Searcha2DMatrix;

class Solution {
    /**
     * 74. Search a 2D Matrix
     * https://leetcode.com/problems/search-a-2d-matrix/
     * Medium
     *
     * @param M
     * @param target
     * @return
     */
    public boolean searchMatrix(int[][] M, int target) {

        // corner case
        if (M == null || M.length == 0) {
            return false;
        }

        int rows = M.length;
        int cols = M[0].length;
        int total = rows * cols;

        // left pointer
        int left = 0;

        // right pointer
        int right = total - 1;

        // binary search
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (target == M[mid / cols][mid % cols]) {
                // bingo
                return true;
            } else if (target > M[mid / cols][mid % cols]) {
                // choose right
                left = mid + 1;
            } else {
                // choose left
                right = mid - 1;
            }
        }

        // could not find
        return false;

    }
}


// Time Complexity: O(logn)
// Space Complexity: O(1)