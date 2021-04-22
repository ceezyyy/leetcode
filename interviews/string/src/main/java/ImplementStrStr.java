/**
 * <p>
 * 28. Implement strStr() (Easy)
 * KMP Algorithm: First occurrence of substring
 * https://leetcode.com/problems/implement-strstr/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/4/20
 */
public class ImplementStrStr {

    private char[] arr;
    private char[] subArr;
    private int n1;
    private int n2;

    public int strStr(String haystack, String needle) {

        // Corner case 1
        if (needle.isEmpty()) return 0;

        char first = needle.charAt(0);
        this.arr = haystack.toCharArray();
        this.subArr = needle.toCharArray();
        this.n1 = arr.length;
        this.n2 = subArr.length;

        // Corner case 2
        if (n2 > n1) return -1;

        // Find the first char of "subArr"
        for (int i = 0; i < n1; i++) {
            if (arr[i] == first) {
                // Match
                if (isMatch(i)) return i;
                // Mismatch -> keep searching
                continue;
            }
        }

        return -1;

    }

    public boolean isMatch(int base) {
        for (int i = 0; i < n2; i++) {
            int index = base + i;
            if (index >= n1 || arr[index] != subArr[i]) return false;
        }
        return true;
    }

}


/**
 * dsd
 */
