class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def how_long_to_eat(k):
            return sum(math.ceil(n / k) for n in piles)
        l = 1
        r = max(piles)
        while l < r:
            mid = (l + r) // 2
            if how_long_to_eat(mid) <= h:
                r = mid
            else:
                l = mid + 1
        return l
