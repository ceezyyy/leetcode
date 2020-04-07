public class Main {

    public static void quickSort(int[] nums, int left, int right) {
        if (left < right) {
            int pivotPosition = partition(nums, left, right);
            /*
             * Left part
             * */
            quickSort(nums, left, pivotPosition - 1);
            /*
             * Right part
             * */
            quickSort(nums, pivotPosition + 1, right);
        }
    }

    /*
     * Partition
     * */
    public static int partition(int[] nums, int left, int right) {

        /*
         * The element that we want to find to position for
         * we choose the rightmost one
         * */
        int pivot = nums[right];

        /*
         * i will keep track of the index
         * which is the 'tail' of the section of items less than the pivot
         * here we set i as -1 initially in case of the worst case (descending)
         * */
        int i = left - 1;

        /*
         * j is the scanning pointer
         * scan from left to right - 1 (inclusive)
         * */
        for (int j = left; j < right; j++) {
            if (nums[j] <= pivot) {
                i++;
                swap(nums, i, j);
            }
        }
        swap(nums, i + 1, right);
        return i + 1;
    }


    /*
     * Swap two elements (Reference)
     * */
    public static void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }


    public static void main(String[] args) {
        int[] nums = {3, 2, 1, 5, 6, 4};
        quickSort(nums, 0, nums.length - 1);
        for ( int num : nums) {
            System.out.println(num);
        }
    }
}
