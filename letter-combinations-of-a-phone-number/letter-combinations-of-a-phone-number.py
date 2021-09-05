class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        patterns = ['', '', 'abc', 'def', 'ghi',
                      'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        
        def dfs(i: int, path: str)->None:
            if i == len(digits):
                ans.append(''.join(path))
                return
            for letter in patterns[ord(digits[i]) - ord('0')]:
                dfs(i + 1, path + [letter])
                
        ans = []

        dfs(0, [])

        return ans        
        