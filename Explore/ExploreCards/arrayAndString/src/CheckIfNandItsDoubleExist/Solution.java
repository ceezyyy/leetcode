package CheckIfNandItsDoubleExist;

import java.util.HashSet;
import java.util.Set;

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