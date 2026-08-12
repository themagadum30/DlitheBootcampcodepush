class Solution(object):
    def trap(self, height):
        st = 0
        end = len(height) - 1
        left_max = 0
        right_max = 0
        water = 0
        while st <end:
            if height[st] < height[end]:
                if height[st] >= left_max:
                    left_max = height[st]
                else:
                    water += left_max - height[st]
                st += 1
            else:
                if height[end] >= right_max:
                    right_max = height[end]
                else:
                    water += right_max - height[end]
                end -= 1
        return water