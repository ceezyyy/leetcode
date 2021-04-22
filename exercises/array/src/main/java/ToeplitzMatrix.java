/**
 * <p>
 * 766. Toeplitz Matrix (Easy)
 * https://leetcode.com/problems/toeplitz-matrix/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/4/22
 */
public class ToeplitzMatrix {
    public boolean isToeplitzMatrix(int[][] matrix) {

        // 1 <= m, n <= 20
        int rows = matrix.length;
        int cols = matrix[0].length;

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (i == 0 || j == 0) continue;
                if (matrix[i - 1][j - 1] != matrix[i][j]) return false;
            }
        }

        return true;

    }
}
