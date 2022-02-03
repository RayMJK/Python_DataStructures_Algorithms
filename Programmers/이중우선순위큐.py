import heapq
def solution(operations):
    answer = []
    print(operations)
    heap = []
    maxheap = []
    for i in operations:
        if i[0] == "I":
            heapq.heappush(heap, int(i[2:]))
            heapq.heappush(maxheap, (-int(i[2:]), int(i[2:])))
        else:
            if len(heap) == 0:
                pass
            elif i == "D 1":
                max = heapq.heappop(maxheap)[1]
                heap.remove(max)
            else:
                min = heapq.heappop(heap)
                maxheap.remove((-min, min))
    if heap:
        return [heapq.heappop(maxheap)[1], heapq.heappop(heap)]

    else:
        return [0, 0]