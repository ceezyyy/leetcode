import java.util.ArrayList;
import java.util.List;

/**
 * @Topic 46. Permutations
 * @Author Yi Cai
 * @Tag BackTracking
 * @Date 3/23/2020 2:43 PM
 **/


class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> runningChoices = new ArrayList<>();
        dfs(nums, runningChoices, result);  // dfs & backtracking
        return result;
    }


    private void dfs(int[] originArray, List<Integer> runningChoices, List<List<Integer>> result) {
        // Reach our goal
        if (runningChoices.size() == originArray.length) {
            result.add(new ArrayList<>(runningChoices)); // add it to our result
            return;  // do not forget to return
        }

        // Our choice
        for (int i = 0; i < originArray.length; i++) {
            int choice = originArray[i];

            // if current element already in our choices, enter the next loop immediately
            if (runningChoices.contains(choice)) continue;

            // choice the element and add it to the 'runningChoices'
            runningChoices.add(choice);

            // recurse on the current choice
            dfs(originArray, runningChoices, result);

            // remove the choice we picked, back to the upper level
            runningChoices.remove(runningChoices.size() - 1);  // backtracking
        }
    }
}


// Time Complexity: O(n * n!)
// Space Complexity: O(n)  result is not considered as the extra space

