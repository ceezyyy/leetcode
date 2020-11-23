import java.util.ArrayList;
import java.util.List;

/**
 * Subsets
 */
class Solution {

    private List<List<Integer>> result = new ArrayList<>();

    public List<List<Integer>> subsets(int[] nums) {
        // 1 <= nums.length <= 10
        backtracking(nums, new ArrayList<Integer>(), 0);
        return result;
    }

    public void backtracking(int[] nums, List<Integer> runningChoices, int start) {

        result.add(new ArrayList<>(runningChoices));

        for (int i = start; i < nums.length; i++) {

            int choice = nums[i];

            // 1. Add current choice to our running choice list
            runningChoices.add(choice);
            // 2. Jump into the next level of decision tree
            // The solution set must not contain duplicate subsets
            // So here is "i+1", which means the element behind our current choice
            backtracking(nums, runningChoices, i + 1);
            // 3. Undo current choice
            runningChoices.remove(runningChoices.size() - 1);

        }
    }
}