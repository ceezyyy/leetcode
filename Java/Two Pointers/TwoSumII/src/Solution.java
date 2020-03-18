/**
 * @Topic 167. Two Sum II - Input array is sorted
 * @Author Yi Cai
 * @Tag Two Pointers
 * @Date 3/18/2020 6:33 PM
 **/


class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int[] result = new int[2];
        int i = 0;  // left pointer
        int j = numbers.length - 1;  // right pointer
        while (i < j) {  // two numbers, so "i != j"
            int sum = numbers[i] + numbers[j];
            if (sum == target) {  // not zero-based
                result[0] = i + 1;
                result[1] = j + 1;
                return result;
            } else if (sum < target) {
                i++;
            } else {
                j--;
            }
        }
        return result;
    }
}


// Time Complexity: O(n)
// Space Complexity: O(1)
