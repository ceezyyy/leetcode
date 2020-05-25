import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * @Topic 39. Combination Sum
 * @Author Yi Cai
 * @Tag BackTracking
 * @Date 3/23/2020 10:38 PM
 **/


class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(candidates);  // in case of duplicate
        dfs(candidates, target, new ArrayList<Integer>(), result, 0);
        return result;
    }


    private void dfs(int[] originArray, int remain, List<Integer> runningChoices, List<List<Integer>> result, int start) {
        // Our goal
        if (remain < 0) return;
        if (remain == 0) {
            result.add(new ArrayList<Integer>(runningChoices));
        }

        // Dfs & Backtracking process
        for (int i = start; i < originArray.length; i++) {  // Start from currentIndex in case of duplicate
            // Choose an element from the origin array
            int choice = originArray[i];

            // Store it in the 'runningChoices'
            runningChoices.add(choice);

            // Recurse the process
            // 'i' stands for the current slot, in case of duplicate
            dfs(originArray, remain - choice, runningChoices, result, i);

            // Backtracking
            runningChoices.remove(runningChoices.size() - 1);
        }
    }
}


// Time Complexity: O(n^2)
// Space Complexity: O(n)  return array is not considered as an extra space

