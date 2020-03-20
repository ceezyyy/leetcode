/*
 * Topic: 136. Single Number
 * Tag: HashSet
 * Updated time: 03/12/2020
 */


import java.util.HashSet;

class Solution {
    public int singleNumber(int[] nums) {
        HashSet<Integer> set = new HashSet<Integer>();
        for (int i : nums) {
            if (set.contains(i)) {
                set.remove(i);
            } else {
                set.add(i);
            }
        }
        for (int i : set) {
            return i;
        }
        return -1;
    }
}


/*
Time Complexity: O(n)
Space Complexity: O(n)
*/

