import java.util.Arrays;

/**
 * @Topic 945. Minimum Increment to Make Array Unique
 * @Author Yi Cai
 * @Tag Array
 * @Date 3/26/2020 10:38 PM
 **/


class Solution {
    public int minIncrementForUnique(int[] A) {
        // Corner case
        if (A == null) return 0;
        int result = 0;
        Arrays.sort(A);  // Sort the array
        for (int i = 1; i < A.length; i++) {
            // Three cases '<'  '='  '>'
            if (A[i] == A[i - 1]) {
                A[i]++;
                result++;
            } else if (A[i] < A[i - 1]) {
                result += A[i - 1] - A[i] + 1;
                A[i] = A[i - 1] + 1;
            } else {
                continue;
            }
        }
        return result;
    }
}


// Time Complexity: O(nlogn)
// Space Complexity: O(1)

