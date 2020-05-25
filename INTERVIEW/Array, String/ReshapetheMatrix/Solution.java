/**
 * @Topic 566. Reshape the Matrix
 * @Author Yi Cai
 * @Tag Array
 * @Date 4/7/2020 11:16 AM
 **/


class Solution {
    public int[][] matrixReshape(int[][] nums, int r, int c) {
        /*
         * Corner case
         * If the 'reshape' operation with given parameters is possible and legal
         * output the new reshaped matrix
         * */
        if ((r * c != nums.length * nums[0].length) || (r == nums.length && c == nums[0].length)) {
            return nums;
        }

        /*
         * Initialize the return array
         * */
        int[][] result = new int[r][c];

        /*
         * Mapping (Old array -> New array)
         * */
        int id = 0;
        for (int i = 0; i < nums.length; i++) {
            for (int j = 0; j < nums[0].length; j++) {
                /*
                 * Every item in the array has its own id
                 * */
                id = i * nums[0].length + j;
                /*
                 * Mapping
                 * */
                result[id / c][id % c] = nums[i][j];
            }
        }

        return result;
    }
}


// Time Complexity: O(m*n)
// Space Complexity: O(m*n) no extra space

