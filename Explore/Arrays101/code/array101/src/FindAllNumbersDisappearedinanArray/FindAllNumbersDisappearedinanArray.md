# Find All Numbers Disappeared in an Array

## 题目

Given an array of integers where 1 ≤ a[i] ≤ *n* (*n* = size of array), some elements appear twice and others appear once.

Find all the elements of [1, *n*] inclusive that do not appear in this array.

Could you do it without extra space and in O(*n*) runtime? You may assume the returned list does not count as extra space.

**Example:**

```
Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
```

## 思路

这题要求：

- O(n)
- in-place

既然题目的数据有限制（[1, n]），那么我们可以：

- 每个元素都有对应的 `index`，关系是 **index = 元素的值 - 1**
- 通过标记元素为负来记录已出现过的元素
- 最后找出没有被标记过的元素即可



## 题解

```java
/**
 * 448. Find All Numbers Disappeared in an Array
 * https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
 * Easy
 *
 * @author ceezyyy
 */
class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {

        // the 'right place' of current element
        int rightPlace = 0;

        List<Integer> result = new ArrayList<>();

        // corner case
        if (nums.length == 0 || nums == null) {
            return result;
        }

        // all the elements of [1, n]
        // e.g: 1 -> nums[0], 2 -> nums[1], 3 -> nums[2]
        // each element has its own place
        for (int i = 0; i < nums.length; i++) {

            // find the place of current element
            if (nums[i] < 0) {
                rightPlace = -nums[i];
            } else {
                rightPlace = nums[i];
            }

            rightPlace--;

            if (nums[rightPlace] > 0) {
                // mark this negative
                // which means the corresponding element already exists
                nums[rightPlace] = -nums[rightPlace];
            }
            // else do nothing
        }

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > 0) {
                // the corresponding element does not exist
                result.add(i + 1);
            }
        }

        return result;

    }
}


// Time Complexity: O(n)
// Space Complexity: O(1)
```



