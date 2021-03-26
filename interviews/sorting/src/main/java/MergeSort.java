/**
 * <p>
 * Merge Sort
 * </p>
 *
 * @author ceezyyy
 * @since 2021/3/26
 */
public class MergeSort {

    public static void sort(int[] arr, int left, int right) {

        if (left >= right) return;

        int mid = left + (right - left) / 2;

        /*
          Divide and Conquer
         */
        sort(arr, left, mid);
        sort(arr, mid + 1, right);
        merge(arr, left, mid, right);

    }


    /*
      Merge two sorted lists
     */
    private static void merge(int[] arr, int left, int mid, int right) {

        int i = left;
        int j = mid + 1;
        int k = 0;
        int n = right - left + 1;
        int[] temp = new int[n];

        while (i <= mid && j <= right) {

            // Choose the smaller one
            if (arr[i] <= arr[j]) {
                temp[k++] = arr[i++];
            } else {
                temp[k++] = arr[j++];
            }

        }

        while (i <= mid) {
            temp[k++] = arr[i++];
        }

        while (j <= right) {
            temp[k++] = arr[j++];
        }

        /*
          temp -> arr
         */
        System.arraycopy(temp, 0, arr, left, n);

    }
}


/**
 * Average: O(nlogn)
 * Best: O(nlogn)
 * Worst: O(nlogn)
 * Space: O(n)
 * Stable
 */
