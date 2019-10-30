"""
@Topic: 189. Rotate Array
@Date: Oct-30 2019
@Author: ceezyyy
@Difficulty: Easy 
"""

from typing import List

# Solution One


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #  in-place with O(n) extra space
        size = len(nums)
        res = list(nums)  # res is a copy of nums
        for i in range(size):
            if (i+k) < size:
                nums[i+k] = res[i]
            else:
                # the thought is equivalent to circular linked list
                nums[(i+k) % size] = res[i]  # here is '%'
        # print(nums)


# testing
def test():
    s = Solution()
    s.rotate([-1, -100, 3, 99], 2)
    s.rotate([1, 2, 3, 4, 5, 6, 7], 3)


if __name__ == "__main__":
    test()
