import java.util.ArrayList;
import java.util.List;

/**
 * Count Sorted Vowel Strings
 */
class Solution {

    private static String vowelString = "aeiou";
    private static char[] vowels = vowelString.toCharArray();
    private int result = 0;

    public int countVowelStrings(int n) {
        // Corner case
        // 1 <= n <= 50
        if (n == 1) return vowels.length;
        backtracking(n, new ArrayList<Character>(), 0);
        return result;
    }

    public void backtracking(int n, List<Character> runningChoices, int start) {

        // We have made all decisions
        if (n == runningChoices.size()) {
            result++;
            return;
        }

        // Decision tree traversal
        for (int i = start; i < vowels.length; i++) {

            // 1. Make decision
            runningChoices.add(vowels[i]);
            // 2. Jump into the next level of decision tree
            backtracking(n, runningChoices, i);
            // 3. Undo current decision
            runningChoices.remove(runningChoices.size() - 1);

        }
    }
}