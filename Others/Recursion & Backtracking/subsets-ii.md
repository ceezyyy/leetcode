# Subsets II

**Example**

```
Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
```





**Explained**





**Solution.java**

```java
/**
 * Subsets II
 */
class Solution {

    private List<List<Integer>> result = new ArrayList<>();

    public List<List<Integer>> subsetsWithDup(int[] nums) {
        // Avoid duplicates, see line 22
        Arrays.sort(nums);
        backtracking(nums, new ArrayList<Integer>(), 0);
        return result;
    }

    public void backtracking(int[] nums, List<Integer> runningChoices, int start) {

        result.add(new ArrayList<>(runningChoices));

        // Decision tree traversal
        for (int i = start; i < nums.length; i++) {

            int choice = nums[i];

            // Constraint (origin array should be sorted)
            // Do not use "result.contains()", which will cause O(n) time complexity
            if (i > start && choice == nums[i - 1]) continue;

            // 1. Add current choice to our running choice list
            runningChoices.add(choice);
            // 2. Jump into the next level of decision tree
            backtracking(nums, runningChoices, i + 1);
            // 3. Undo current choice
            runningChoices.remove(runningChoices.size() - 1);

        }
    }
}
```

