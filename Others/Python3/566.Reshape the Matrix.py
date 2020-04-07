"""
@Title: 566. Reshape the Matrix
@Tag: array
@Date: Apr-07 2020
@Author: ceezyyy
@Difficulty: Easy
"""


# Approach 1: (Using queue)

class Solution:
    def matrixReshape(self, nums: List[List[int]], rows: int, cols: int) -> List[List[int]]:
        m = len(nums)
        n = len(nums[0])

        # Corner case
        if (m == rows and n == cols) or (rows * cols > m * n):
            return nums

        # Store in queue
        A = []
        for i in range(m):
            for j in range(n):
                A.append(nums[i][j])

        # Corner case
        if rows == 1:
            return [A]

        # Initialize the new array
        res = [[0 for j in range(cols)] for i in range(rows)]

        # queue -> new array
        for i in range(rows):
            for j in range(cols):
                res[i][j] = A.pop(0)

        return res


"""
Runtime: 300 ms, faster than 5.03% of Python3 online submissions for Reshape the Matrix.
Memory Usage: 15.1 MB, less than 5.55% of Python3 online submissions for Reshape the Matrix.
"""


"""
Time Complexity: O(n^2)
Space Complexity: O(n)
"""


# Approach 2: (Using division and modulus)

class Solution:
    def matrixReshape(self, nums: List[List[int]], rows: int, cols: int) -> List[List[int]]:
        m = len(nums)
        n = len(nums[0])

        # Corner case
        if (m == rows and n == cols) or (rows * cols > m * n):
            return nums

        # Initialize return array
        res = [[0 for j in range(cols)] for i in range(rows)]

        # Mapping (Old -> New)
        for i in range(m):
            for j in range(n):
                id_num = i * n + j
                res[id_num // cols][id_num % cols] = nums[i][j]

        return res


"""
Runtime: 96 ms, faster than 93.87% of Python3 online submissions for Reshape the Matrix.
Memory Usage: 14.9 MB, less than 5.55% of Python3 online submissions for Reshape the Matrix.
"""


"""
Time Complexity: O(n^2)
Space Complexity: O(1)
"""
