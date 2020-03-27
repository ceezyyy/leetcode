"""
@Title: 1051. Height Checker
@Tag: list
@Date: Oct-22 2019
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    # def heightChecker(self, heights: List[int]) -> int:
    def heightChecker(self, heights) -> int:
        res=0
        new_heights=sorted(heights)  
        # The sorted() function returns a sorted list of the specified iterable object.
        for i,j in zip(heights,new_heights):
            if i!=j:
                res=res+1
        return res


def main():
    s=Solution()
    print(s.heightChecker([1,1,4,2,1,3]))


if __name__ == "__main__":
    main()


"""
Runtime: 44 ms, faster than 58.44% of Python3 online submissions for Height Checker.
Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Height Checker.
"""