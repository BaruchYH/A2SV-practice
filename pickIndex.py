class Solution:
    def __init__(self, w: List[int]):
        self.prefix = [0]
        for x in w: self.prefix.append(self.prefix[-1] + x)

    def pickIndex(self) -> int:
        r = randint(1, self.prefix[-1])
        return bisect_left(self.prefix, r)-1


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
