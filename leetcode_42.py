# class Solution:
#     def trap(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#
#         def calculate_area(l, r):
#             area, min_height = 0, min(height[l], height[r])
#             for hei in height[l + 1:r]:
#                 area = area - hei + min_height
#             return area
#
#         left, right, area = 0, 0, 0
#         length = 0
#         for i, pillar in enumerate(height):
#             if not pillar:
#                 if not left:
#                     continue
#                 else:
#                     length = length + 1
#             elif not left:
#                 left = pillar
#             elif not right:
#                 right = pillar
#             elif pillar > right:
#                 right = pillar
#                 length = length + 1
#             else:
#                 area = area + calculate_area(i - length - 2, i - 1)  # 计算当前块面积
#                 if pillar < right:
#                     left, right, length = right, 0, 1
#                 else:
#                     left, right, length = pillar, 0, 0
#         else:
#             if right:
#                 area = area + calculate_area(i-length-1,i)
#         return area


class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        l_max, r_max, area = 0, 0, 0
        l_index, r_index = 0, len(height) - 1
        while l_index < r_index:
            l_max = max(l_max, height[l_index])
            r_max = max(r_max, height[r_index])
            if l_max < r_max:
                area = area + l_max - height[l_index]
                l_index +=1
            else:
                area = area + r_max - height[r_index]
                r_index -= 1
        return area

s = Solution()
print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
