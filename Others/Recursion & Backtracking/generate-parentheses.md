# Generate Parentheses

**Example**

```
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
```

**Explained**





**Solution.java**

```java
/**
 * Generate Parentheses
 */
class Solution {

    private List<String> result = new ArrayList<>();

    public List<String> generateParenthesis(int n) {
        // 1 <= n <= 8
        backtracking(n, n, new StringBuilder());
        return result;
    }

    public void backtracking(int left, int right, StringBuilder runningChoices) {

        // Goal: We have made all decisions
        if (left == 0 && right == 0) {
            result.add(new String(runningChoices));
            return;
        }

        // Decision tree traversal
        if (left > 0) {
            runningChoices.append("(");
            backtracking(left - 1, right, runningChoices);
            runningChoices.deleteCharAt(runningChoices.length() - 1);
        }

        // e.g: "())" is not a valid parentheses
        if (right > left) {
            runningChoices.append(")");
            backtracking(left, right - 1, runningChoices);
            runningChoices.deleteCharAt(runningChoices.length() - 1);
        }

    }
}
```