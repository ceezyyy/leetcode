import java.util.HashMap;
import java.util.Map;
import java.util.Stack;


/**
 * @Topic 20. Valid Parentheses
 * @Author Yi Cai
 * @Tag Stack
 * @Date 4/4/2020 8:07 PM
 **/


class Solution {
    public boolean isValid(String s) {
        // Initialize hashtable
        Map<Character, Character> map = new HashMap<>();
        map.put('(', ')');
        map.put('{', '}');
        map.put('[', ']');

        // Match the parentheses
        Stack<Character> stack = new Stack<>();

        for (char ch : s.toCharArray()) {
            if (!map.containsKey(ch)) {
                // Nothing to be matched
                if (stack.isEmpty()) {
                    return false;
                }
                // Not the valid parentheses
                if (map.get(stack.pop()) != ch) {
                    return false;
                }
            } else {
                stack.push(ch);
            }
        }

        // All should be matched and nothing left
        return stack.isEmpty();
    }
}


// Time Complexity: O(n)
// Space Complexity: O(n)

