public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[][] nums = new int[][]{{1, 2}, {3, 4}};
        int[][] result = solution.matrixReshape(nums, 1, 4);

        for (int[] row : result) {
            for (int item : row) {
                System.out.println(item);
            }
        }
    }
}
