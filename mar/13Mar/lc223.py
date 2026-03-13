class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        a1 = (ax2-ax1) * (ay2-ay1)
        a2 = (bx2-bx1) * (by2-by1)
        inter_width = min(ax2, bx2) - max(ax1, bx1)
        inter_height = min(ay2, by2) - max(ay1, by1)
        if inter_width > 0 and inter_height > 0:
            intersection = inter_width * inter_height
            return a1 + a2 - intersection
        return a1 + a2