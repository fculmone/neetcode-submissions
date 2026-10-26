class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        say we get count of each num? then what? We can't sort or we get O(nlogn)
        we can't maintain a heap cause inserts take O(logn) and we'd have to do n inserts worst case???
        actually no because we only have ~2000 possible values, so we could shove those either in a heap?
        bucket sort is O(n) and we know the value constraints on the numbers. still though don't see how this would get us the most frequent
        we actually could just sort or use quick select on the final sorted counts since technically it's fixed size and O(1)
        """
        frequencies = [0] * 2001 # 2001 is the amount of numbers between -1000 and 1000 inclusive, since nums[i] is in that range
        for n in nums:
            frequencies[n + 1000] += 1
        
        nums_with_count = [{'number': x - 1000, 'count': n} for x, n in enumerate(frequencies)]
        nums_with_count.sort(key=lambda x: x['count'], reverse=True)
        return [x['number'] for x in nums_with_count[:k]]
         