import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums = {1, 2, 2};
        List<List<Integer>> result = new ArrayList<>();
        result = solution.subsetsWithDup(nums);
        System.out.println(result);
    }
}
