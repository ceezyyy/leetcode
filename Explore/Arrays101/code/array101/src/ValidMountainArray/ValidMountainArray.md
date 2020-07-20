# Valid Mountain Array

## 题目

Given an array `A` of integers, return `true` if and only if it is a *valid mountain array*.

Recall that A is a mountain array if and only if:

- `A.length >= 3`

- There exists some `i` with `0 < i < A.length - 1`

   such that:

  - `A[0] < A[1] < ... A[i-1] < A[i]`
  - `A[i] > A[i+1] > ... > A[A.length - 1]`

**Example 1:**

```
Input: [2,1]
Output: false
```

**Example 2:**

```
Input: [3,5,5]
Output: false
```

**Example 3:**

```
Input: [0,3,2,1]
Output: true
```



<div align="center"> <img src="hint_valid_mountain_array.png" width="50%"/> </div><br>

**Note:**

1. `0 <= A.length <= 10000`
2. `0 <= A[i] <= 10000 `

 

## 思路

- 找 `peak` 元素，且在遍历过程中判断元素是否严格升序
- 若找到：判断之后的元素是否严格降序；若没有找到，直接返回 `false`

## 题解

```java
class Solution {
    public boolean validMountainArray(int[] A) {

        // index of peak element
        int peak = -1;

        // corner case
        if (A.length < 3) {
            return false;
        }

        for (int i = 1; i < A.length - 1; i++) {
            // increasing
            if (A[i - 1] >= A[i]) {
                return false;
            }
            // find the index of peak element
            if ((A[i - 1] < A[i]) && (A[i] > A[i + 1])) {
                peak = i;
                break;
            }
        }

        // peak does not exist
        if (peak == -1) {
            return false;
        }

        // decreasing
        for (int j = peak; j < A.length - 1; j++) {
            if (A[j] <= A[j + 1]) {
                return false;
            }
        }

        return true;

    }
}


// Time Complexity: O(n)
// Space Complexity: O(1)
```

