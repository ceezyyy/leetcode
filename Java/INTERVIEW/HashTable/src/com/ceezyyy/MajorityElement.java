/*
 * Topic: 169. Majority Element
 * Tag: HashMap
 * Updated time: 03/12/2020
 */


class Solution {
    public int majorityElement(int[] nums) {
        if (nums.length == 1) {
            return nums[0];
        }
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i : nums) {
            if (map.containsKey(i) && map.get(i) + 1 > nums.length / 2) {
                return i;
            } else {
                map.put(i, map.getOrDefault(i, 0) + 1);
            }
        }
        return -1;
    }
}


/*
Runtime: 11 ms, faster than 26.02% of Java online submissions for Majority Element.
Memory Usage: 47.2 MB, less than 5.15% of Java online submissions for Majority Element.
*/


/*
Time Complexity: O(n)
Space Complexity: O(1)
*/
