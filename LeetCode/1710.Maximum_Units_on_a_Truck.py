class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        boxTypes.sort(key=lambda x: -x[1])

        n = 0
        answer = 0
        i = 0
        while i < len(boxTypes):
            if boxTypes[i][0] <= truckSize:
                answer += boxTypes[i][0] * boxTypes[i][1]
                truckSize -= boxTypes[i][0]
                i += 1
            else:
                boxTypes[i][0] = truckSize
                answer += boxTypes[i][0] * boxTypes[i][1]
                break
        return answer


