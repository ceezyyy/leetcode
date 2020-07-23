package ValidMountainArray;

class Solution {
    public boolean validMountainArray(int[] A) {

        // index of peak element
        int peak = -1;

        // corner case
        if (A.length < 3) {
            return false;
        }

        for (int i = 1; i < A.length - 1; i++) {
            // increasing
            if (A[i - 1] >= A[i]) {
                return false;
            }
            // find the index of peak element
            if ((A[i - 1] < A[i]) && (A[i] > A[i + 1])) {
                peak = i;
                break;
            }
        }

        // peak does not exist
        if (peak == -1) {
            return false;
        }

        // decreasing
        for (int j = peak; j < A.length - 1; j++) {
            if (A[j] <= A[j + 1]) {
                return false;
            }
        }

        return true;

    }
}


// Time Complexity: O(n)
// Space Complexity: O(1)