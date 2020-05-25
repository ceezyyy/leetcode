/**
 * @Topic 344. Reverse String
 * @Author Yi Cai
 * @Tag Recursion
 * @Date 3/27/2020 12:32 PM
 **/


class Solution {
    public void reverseString(char[] s) {
        recurse(s, 0, s.length - 1);
    }

    private void recurse(char[] originArray, int left, int right) {
        // Our goal
        if (left >= right) return;

        // Our choice
        char temp = originArray[left];
        originArray[left] = originArray[right];
        originArray[right] = temp;

        recurse(originArray, left + 1, right - 1);
    }
}


// Time Complexity: O(n)
// Space Complexity: O(n)

