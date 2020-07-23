# Search a 2D Matrix

## 题目

Write an efficient algorithm that searches for a value in an *m* x *n* matrix. This matrix has the following properties:

- Integers in each row are sorted from left to right.
- The first integer of each row is greater than the last integer of the previous row.

**Example 1:**

```
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
```

**Example 2:**

```
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
```

## 思路

- corner case 判断
- 条件反射：**有序 -> 二分**
- 物理上的二维数组 -> 逻辑上的一维数组



## 题解

```java
class Solution {
    /**
     * 74. Search a 2D Matrix
     * https://leetcode.com/problems/search-a-2d-matrix/
     * Medium
     *
     * @param M
     * @param target
     * @return
     */
    public boolean searchMatrix(int[][] M, int target) {

        // corner case
        if (M == null || M.length == 0) {
            return false;
        }

        int rows = M.length;
        int cols = M[0].length;
        int total = rows * cols;

        // left pointer
        int left = 0;

        // right pointer
        int right = total - 1;

        // binary search
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (target == M[mid / cols][mid % cols]) {
                // bingo
                return true;
            } else if (target > M[mid / cols][mid % cols]) {
                // choose right
                left = mid + 1;
            } else {
                // choose left
                right = mid - 1;
            }
        }

        // could not find
        return false;

    }
}


// Time Complexity: O(logn)
// Space Complexity: O(1)
```



