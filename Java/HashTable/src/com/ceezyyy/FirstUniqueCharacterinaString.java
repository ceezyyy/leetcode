/*
 * Topic: 387. First Unique Character in a String
 * Tag: HashMap
 * Updated time: 03/13/2020
 */


class Solution {
    public int firstUniqChar(String s) {
        int res = -1;
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        /* Record the freq of each character in the hashtable */
        for (int i = 0; i < s.length(); i++) {
            map.put(s.charAt(i), map.getOrDefault(s.charAt(i), 0) + 1);
        }
        for (int i = 0; i < s.length(); i++) {
            if (map.get(s.charAt(i)) == 1) {
                /* return immediately to make sure it's the first unique char */
                return i;
            }
        }
        return res;
    }
}


/*
Time Complexity: O(n)
Space Complexity: O(n)
*/
