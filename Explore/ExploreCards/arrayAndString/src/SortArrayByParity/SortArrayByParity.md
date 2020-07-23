# Sort Array By Parity

## 题目

Given an array `A` of non-negative integers, return an array consisting of all the even elements of `A`, followed by all the odd elements of `A`.

You may return any answer array that satisfies this condition.

 

**Example 1:**

```
Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
```

 

**Note:**

1. `1 <= A.length <= 5000`
2. `0 <= A[i] <= 5000`

## 思路

如果使用辅助数组，则是一道非常简单的题

遍历元素，根据奇偶性：

- 偶数，从头加
- 奇数，从尾加



## 题解

```java
/**
 * 905. Sort Array By Parity
 * https://leetcode.com/problems/sort-array-by-parity/
 * Easy
 *
 * @author ceezyyy
 */
class Solution {
    public int[] sortArrayByParity(int[] A) {

        int n = A.length;
        int[] arr = new int[n];

        // two pointers
        int left = 0;
        int right = n - 1;

        // [even, odd]
        for (int i = 0; i < n; i++) {
            // even
            if (A[i] % 2 == 0) {
                arr[left] = A[i];
                left++;
            } else {
                // odd
                arr[right] = A[i];
                right--;
            }
        }

        return arr;

    }
}


// Time Complexity: O(n)
// Space Complexity: O(n)
```

