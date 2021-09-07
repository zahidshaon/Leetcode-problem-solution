class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        def dfs(s: int, target: int, path: List[int]) -> None:
            if target < 0:
                return
            if target == 0:
                answer.append(path)
                return
            for i in range(s, len(candidates)):
                if i > s and candidates[i] == candidates[i - 1]:
                    continue
                dfs(i + 1, target - candidates[i], path + [candidates[i]])

        candidates.sort()
        dfs(0, target, [])

        return answer
        