/**
 * <p>
 * Selection Sort
 * Finding the smallest element in the unsorted sublist
 * </p>
 *
 * @author ceezyyy
 * @since 2021/3/26
 */
public class SelectionSort {

    public static int[] sort(int[] arr) {

        int n = arr.length;

        /*
          Sorted sublist: [0, i)
          Unsorted sublist: [i, n)
         */
        for (int i = 0; i < n - 1; i++) {

            /*
              Initialize the index of minimum element
             */
            int min = i;

            /*
              Find the index of the minimum element
             */
            for (int j = i + 1; j < n; j++) {
                if (arr[j] < arr[min]) min = j;
            }

            if (min != i) swap(arr, i, min);

        }

        return arr;

    }

    private static void swap(int[] arr, int i, int j) {
        int tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }

}


/**
 * Average: O(n^2)
 * Best: O(n^2)
 * Worst: O(n^2)
 * Space: O(1)
 * Unstable
 */
