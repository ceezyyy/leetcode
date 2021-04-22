/**
 * <p>
 * 242. Valid Anagram (Easy)
 * https://leetcode.com/problems/valid-anagram/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/4/19
 */
public class ValidAnagram {
    public boolean isAnagram(String s, String t) {

        // s and t consist of lowercase English letters
        int[] visited = new int[26];

        for (char c : s.toCharArray()) {
            int e = c - 'a';
            visited[e]++;
        }

        for (char c : t.toCharArray()) {
            int e = c - 'a';
            visited[e]--;
        }

        for (int e : visited) {
            if (e != 0) return false;
        }

        return true;

    }
}
