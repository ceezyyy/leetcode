# Squares of a Sorted Array

## 题目

Given an array of integers `A` sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

 

**Example 1:**

```
Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
```

**Example 2:**

```
Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]
```

 

**Note:**

1. `1 <= A.length <= 10000`

2. `-10000 <= A[i] <= 10000`

3. `A` is sorted in non-decreasing order.

   

## 思路

这道题考察 `two pointers`

因为平方只考虑绝对值，所以最大的元素肯定在最左或者最右（题目特征）

放元素的顺序采用 **从大到小**，这样的好处在于不管元素正负与否，都能满足条件

`left`，`right` 俩指针控制左右边界，边界元素两两比较，大的元素就加入结果数组，直到左右边界不满足条件



## 题解

```java
/**
 * 977. Squares of a Sorted Array
 * https://leetcode.com/problems/squares-of-a-sorted-array/
 * Easy
 *
 * @author ceezyyy
 */
class Solution {
    public int[] sortedSquares(int[] A) {

        int n = A.length;

        // left pointer
        int left = 0;

        // right pointer
        int right = n - 1;

        // result array
        int[] result = new int[n];

        // the place of current element
        int index = n - 1;

        while (left <= right) {
            if (A[left] * A[left] >= A[right] * A[right]) {
                // choose left
                result[index] = A[left] * A[left];
                index--;
                left++;
            } else {
                // choose right
                result[index] = A[right] * A[right];
                index--;
                right--;
            }
        }

        return result;

    }
}


// Time Complexity: O(n)
// Space Complexity: O(1)
```



