import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

/**
 * <p>
 * 345. Reverse Vowels of a String (Easy)
 * https://leetcode.com/problems/reverse-vowels-of-a-string/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/3/24
 */
class ReverseVowels {
    public String reverseVowels(String s) {

        if (s == null || s.isEmpty()) return s;

        Set<Character> set = new HashSet<>(Arrays.asList('a', 'e', 'i', 'o', 'u',
                'A', 'E', 'I', 'O', 'U'));

        char a, b = ' ';
        char[] arr = s.toCharArray();
        // head
        int i = 0;
        // tail
        int j = arr.length - 1;

        while (i < j) {

            a = arr[i];
            b = arr[j];


            if (set.contains(a) && set.contains(b)) {
                swap(arr, i, j);
                i++;
                j--;
            } else if (set.contains(a)) {
                j--;
            } else if (set.contains(b)) {
                i++;
            } else {
                i++;
                j--;
            }

        }

        return new String(arr);

    }

    public void swap(char[] arr, int i, int j) {
        char tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }

}
