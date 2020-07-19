# Find Numbers with Even Number of Digits

## 题目

Given an array `nums` of integers, return how many of them contain an **even number** of digits.

**Example 1:**

```
Input: nums = [12,345,2,6,7896]

Output: 2

Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.
```

**Example 2:**

```
Input: nums = [555,901,482,1771]

Output: 1 

Explanation: 
Only 1771 contains an even number of digits.
```

**Constraints:**

- `1 <= nums.length <= 500`
- `1 <= nums[i] <= 10^5`

## 思路

这道题很简单，关键在于判断一个数是几位数



太久没做题导致犯了一个小错误，舍去最后一位数是用 `/`，而第一次写的时候误用了 `%` （`%` 是用来保留最后一位数的）



得到的教训：

1. `debug` 很有用
2. `leetcode` 刷起来

## 题解

```java
package FindNumberswithEvenNumberofDigits;

/**
 * 1295. Find Numbers with Even Number of Digits
 * https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
 * Easy
 *
 * @author ceezyyy
 */
class Solution {
    public int findNumbers(int[] nums) {
        int result = 0;
        for (int i = 0; i < nums.length; i++) {
            // even digit
            if (countDigit(nums[i]) % 2 == 0) {
                result++;
            }
        }
        return result;
    }


    public int countDigit(int num) {
        int digit = 1;
        while ((num / 10) != 0) {
            num /= 10;
            digit++;
        }
        return digit;
    }
}


// Time Complexity: O(n)
// Space Complexity: O(1)
```



 