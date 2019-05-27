class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        nums = len(height)

        index_move, index_stay, add_num = 0, nums - 1, 1

        if height[0] > height[nums - 1]:
            index_move, index_stay = nums - 1, 0
            add_num = -1
        area, area_now = height[index_move] * (nums - 1), 0

        while abs(index_stay - index_move) > 1:
            i = index_move + add_num
            while True:
                if height[i] <= height[index_move]:
                    pass
                elif height[i] > height[index_stay]:
                    area_now = height[index_stay] * abs(index_stay - i)
                    index_stay, index_move = i, index_stay
                    add_num = -add_num
                    area = area_now if area_now > area else area
                    break
                else:
                    area_now = height[i] * abs(index_stay - i)
                    if area_now > area:
                        index_move = i
                        area = area_now
                        break
                i += add_num
                if i == index_stay:
                    return area 
        return area
