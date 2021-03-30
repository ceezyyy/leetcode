import java.util.Random;

/**
 * <p>
 * Quick Sort
 * </p>
 *
 * @author ceezyyy
 * @since 2021/3/28
 */
public class QuickSort {


    /**
     * The sorting process
     *
     * @param arr
     * @param left
     * @param right
     */
    public static void sort(int[] arr, int left, int right) {

        if (left >= right) return;

        int pivot = randomPartition(arr, left, right);
        sort(arr, left, pivot - 1);
        sort(arr, pivot + 1, right);

    }


    /**
     * Choose a pivot randomly
     *
     * @param arr
     * @param left
     * @param right
     * @return
     */
    public static int randomPartition(int[] arr, int left, int right) {

        int index = left + new Random().nextInt(right - left + 1);
        swap(arr, left, index);

        return partition(arr, left, right);

    }


    /**
     * Finding the partition index of an array
     * [less than pivot], pivot, [greater than pivot]
     *
     * @param arr
     * @param left
     * @param right
     * @return
     */
    public static int partition(int[] arr, int left, int right) {

        int pivot = arr[left];

        int i = left + 1;
        int j = right;

        while (true) {

            /*
              Won't stop until arr[i] >= "pivot"
             */
            while (i <= j && arr[i] < pivot) {
                i++;
            }

            /*
              Won't stop until arr[j] <= "pivot"
             */
            while (i <= j && arr[j] > pivot) {
                j--;
            }

            // We've done
            if (i >= j) break;

            swap(arr, i, j);
            i++;
            j--;

        }

        /*
          Put "pivot" in the correct position
         */
        swap(arr, left, j);
        return j;

    }

    public static void swap(int[] arr, int i, int j) {
        int tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }

}


/**
 * Average: O(nlogn)
 * Best:
 * Worse:
 * Space: O(1)
 * Unstable
 */
