"""
@Title: 929. Unique Email Addresses
@Tag: string
@Date: Jan-30 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = []
        for email in emails:  # each email
            local, domain = email.split("@")[0], email.split("@")[1]
            local = local.replace(".", "")  # rule one
            if "+" in local:
                local = local[:local.index('+')]  # rule two
            res.append(local + "@" + domain)
        return len(set(res))


"""
Runtime: 44 ms, faster than 92.49% of Python3 online submissions for Unique Email Addresses.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Unique Email Addresses.
"""
