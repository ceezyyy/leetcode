import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * @Topic 1380. Lucky Numbers in a Matrix
 * @Author Yi Cai
 * @Tag Array
 * @Date 3/20/2020 10:56 AM
 **/

class Solution {
    public List<Integer> luckyNumbers(int[][] A) {
        int m = A.length;
        int n = A[0].length;
        int[] minRow = new int[m];
        int[] maxCol = new int[n];
        Arrays.fill(minRow, Integer.MAX_VALUE);  // initialize the minRow array
        /*
        For loop each element and keep tracking the min of each row
        and the max of each col
        */
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                minRow[i] = Math.min(A[i][j], minRow[i]);
                maxCol[j] = Math.max(A[i][j], maxCol[j]);
            }
        }
        // find the intersection
        List<Integer> result = new ArrayList();
        for (int i = 0; i < minRow.length; i++) {
            for (int j = 0; j < maxCol.length; j++) {
                if (minRow[i] == maxCol[j]) {
                    result.add(minRow[i]);
                }
            }
        }
        return result;
    }
}


// Time Complexity: O(mn)
// Space Complexity: O(1)

