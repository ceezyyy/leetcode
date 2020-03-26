import java.util.ArrayList;
import java.util.List;

/**
 * @Topic 216. Combination Sum III
 * @Author Yi Cai
 * @Tag Backtracking
 * @Date 3/26/2020 8:58 PM
 **/


class Solution {
    public List<List<Integer>> combinationSum3(int k, int n) {
        List<List<Integer>> result = new ArrayList<>();
        dfs(k, n, new ArrayList<Integer>(), 1, result);
        return result;
    }


    private void dfs(int k, int remain, List<Integer> runningChoices, int start, List<List<Integer>> result) {
        // 2. Constraints
        if (remain < 0 || runningChoices.size() > k) return;

        // 3. Goal: K numbers that add up tp n
        if (remain == 0 && runningChoices.size() == k) {
            result.add(new ArrayList<>(runningChoices));
        }

        // 1. Choice
        for (int i = start; i < 10; i++) {  // Pick an element from 1 - 9
            int choice = i;

            // Add the current choice to 'runningChoices'
            runningChoices.add(choice);

            // Recurse
            dfs(k, remain - i, runningChoices, i + 1, result);  // Unique set

            // Backtracking
            runningChoices.remove(runningChoices.size() - 1);
        }
    }
}


// Time Complexity: O(n * (n-1)!)
// Space Complexity: O(k)

