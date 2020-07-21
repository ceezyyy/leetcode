package SortArrayByParity;

/**
 * 905. Sort Array By Parity
 * https://leetcode.com/problems/sort-array-by-parity/
 * Easy
 *
 * @author ceezyyy
 */
class Solution {
    public int[] sortArrayByParity(int[] A) {

        int n = A.length;
        int[] arr = new int[n];

        // two pointers
        int left = 0;
        int right = n - 1;

        // [even, odd]
        for (int i = 0; i < n; i++) {
            // even
            if (A[i] % 2 == 0) {
                arr[left] = A[i];
                left++;
            } else {
                // odd
                arr[right] = A[i];
                right--;
            }
        }

        return arr;

    }
}


// Time Complexity: O(n)
// Space Complexity: O(n)
