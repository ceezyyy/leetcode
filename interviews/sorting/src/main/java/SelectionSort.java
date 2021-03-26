/**
 * <p>
 * 选择排序法
 * 每次都在未排序的元素中选择最小的
 * </p>
 *
 * @author ceezyyy
 * @since 2021/3/26
 */
public class SelectionSort {

    public static int[] sort(int[] arr) {

        int n = arr.length;

        /*
          Sorted: [0, i)
          Unsorted: [i, n]
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
 * 平均: O(n^2)
 * 最好: O(n^2)
 * 最坏: O(n^2)
 * 空间: O(1)
 * 是否稳定: 不稳定
 */
