"""
@Title: 1232. Check If It Is a Straight Line
@Tag: math
@Date: Nov-04 2019
@Author: ceezyyy
@Difficulty: Easy
"""

from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        slope = []
        for i in range(len(coordinates)-1):
            # if denominator == 0 -> ZeroDivisionError
            if coordinates[i+1][0]-coordinates[i][0] == 0:
                return False
            slope.append(
                (coordinates[i+1][1]-coordinates[i][1])/(coordinates[i+1][0]-coordinates[i][0]))
        return slope[1:] == slope[:-1]  # all equal


def test():
    s = Solution()
    print(s.checkStraightLine(
        [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))
    print(s.checkStraightLine(
        [[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]))


if __name__ == "__main__":
    test()
