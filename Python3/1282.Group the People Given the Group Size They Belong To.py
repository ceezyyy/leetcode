"""
@Title: 1282. Group the People Given the Group Size They Belong To
@Tag: greedy
@Date: Feb-16 2020
@Author: ceezyyy
@Difficulty: Medium
"""


class Solution:
    def groupThePeople(self, S: List[int]) -> List[List[int]]:
        n, res = len(S), []  # people
        G = [[] for i in range(n)]  # 1 <= groupSizes[i] <= n
        for i, s in enumerate(S):
            G[s-1].append(i)  # 1 <= groupSizes[i] <= n
        for i, g in enumerate(G):
            k = i + 1
            if len(g) > i + 1:  # separate
                # split into evenly sized group
                temp = [g[i:i+k] for i in range(0, len(g), k)]
                res.extend(temp)
            else:
                if g:  # not empty
                    res.append(g)
        return res


"""
Runtime: 76 ms, faster than 83.35% of Python3 online submissions for Group the People Given the Group Size They Belong To.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Group the People Given the Group Size They Belong To.
"""
