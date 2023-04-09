class Sorting:

    @classmethod
    def merge_sort(cls, array, lo=None, hi=None):
        if lo is None:
            lo = 0
        if hi is None:
            hi = len(array) - 1
        if lo == hi:
            return [array[lo]]
        mid = lo + (hi - lo) // 2
        left_arr = cls.merge_sort(array, lo, mid)
        # we will use mid + 1 to avoid going to infinite loop due to hi becoming negative
        right_arr = cls.merge_sort(array, mid + 1, hi)
        return cls._merge_two_sorted_array(left_arr, right_arr)

    @classmethod
    def _merge_two_sorted_array(cls, array1, array2):
        ans = []
        i = j = 0
        while i < len(array1) or j < len(array2):
            if i == len(array1):
                ans.append(array2[j])
                j += 1
            elif j == len(array2):
                ans.append(array1[i])
                i += 1
            else:
                if array1[i] < array2[j]:
                    ans.append(array1[i])
                    i += 1
                else:
                    ans.append(array2[j])
                    j += 1
        return ans


arr = [4, 6, 7, 2, 7, 1, 88, 21, 56, 12]
Sorting.merge_sort(arr)
