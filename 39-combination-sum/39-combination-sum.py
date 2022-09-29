class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        vals = []
        
        # Recrusive decision tree, each time we call the function, we either
        # search all comibnations including or excluding the element at index i in the array
        def dfs(index, curr, total):
            if target == total:
                vals.append(curr.copy())
                return
            
            if total > target or index >= len(candidates):
                return
            
            curr.append(candidates[index])
            
            dfs(index, curr, total + candidates[index])
            
            curr.pop()
            
            dfs(index + 1, curr, total)
            
            
        
        dfs(0, [], 0)
        
        return vals
        
        