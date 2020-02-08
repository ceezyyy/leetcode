"""
@Title: 1222. Queens That Can Attack the King
@Tag: array
@Date: Feb-08 2020
@Author: ceezyyy
@Difficulty: Medium
"""


class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        res, x, y = [], king[0], king[1]
        for x1 in range(x, -1, -1):  # left
            if [x1, y] in queens:
                res.append([x1, y])
                break
        for x1 in range(x, 8):  # right
            if [x1, y] in queens:
                res.append([x1, y])
                break
        for y1 in range(y, -1, -1):  # up
            if [x, y1] in queens:
                res.append([x, y1])
                break
        for y1 in range(y, 8):  # down
            if [x, y1] in queens:
                res.append([x, y1])
                break
        x1, y1 = x, y
        while x1 < 8 and y1 < 8:  # top-right
            if [x1, y1] in queens:
                res.append([x1, y1])
                break
            x1 += 1
            y1 -= 1
        x1, y1 = x, y
        while x1 > -1 and y1 < 8:  # bottom-left
            if [x1, y1] in queens:
                res.append([x1, y1])
                break
            x1 -= 1
            y1 += 1
        x1, y1 = x, y
        while x1 < 8 and y1 < 8:  # bottom-right
            if [x1, y1] in queens:
                res.append([x1, y1])
                break
            x1 += 1
            y1 += 1
        x1, y1 = x, y
        while x1 > -1 and y1 > -1:  # top-left
            if [x1, y1] in queens:
                res.append([x1, y1])
                break
            x1 -= 1
            y1 -= 1
        return res


"""
Runtime: 40 ms, faster than 55.42% of Python3 online submissions for Queens That Can Attack the King.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Queens That Can Attack the King.
"""
