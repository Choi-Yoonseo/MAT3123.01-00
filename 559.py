class Solution:
    def maxDepth(self, r) -> int:
        return 1 +max((self.maxDepth(c) for c in r.children),default=0) if r else 0