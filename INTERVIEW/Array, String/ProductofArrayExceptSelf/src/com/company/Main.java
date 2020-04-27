package com.company;

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] productExceptSelf = solution.productExceptSelf(new int[]{1, 2, 3, 4});

        for (int a : productExceptSelf) {
            System.out.println(a);
        }
    }
}
