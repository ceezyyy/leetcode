# Check If N and Its Double Exist

## 题目

Given an array `arr` of integers, check if there exists two integers `N` and `M` such that `N` is the double of `M` ( i.e. `N = 2 * M`).

More formally check if there exists two indices `i` and `j` such that :

- `i != j`
- `0 <= i, j < arr.length`
- `arr[i] == 2 * arr[j]`

 

**Example 1:**

```
Input: arr = [10,2,5,3]
Output: true
Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.
```

**Example 2:**

```
Input: arr = [7,1,14,11]
Output: true
Explanation: N = 14 is the double of M = 7,that is, 14 = 2 * 7.
```

**Example 3:**

```
Input: arr = [3,1,7,11]
Output: false
Explanation: In this case does not exist N and M, such that N = 2 * M.
```

 

**Constraints:**

- `2 <= arr.length <= 500`
- `-10^3 <= arr[i] <= 10^3`

## 思路

最初是想用 `hashmap` 存储元素，查找效率快，后来发现没必要存 `kv`，就改成 `hashset`

这题采用不排序的方法，遍历数组，判断两种情况：

1. 该元素的两倍是否已存在
2. 该元素的 `1/2` 是否已存在（该元素为偶数）



若两种都不符合，则将该元素加入到 `hashset` 中（注意添加元素的顺序，先判断后添加，以避免元素 `0` 的干扰）





## 题解

```java
/**
 * 1346. Check If N and Its Double Exist
 * https://leetcode.com/problems/check-if-n-and-its-double-exist/
 * Easy
 *
 * @author ceezyyy
 */
class Solution {
    public boolean checkIfExist(int[] arr) {

        Set<Integer> set = new HashSet<>();

        for (int i = 0; i < arr.length; i++) {
            if (set.contains(arr[i] * 2) || (arr[i] % 2 == 0 && set.contains(arr[i] / 2))) {
                return true;
            } else {
                // add element to set
                set.add(arr[i]);
            }
        }

        return false;

    }

}


// Time Complexity: O(n)
// Space Complexity: O(n)
```

