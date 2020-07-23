# Remove Duplicates from Sorted Array

## 题目

Given a sorted array *nums*, remove the duplicates [**in-place**](https://en.wikipedia.org/wiki/In-place_algorithm) such that each element appear only *once* and return the new length.

Do not allocate extra space for another array, you must do this by **modifying the input array [in-place](https://en.wikipedia.org/wiki/In-place_algorithm)** with O(1) extra memory.

**Example 1:**

```
Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
```

**Example 2:**

```
Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
```

**Clarification:**

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by **reference**, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

```
// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
```

## 思路

题目特点：**有序数组**

快慢指针

- 快指针：扫描元素
- 慢指针：更新 **不重复元素** 的边界

若快指针与慢指针所指元素值不相同，则证明有新的不重复元素，慢指针右移，更新边界

反之，快指针继续扫描



## 题解

```java
class Solution {
    /**
     * 26. Remove Duplicates from Sorted Array
     * https://leetcode.com/problems/remove-duplicates-from-sorted-array/
     * Easy
     *
     * @param nums
     * @return
     */
    public int removeDuplicates(int[] nums) {

        // slow pointer
        // keep tracking the unique element
        int i = 0;

        // fast pointer
        // keep scanning each element
        int j = 1;

        for (j = 0; j < nums.length; j++) {

            // if meet duplicate
            if (nums[i] != nums[j]) {
                i++;
                nums[i] = nums[j];
            }
            // else do nothing

        }

        return i + 1;

    }
}


// Time Complexity: O(n)
// Space Complexity: O(1)
```

