package SquaresofaSortedArray;

/**
 * 977. Squares of a Sorted Array
 * https://leetcode.com/problems/squares-of-a-sorted-array/
 * Easy
 *
 * @author ceezyyy
 */
class Solution {
    public int[] sortedSquares(int[] A) {

        int n = A.length;

        // left pointer
        int left = 0;

        // right pointer
        int right = n - 1;

        // result array
        int[] result = new int[n];

        // the place of current element
        int index = n - 1;

        while (left <= right) {
            if (A[left] * A[left] >= A[right] * A[right]) {
                // choose left
                result[index] = A[left] * A[left];
                index--;
                left++;
            } else {
                // choose right
                result[index] = A[right] * A[right];
                index--;
                right--;
            }
        }

        return result;

    }
}


// Time Complexity: O(n)
// Space Complexity: O(1)

