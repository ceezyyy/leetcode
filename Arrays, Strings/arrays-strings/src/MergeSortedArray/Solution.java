package MergeSortedArray;

class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {

        int i = m - 1;
        int j = n - 1;
        int k = m + n - 1;

        // Backwards
        while (i >= 0 && j >= 0) {
            if (nums1[i] >= nums2[j]) {
                nums1[k--] = nums1[i--];
            } else {
                nums1[k--] = nums2[j--];
            }
        }

        // nums2 still has remaining
        // e.g: nums1[8,9,10,0,0,0], nums2[1,2,3]
        while (j >= 0) {
            nums1[k--] = nums2[j--];
        }

    }
}
