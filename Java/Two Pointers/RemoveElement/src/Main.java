public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] testArray = {0, 1, 2, 2, 3, 0, 4, 2};
        int testVal = 2;
        int result = solution.removeElement(testArray, testVal);
        System.out.println(result);

    }
}
