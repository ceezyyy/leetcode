/**
 * <p>
 * 344. Reverse String (Easy)
 * https://leetcode.com/problems/reverse-string/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/4/19
 */
public class ReverseString {

    private char[] s;

    public void reverseString(char[] s) {

        this.s = s;
        int i = 0;
        int j = s.length - 1;

        while (i < j) {
            swap(i, j);
            i++;
            j--;
        }

    }

    public void swap(int i, int j) {
        char tmp = s[i];
        s[i] = s[j];
        s[j] = tmp;
    }

}
