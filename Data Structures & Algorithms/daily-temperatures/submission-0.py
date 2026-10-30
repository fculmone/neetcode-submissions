class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # if you see a decrease or the number is greater than the number 
        # that we see previously
        result = [0] * len(temperatures)
        stack = [] # going to keep (temp, index)
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                temp, index = stack.pop() 
                result[index] = i - index
            stack.append((t, i))
        return result

        