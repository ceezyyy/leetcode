import java.util.HashSet;
import java.util.Set;

/**
 * @Topic 217. Contains Duplicate
 * @Author Yi Cai
 * @Tag Hashtable
 * @Date 3/29/2020 7:57 PM
 **/


class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (int i : nums) {
            if (set.contains(i)) return true;
            set.add(i);
        }
        return false;
    }
}


// Time Complexity: O(n)
// Space Complexity: O(n)

