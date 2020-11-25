import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * Letter Combinations of a Phone Number
 */
class Solution {

    private List<String> result = new ArrayList<>();
    private static Map<Character, String> map = new HashMap<>();
    private String value;

    public List<String> letterCombinations(String digits) {

        // Corner case
        // digits[i] is a digit in the range ['2', '9']
        if (digits.isEmpty()) return result;

        map.put('2', "abc");
        map.put('3', "def");
        map.put('4', "ghi");
        map.put('5', "jkl");
        map.put('6', "mno");
        map.put('7', "pqrs");
        map.put('8', "tuv");
        map.put('9', "wxyz");

        backtracking(digits, map, 0, new StringBuilder());
        return result;

    }

    public void backtracking(String digits, Map<Character, String> map, int level, StringBuilder runningChoices) {

        // Goal: We have made all decisions
        if (level == digits.length()) {
            result.add(new String(runningChoices));
            return;
        }

        // Decision tree traversal
        // At each level we make different decisions
        value = map.get(digits.charAt(level));
        for (char choice : value.toCharArray()) {

            // 1. Add current choice to our current choice list
            runningChoices.append(choice);
            // 2. Jump into the next level of decision tree
            backtracking(digits, map, level + 1, runningChoices);
            // 3. Undo current choice
            runningChoices.deleteCharAt(runningChoices.length() - 1);

        }
    }
}