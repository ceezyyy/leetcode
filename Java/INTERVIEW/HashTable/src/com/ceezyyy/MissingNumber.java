/*
 * Topic: 268. Missing Number
 * Tag: HashSet
 * Updated time: 03/13/2020
 */


class Solution {
    public int missingNumber(int[] nums) {
        HashSet<Integer> set = new HashSet<Integer>();
        for (int i : nums) {
            set.add(i);
        }
        for (int i = 0; i <= nums.length; i++) {
            if (!set.contains(i)) {
                return i;
            }
        }
        return -1;
    }
}


/*
Time Complexity: O(n)
Space Complexity: O(n)
*/
