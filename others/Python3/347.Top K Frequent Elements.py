"""
@Title: 347. Top K Frequent Elements
@Tag: Counter
@Date: Nov-13 2019
@Author: ceezyyy
@Difficulty: Medium
"""


import collections
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [item[0] for item in collections.Counter(nums).most_common(k)]


def test():
    s = Solution()
    res = s.topKFrequent([1, 1, 1, 2, 2, 3], 3)
    print(res)


if __name__ == "__main__":
    test()


"""
Runtime: 104 ms, faster than 98.05% of Python3 online submissions for Top K Frequent Elements.
Memory Usage: 17.1 MB, less than 6.25% of Python3 online submissions for Top K Frequent Elements.
"""
