"""
@Title: 303. Range Sum Query - Immutable
@Tag: dp
@Date: Dec-29 2019
@Author: ceezyyy
@Difficulty: Easy
"""


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        # cumulative sum from 0 to the current position(index)
        for k in range(1, len(self.nums)):  # here should be 'k' (do not place 'i' or 'j' here)
            # such as dp[], but here we just update the original array instead, which means no extra space
            self.nums[k] += self.nums[k-1]

    # There are many calls to sumRange function
    # no corner case this time
    def sumRange(self, i: int, j: int) -> int:
        return self.nums[j]-(self.nums[i-1] if i > 0 else 0)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)


"""
Runtime: 80 ms, faster than 85.46% of Python3 online submissions for Range Sum Query - Immutable.
Memory Usage: 16.2 MB, less than 100.00% of Python3 online submissions for Range Sum Query - Immutable.
"""


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
