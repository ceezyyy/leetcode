/**
 * <p>
 * 48. Rotate Image (Medium)
 * https://leetcode.com/problems/rotate-image/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/4/19
 */
public class RotateImage {

    private int[][] matrix;
    private int n;

    public void rotate(int[][] matrix) {

        this.matrix = matrix;
        this.n = matrix.length;

        // 1) Reverse
        reverse();

        // 2) Swap
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                swap(i, j);
            }
        }

    }

    public void reverse() {

        int i = 0;
        int j = matrix.length - 1;

        while (i < j) {
            int[] tmp = matrix[i];
            matrix[i] = matrix[j];
            matrix[j] = tmp;
            i++;
            j--;
        }

    }

    public void swap(int i, int j) {
        int tmp = matrix[i][j];
        matrix[i][j] = matrix[j][i];
        matrix[j][i] = tmp;
    }
}
