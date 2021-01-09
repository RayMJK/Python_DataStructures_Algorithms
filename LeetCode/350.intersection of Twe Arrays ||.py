class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []

        for i in nums1:
            if nums2:
                for j in nums2:
                    if i == j:
                        answer.append(j)
                        nums2.remove(j)
                        break

        return answer
