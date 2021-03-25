# Practices for Backtracking

Table of Contents
-----------------

* [Count Sorted Vowel Strings](#count-sorted-vowel-strings)
* [Iterator for Combination](#iterator-for-combination)


## Count Sorted Vowel Strings

**Example**

```
Input: n = 2
Output: 15
Explanation: The 15 sorted strings that consist of vowels only are
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.
```

**Explained**



**Solution.java**

```java
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
```

## Iterator for Combination

**Example**

```
CombinationIterator iterator = new CombinationIterator("abc", 2); // creates the iterator.

iterator.next(); // returns "ab"
iterator.hasNext(); // returns true
iterator.next(); // returns "ac"
iterator.hasNext(); // returns true
iterator.next(); // returns "bc"
iterator.hasNext(); // returns false
```

**Explained**



**CombinationIterator.java**

```java
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
```