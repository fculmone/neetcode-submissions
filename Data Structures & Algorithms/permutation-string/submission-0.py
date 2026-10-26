class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def isArrEqual(a1, a2):
            for i in range(len(a1)):
                if a1[i] != a2[i]:
                    return False
            return True

        if len(s1) > len(s2):
            return False
        s1_count = [0] * 26
        sub_count = [0] * 26
        for c in s1:
            s1_count[ord(c) - ord('a')] += 1
        for i in range(len(s1)):
            sub_count[ord(s2[i]) - ord('a')] += 1
        if isArrEqual(s1_count, sub_count):
            return True
        l = 0
        for r in range(len(s1), len(s2)):
            sub_count[ord(s2[l]) - ord('a')] -= 1
            sub_count[ord(s2[r]) - ord('a')] += 1
            l += 1
            if isArrEqual(s1_count, sub_count):
                return True
        return False
        