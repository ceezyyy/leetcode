import java.util.ArrayList;
import java.util.List;

/**
 * Combinations
 */
class Solution {

    private List<List<Integer>> result = new ArrayList<>();

    public List<List<Integer>> combine(int n, int k) {
        // Constraints:
        // 1 <= n <= 20
        // 1 <= k <= n
        backtracking(n, k, new ArrayList<Integer>(), 1);
        return result;
    }

    public void backtracking(int n, int k, List<Integer> runningChoices, int start) {

        // Reach the goal: we have made all decisions
        if (runningChoices.size() == k) {
            result.add(new ArrayList(runningChoices));
            return;
        }

        // Decision tree traversal
        for (int i = start; i <= n; i++) {

            int choice = i;

            if (runningChoices.contains(choice)) continue;

            // 1. Add current choice to our running choice list
            runningChoices.add(choice);
            // 2. Jump into the next level of decision tree
            backtracking(n, k, runningChoices, i + 1);
            // 3. Undo current choice
            runningChoices.remove(runningChoices.size() - 1);

        }
    }
}