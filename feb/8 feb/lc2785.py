class Solution:
    def sortVowels(self, s: str) -> str:
        x = []
        for i in s:
            if i in 'aeiou':
                x.append(i)
        x.sort()
        ans = []
        j = 0
        for i in s:
            if i in 'aeiou':
                ans.append(x[j])
                j += 1
            else:
                ans.append(i)
        return ''.join(ans)