/**
 * <p>
 * 34. Find First and Last Position of Element in Sorted Array (Medium)
 * https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/3/24
 */
class SearchRange {
    public int[] searchRange(int[] nums, int target) {

        // Find the location of "target"
        int index = binarySearch(nums, target);

        // If we could not find "target"
        if (index == -1) return new int[]{-1, -1};

        int indexLeft = index;
        int indexRight = index;
        int n = nums.length;
        int[] res = new int[2];

        // Search right
        while (indexRight < n && nums[indexRight] == target) {
            indexRight++;
        }
        res[1] = indexRight - 1;

        // Search left
        while (indexLeft >= 0 && nums[indexLeft] == target) {
            indexLeft--;
        }
        res[0] = indexLeft + 1;

        return res;

    }

    public int binarySearch(int[] nums, int target) {

        int left = 0;
        int right = nums.length - 1;
        int mid;

        while (left <= right) {

            mid = left + (right - left) / 2;
            int cur = nums[mid];

            if (target == cur) return mid;
            if (target < cur) {
                // Search left
                right = mid - 1;
            } else {
                // Search right
                left = mid + 1;
            }

        }

        return -1;

    }
}
