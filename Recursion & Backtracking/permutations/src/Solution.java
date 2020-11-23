import java.util.ArrayList;
import java.util.List;

/**
 * Permutations
 */
class Solution {

    private List<List<Integer>> result = new ArrayList<>();

    public List<List<Integer>> permute(int[] nums) {
        // 1 <= nums.length <= 6
        backtracking(nums, new ArrayList<Integer>());
        return result;
    }

    public void backtracking(int[] nums, List<Integer> runningChoices) {

        // Reach the goal: we have made all the decisions
        if (runningChoices.size() == nums.length) {
            result.add(new ArrayList(runningChoices));
            // Do not forget to return
            return;
        }

        // Decision tree traversal
        for (int i = 0; i < nums.length; i++) {

            int choice = nums[i];

            // All the integers of nums are unique
            // Skip if current choice is in our choice list
            if (runningChoices.contains(choice)) continue;

            runningChoices.add(choice);
            // Jump into the next level of decision tree
            backtracking(nums, runningChoices);
            // Undo current choice
            runningChoices.remove(runningChoices.size() - 1);

        }
    }
}