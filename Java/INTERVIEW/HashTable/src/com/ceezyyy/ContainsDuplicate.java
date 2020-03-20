/*
 * Topic: 217. Contains Duplicate
 * Tag: HashSet
 * Updated time: 03/12/2020
 */


import java.util.HashSet;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> set = new HashSet<Integer>();
        for (int i : nums) {
            if (set.contains(i)) {
                return true;
            }
            set.add(i);
        }
        return false;
    }
}


/*
Time Complexity: O(n)
Space Complexity: O(n)
*/
