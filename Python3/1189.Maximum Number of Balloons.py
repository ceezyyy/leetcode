"""
@Title: 1189. Maximum Number of Balloons
@Tag: dict
@Date: Oct-22 2019
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        aim='balon'
        # dict.fromkeys() is a classmethod as well as the initialization of dict
        # d={'b','a','l','o','n'}
        d=dict.fromkeys(aim,0) 
        for i in text:
            if i in d:
                d[i]=d[i]+1
        d['l']=int(d['l']/2)  # 'l' appears twice
        d['o']=int(d['o']/2)  # 'o' appears twice
        return min(d.values())


def main():
    s=Solution()
    print(s.maxNumberOfBalloons("loonbalxballpoon"))


if __name__ == "__main__":
    main()
