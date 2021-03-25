import java.util.ArrayList;
import java.util.List;

class CombinationIterator {

    private List<String> result = new ArrayList<>();
    // There will be at most 10^4 function calls per test
    // The  pointer of CombinationIterator
    private int index = 0;

    public CombinationIterator(String characters, int combinationLength) {
        // Get result from backtracking()
        backtracking(characters.toCharArray(), combinationLength, new StringBuilder(), 0);
    }

    public void backtracking(char[] originArray, int n, StringBuilder runningChoices, int start) {

        // Goal: We have made all decisions
        if (runningChoices.length() == n) {
            result.add(new String(runningChoices));
            return;
        }

        // Decision tree traversal
        for (int i = start; i < originArray.length; i++) {

            char choice = originArray[i];

            // 1. Add current choice to our current choice list
            runningChoices.append(choice);
            // 2. Jump into the next level of decision tree
            backtracking(originArray, n, runningChoices, i + 1);
            // 3. Undo current choice
            runningChoices.deleteCharAt(runningChoices.length() - 1);

        }
    }

    public String next() {
        // It's guaranteed that all calls of the function next are valid
        return result.get(index++);
    }

    public boolean hasNext() {
        return index < result.size() ? true : false;
    }
}

/**
 * Your CombinationIterator object will be instantiated and called as such:
 * CombinationIterator obj = new CombinationIterator(characters, combinationLength);
 * String param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */