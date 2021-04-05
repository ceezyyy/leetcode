import java.util.ArrayList;
import java.util.List;

/**
 * <p>
 * 216. Combination Sum III (Medium)
 * https://leetcode.com/problems/combination-sum-iii/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/4/5
 */
public class CombinationSum3 {

    private List<List<Integer>> res = new ArrayList<>();
    private int n;
    private int target;

    public List<List<Integer>> combinationSum3(int k, int n) {

        this.n = k;
        this.target = n;

        backtracking(1, new ArrayList<Integer>());

        return res;

    }

    public void backtracking(int currentChoice, List<Integer> path) {

        /*
          When we reach the goal
         */
        if (path.size() == n) {
            if (getSum(path) == target) {
                res.add(new ArrayList<>(path));
            }
            return;
        }

        /*
          Making choices
          Choices: numbers 1 through 9
         */
        for (int i = currentChoice; i <= 9; i++) {
            /*
              Constraint: Each number is used at most once
             */
            path.add(i);
            backtracking(i + 1, path);
            path.remove(path.size() - 1);
        }

    }

    public int getSum(List<Integer> nums) {
        int sum = 0;
        for (int i : nums) {
            sum += i;
        }
        return sum;
    }

}
