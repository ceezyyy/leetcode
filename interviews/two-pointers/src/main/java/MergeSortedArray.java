/**
 * <p>
 * 88. Merge Sorted Array (Easy)
 * https://leetcode.com/problems/merge-sorted-array/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/3/24
 */
class MergeSortedArray {
    public void merge(int[] nums1, int m, int[] nums2, int n) {

        // Corner case
        if (n == 0) return;

        // tails
        int i = m - 1;
        int j = n - 1;
        int a, b = 0;
        int cur = 0;

        // Backwards
        for (cur = m + n - 1; i != -1 && j != -1; cur--) {

            a = nums1[i];
            b = nums2[j];

            // Choose a
            if (a > b) {
                nums1[cur] = a;
                i--;
            } else {
                // Choose b
                nums1[cur] = b;
                j--;
            }

        }

        /*
          Two cases:
          1) nums1 is done:
          Merge nums2 -> nums1

          2) nums2 is done:
          return nums1
         */
        if (i == -1) {
            while (cur >= 0) {
                nums1[cur] = nums2[j--];
                cur--;
            }
        }

    }
}
