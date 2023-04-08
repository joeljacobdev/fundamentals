from typing import List

class Search:
    @classmethod
    def binary_search(cls, nums: List[int], target: int) -> int:
        """
        :return index of element
        """
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return -1

    @classmethod
    def binary_search_equal_or_next(cls, nums: List[int], target: int) -> int:
        """
        It will return the next value in case equal value is not present.
        :return index of element
        """
        start, end = 0, len(nums) - 1
        while start < end:
            mid = start + (end - start) // 2
            if target > nums[mid]:
                start = mid + 1
            else:
                end = mid
        return end

    @classmethod
    def binary_search_equal_or_smaller(cls, nums: List[int], target: int) -> int:
        """
        It will return the smaller value in case equal value is not present.
        :return index of element
        """
        # We need to choose a mid - which is right most and shrink to left to avoid infinite loop
        start, end = 0, len(nums) - 1
        while start < end:
            # in case of even elements - choose the right most
            mid = start + (end - start + 1) // 2
            if target < nums[mid]:
                # we need to shrink to left - to get smaller value in case of no exact value.
                end = mid - 1
            else:
                start = mid
        # in case the value is less than 0th index - we return -1.
        # above section of algo copies bisect_left - which find the left index to insert the value
        # in case no exact match of value is found
        if start == 0 and nums[start] > target:
            return -1
        return start

    @classmethod
    def linear_search(cls, nums: List[int], target: int) -> int:
        for idx, num in enumerate(nums):
            if target == num:
                return idx
        return -1

    @classmethod
    def search_in_rotated_array(cls, nums: List[int], target: int) -> int:
        """
        Pivot is not known
        :param nums: ordered iterable of elements
        :param target: element to find
        :return: idx of element
        """
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if target == nums[mid]:
                return mid
            elif nums[start] > nums[mid] and not (nums[mid] < target and target <= nums[end]):
                end = mid - 1
            elif nums[mid] > nums[end] and not (target < nums[mid] and nums[start] <= target):

                start = mid + 1
            elif target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return -1
