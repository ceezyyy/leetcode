# Permutations

Given an array `nums` of distinct integers, return *all the possible permutations*. You can return the answer in **any order**.

 

**Example**

```
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```





**Explained**









**Solution.java**

```java
/**
 * Permutations
 */
class Solution {

    private List<List<Integer>> result = new ArrayList<>();

    public List<List<Integer>> permute(int[] nums) {
        // 1 <= nums.length <= 6
        backtracking(nums, new ArrayList<Integer>());
        return result;
    }

    public void backtracking(int[] nums, List<Integer> runningChoices) {

        // Reach the goal: we have made all the decisions
        if (runningChoices.size() == nums.length) {
            result.add(new ArrayList(runningChoices));
            // Do not forget to return
            return;
        }

        // Decision tree traversal
        for (int i = 0; i < nums.length; i++) {

            int choice = nums[i];

            // All the integers of nums are unique
            // Skip if current choice is in our choice list
            if (runningChoices.contains(choice)) continue;

            // 1. Add current choice to our current choice list
            runningChoices.add(choice);
            // 2. Jump into the next level of decision tree
            backtracking(nums, runningChoices);
            // 3. Undo current choice
            runningChoices.remove(runningChoices.size() - 1);

        }
    }
}
```