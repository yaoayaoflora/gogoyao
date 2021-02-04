# Given a list of non-overlapping intervals sorted by their start time, insert a given interval 
# at the correct position and merge all necessary intervals to produce a list that 
# has only mutually exclusive intervals.


def insert(intervals, new_interval):
    mergedIntervals = []
    i, start, end = 0, 0, 1

    # skip and add to the output all intervals that come before the 'new_interval'
    while i < len(intervals) and intervals[i][end] < new_interval[start]:
        mergedIntervals.append(intervals[i])
        i += 1

    # merge all intervals that overlap with 'new_interva'
    while i < len(intervals) and intervals[i][start] <= new_interval[end]:
        new_interval[start] = min(intervals[i][start], new_interval[start])
        new_interval[end] = max(intervals[i][end], new_interval[end])
        i += 1

    # insert the new_interval
    mergedIntervals.append(new_interval)

    # add all the remaining intervals to the output
    while i < len(intervals):
        mergedIntervals.append(intervals[i])
        i += 1

    return mergedIntervals


def main():
    print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
    print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
    print("Intervals after inserting the new interval: " + str(insert([[2, 3], [5, 7]], [1, 4])))


main()
