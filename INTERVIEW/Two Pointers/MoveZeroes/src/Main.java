public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 3, 12};
        solution.moveZeroes(nums);
        for (int num : nums) {
            System.out.print(num);
        }
    }
}
