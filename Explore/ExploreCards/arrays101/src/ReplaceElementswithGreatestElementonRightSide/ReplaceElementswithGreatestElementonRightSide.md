# Replace Elements with Greatest Element on Right Side

## 题目

Given an array `arr`, replace every element in that array with the greatest element among the elements to its right, and replace the last element with `-1`.

After doing so, return the array.



**Example 1:**

```
Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
```

 

**Constraints:**

- `1 <= arr.length <= 10^4`
- `1 <= arr[i] <= 10^5`



## 思路

第一反应是递减栈，想了一下可以更简单

对于当前元素：

- 只关心右边最大的元素，所以可以定义一个变量 keep tracking 最大值
- 在 `in-place` 替换的时候更新该变量（注意顺序）



## 题解

```java
/**
 * 1299. Replace Elements with Greatest Element on Right Side
 * https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
 * Easy
 *
 * @author ceezyyy
 */
class Solution {
    public int[] replaceElements(int[] arr) {

        // the greatest element on right side
        int maxOfRight = -1;
        int temp = -1;

        // walk through from right to left
        for (int i = arr.length - 1; i >= 0; i--) {

            // store the value of arr[i]
            temp = arr[i];

            // replace
            arr[i] = maxOfRight;

            if (temp > maxOfRight) {
                maxOfRight = temp;
            }
        }

        return arr;

    }
}


// Time Complexity: O(n)
// Space Complexity: O(1)
```

