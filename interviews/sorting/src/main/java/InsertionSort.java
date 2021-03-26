/**
 * <p>
 * Insertion Sort
 * Finding the location of data[i] within the sorted list
 * </p>
 *
 * @author ceezyyy
 * @since 2021/3/26
 */
public class InsertionSort {

    public static int[] sort(int[] arr) {

        int n = arr.length;

        for (int i = 1; i < n; i++) {

            /*
              Pick the card
             */
            int card = arr[i];

            int j = i - 1;
            while (j >= 0 && arr[j] > card) {
                arr[j + 1] = arr[j];
                j--;
            }

            /*
              Placing card at its correct position
             */
            arr[j + 1] = card;

        }

        return arr;

    }

}


/**
 * Average: O(n^2)
 * Best: O(n)
 * Worse: O(n^2)
 * Space: O(1)
 * Stable
 */
