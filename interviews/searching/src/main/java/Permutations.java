import java.util.ArrayList;
import java.util.List;

/**
 * <p>
 * 46. Permutations
 * https://leetcode.com/problems/permutations/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/4/5
 */
public class Permutations {

    private List<List<Integer>> res = new ArrayList<>();
    private int[] choices;
    private int n;

    public List<List<Integer>> permute(int[] nums) {

        this.choices = nums;
        this.n = nums.length;

        backtracking(0, new ArrayList<Integer>());

        return res;

    }

    public void backtracking(int current, List<Integer> path) {

        /*
          When we reach the goal
         */
        if (path.size() == n) {
            // Add "snapshot"
            res.add(new ArrayList<>(path));
            // Stop searching
            return;
        }

        /*
          Making choices w/ constraints
         */
        for (int i = 0; i < n; i++) {

            int choice = choices[i];

            /*
              Constraints:
              1. Permutations (all the integers of nums are unique)
             */
            if (path.contains(choice)) continue;

            path.add(choice);
            backtracking(i + 1, path);
            path.remove(path.size() - 1);

        }

    }
}
