public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums = {1, 1, 1, 3, 3, 4, 3, 2, 4, 2};
        boolean result = solution.containsDuplicate(nums);
        System.out.println(result);
    }
}
