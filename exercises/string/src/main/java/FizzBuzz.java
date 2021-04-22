import java.util.ArrayList;
import java.util.List;

/**
 * <p>
 * 412. Fizz Buzz (Easy)
 * https://leetcode.com/problems/fizz-buzz/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/4/22
 */
public class FizzBuzz {

    private static final String fizzBuzz = "FizzBuzz";
    private static final String fizz = "Fizz";
    private static final String buzz = "Buzz";
    private List<String> res = new ArrayList<>();

    public List<String> fizzBuzz(int n) {

        for (int i = 1; i <= n; i++) {
            if (i % 3 == 0 && i % 5 == 0) {
                res.add(fizzBuzz);
            } else if (i % 3 == 0) {
                res.add(fizz);
            } else if (i % 5 == 0) {
                res.add(buzz);
            } else {
                res.add(String.valueOf(i));
            }
        }

        return res;

    }
}
