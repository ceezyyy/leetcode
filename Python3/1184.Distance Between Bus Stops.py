"""
@Title: 1184. Distance Between Bus Stops
@Tag: array
@Date: Jan-24 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        start, destination = min(start, destination), max(
            start, destination)  # redefine
        distance *= 2  # cycle
        return min(sum(distance[start: destination]), sum(distance[destination: start + len(distance) // 2]))


"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
