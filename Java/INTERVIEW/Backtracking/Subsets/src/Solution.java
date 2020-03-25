import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * @Topic 78. Subsets
 * @Author Yi Cai
 * @Tag Backtracking
 * @Date 3/25/2020 3:57 PM
 **/


class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);  // avoid duplicate
        dfs(nums, new ArrayList<Integer>(), 0, result);
        return result;
    }


    private void dfs(int[] originArray, List<Integer> runningChoices, int start, List<List<Integer>> result) {
        // 3. Our goal: restore all subsets
        result.add(new ArrayList<Integer>(runningChoices));

        // 2. Our constraints
        if (runningChoices.size() == originArray.length) return;

        // 1. Our choice
        for (int i = start; i < originArray.length; i++) {
            // Pick an element from the origin array
            int choice = originArray[i];

            // Store the current pickup to our 'runningChoices'
            runningChoices.add(choice);

            // Recurse
            dfs(originArray, runningChoices, i + 1, result);

            // Backtracking
            runningChoices.remove(runningChoices.size() - 1);
        }
    }
}


// Time Complexity: O()
// Space Complexity: O(1)

