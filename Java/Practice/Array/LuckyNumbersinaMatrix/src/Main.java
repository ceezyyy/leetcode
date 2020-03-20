import java.util.List;

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[][] testCase = {{3, 7, 8}, {9, 11, 13}, {15, 16, 17}};
        List<Integer> result = solution.luckyNumbers(testCase);
        System.out.println(result);
    }
}
