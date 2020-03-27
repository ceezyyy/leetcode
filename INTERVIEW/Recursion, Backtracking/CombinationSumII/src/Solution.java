import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * @Topic 40. Combination Sum II
 * @Author Yi Cai
 * @Tag Backtracking
 * @Date 3/24/2020 11:54 AM
 **/


class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(candidates);  // avoid duplicate
        dfs(candidates, target, new ArrayList<Integer>(), result, 0);
        return result;
    }


    private void dfs(int[] originArray, int remain, List<Integer> runningChoices, List<List<Integer>> result, int start) {
        // 3. Our goal
        if (remain == 0 && !result.contains(runningChoices)) {
            // 2. Our constraint two -> avoid duplicate
            result.add(new ArrayList<Integer>(runningChoices));
        }
        if (remain < 0) return;

        // 1. Our choice
        for (int i = start; i < originArray.length; i++) {
            // Pick an element from the origin array as our current choice
            int choice = originArray[i];
            runningChoices.add(choice);

            // Recurse
            // 2. Our constraint one -> each choice only be used once
            dfs(originArray, remain - choice, runningChoices, result, i + 1);

            // Backtracking, enter the next for loop
            runningChoices.remove(runningChoices.size() - 1);
        }
    }
}


// Time Complexity: O(n * n!)
// Space Complexity: O(n)  return array is not considered as extra space

