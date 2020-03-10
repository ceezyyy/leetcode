class Solution {
    public int[] plusOne(int[] A) {
        for (int i = A.length - 1; i >= 0; i--) {
            /*
             * From the very beginning
             * if current bit is greater less than 9
             * plus one and return the digit immediately
             * else set it as zero, then continue
             */
            if (A[i] < 9) {
                A[i]++;
                return A;
            }
            A[i] = 0;
        }
        /*
         * Add one new digit
         */
        int[] res = new int[A.length + 1];
        res[0] = 1;
        return res;
    }
}

