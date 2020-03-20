public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums1 = {1, 1, 2};
        int[] nums2 = {0, 0, 1, 1, 1, 2, 2, 3, 3, 4};
        int result = solution.removeDuplicates(nums1);
        System.out.println(result);
        result = solution.removeDuplicates(nums2);
        System.out.println(result);
    }
}
