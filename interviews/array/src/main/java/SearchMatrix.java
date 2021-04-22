/**
 * <p>
 * 240. Search a 2D Matrix II (Medium)
 * https://leetcode.com/problems/search-a-2d-matrix-ii/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/4/22
 */
public class SearchMatrix {
    public boolean searchMatrix(int[][] matrix, int target) {

        // 1 <= n, m <= 300
        int rows = matrix.length;
        int cols = matrix[0].length;
        // Upper-right
        int i = 0;
        int j = cols - 1;

        while (i < rows && j >= 0) {
            int cur = matrix[i][j];
            if (target == cur) return true;
            if (target < cur) j--;
            if (target > cur) i++;
        }

        return false;

    }
}
