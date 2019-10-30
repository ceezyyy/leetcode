"""
@Title: 1200. Minimum Absolute Difference
@Tag: list
@Date: Oct-23 2019
@Author: ceezyyy
@Difficulty: Easy
"""


from typing import List
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        res=[]
        arr=sorted(arr)
        temp=arr[1]-arr[0]
        for i in range(1,len(arr)-1):
            temp=min(arr[i+1]-arr[i],temp)
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i]==temp:
                res.append([arr[i],arr[i+1]])
        return res


def main():
    s=Solution()
    print(s.minimumAbsDifference([3,8,-10,23,19,-4,-14,27]))


if __name__ == "__main__":
    main()


"""
Runtime: 444 ms, faster than 30.95% of Python3 online submissions for Minimum Absolute Difference.
Memory Usage: 28 MB, less than 100.00% of Python3 online submissions for Minimum Absolute Difference.
"""