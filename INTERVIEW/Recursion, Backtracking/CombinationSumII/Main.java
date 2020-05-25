import javax.swing.event.ListDataEvent;
import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] candidates = {10, 1, 2, 7, 6, 1, 5};
        int target = 8;
        List<List<Integer>> result = new ArrayList<>();
        result = solution.combinationSum2(candidates, target);
        System.out.println(result);
    }
}