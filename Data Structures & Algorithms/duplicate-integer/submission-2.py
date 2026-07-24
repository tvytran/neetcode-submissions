class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        stash = set()
        for r in nums:
            if r in stash:
                return True
            else:
                stash.add(r)
        return False

        