"""
1108. Defanging an IP Address
Date: Oct-22 2019
Author: ceezyyy
"""


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.','[.]')


def main():
    s=Solution()
    print(s.defangIPaddr("1.1.1.1"))


if __name__=="__main__":
    main()

