package Searcha2DMatrixII;

class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {

        /**
         * Corner case for 2d array
         */
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return false;
        }

        int rows = matrix.length;
        int cols = matrix[0].length;
        int i = 0;
        int j = cols - 1;

        /**
         * From top-right to bottom-left
         * to some extent, like BST
         */
        while (i < rows && j >= 0) {
            if (target == matrix[i][j]) return true;
            if (target > matrix[i][j]) {
                i++;
            } else {
                j--;
            }
        }

        return false;

    }
}
