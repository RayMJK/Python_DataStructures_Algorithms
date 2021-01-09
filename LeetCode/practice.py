import heapq
def minMeetingRooms(intervals):
    if not intervals:
        return 0

    free_rooms = []
    intervals.sort(key = lambda x:x[0])
    print('intervals : ', intervals)

    heapq.heappush(free_rooms, intervals[0][1])
    print('free rooms : ', free_rooms)

    for i in intervals[1:]:
        if free_rooms[0] <= i[0]:
            heapq.heappop(free_rooms)

        heapq.heappush(free_rooms, i[1])
        print('free room : ', free_rooms)
    return len(free_rooms)


intervals = [[1,5],[8,9], [8,9]]

# [[13, 15], [1, 13]] => 1
# [[1,5],[8,9], [8,9]] => 2
# [[9,10],[4,9],[4,17]] => 2
print(minMeetingRooms(intervals))