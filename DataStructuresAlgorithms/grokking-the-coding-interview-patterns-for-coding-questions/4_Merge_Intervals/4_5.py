# Given a list of intervals representing the start and end time of ‘N’ meetings, find the minimum
# number of rooms required to hold all the meetings.


from heapq import *


class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        # minHeap based on meeting.end
        return self.end < other.end


def min_meeting_rooms(meetings):
    # sort the meeting by start time
    meetings.sort(key=lambda x: x.start)

    minRooms = 0
    minHeap = []
    for m in meetings:
        # remove all the meetings that have ended before m.start
        while len(minHeap) > 0 and m.start >= minHeap[0].end:
            heappop(minHeap)
        # add the current meeting into minHeap
        heappush(minHeap, m)
        # all the meetings are in the minHeap, so we need rooms for all of them
        minRooms = max(minRooms, len(minHeap))
    
    return minRooms


def main():
    print("Minimum meeting rooms required: " + str(min_meeting_rooms(
        [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])))
    print("Minimum meeting rooms required: " +
          str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 5), Meeting(7, 9)])))
    print("Minimum meeting rooms required: " +
          str(min_meeting_rooms([Meeting(6, 7), Meeting(2, 4), Meeting(8, 12)])))
    print("Minimum meeting rooms required: " +
          str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 3), Meeting(3, 6)])))
    print("Minimum meeting rooms required: " + str(min_meeting_rooms(
        [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])))


main()