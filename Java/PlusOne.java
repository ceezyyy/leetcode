class Solution {
    public int[] plusOne(int[] A) {
        for (int i = A.length - 1; i >= 0; i--) {
            if (A[i] < 9) {
                A[i]++;
                return A;
            }
            A[i] = 0;
        }
        int[] res = new int[A.length + 1];
        res[0] = 1;
        return res;
    }
}

