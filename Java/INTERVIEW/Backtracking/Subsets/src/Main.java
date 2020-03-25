import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums = {1, 2, 3};
        List<List<Integer>> result = new ArrayList<>();
        result = solution.subsets(nums);
        System.out.println(result);
    }
}
