"""
Your company built an in-house calendar tool called HiCal. 
You want to add a feature to see the times in a day when everyone is available. 

In HiCal, a meeting is stored as a tuple ↴ of integers (start_time, end_time). 
These integers represent the number of 30-minute blocks past 9:00am. 

Be sure to consider these edge cases:

    The end time of the first meeting and the start time of the second meeting are equal. 
    For example: [(1, 2), (2, 3)]
    The second meeting ends before the first meeting ends. For example: [(1, 5), (2, 3)]

 Here's a formal algorithm:

    1) We treat the meeting with earlier start time as "first," and the other as "second."
    2) If the end time of the first meeting is equal to or greater than the start time of the second meeting, 
        we merge the two meetings into one time range. 
        The resulting time range's start time is the first meeting's start, 
        and its end time is the later of the two meetings' end times.
    3) Else, we leave them separate.

"""
meetings = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]

# sort array by start time
sorted_meetings = sorted(meetings)
print(sorted_meetings)  # [(0, 1), (3, 5), (4, 8), (9, 10), (10, 12)]


# initialize merged_meetings with the earliest meeting
merged_meetings = [sorted_meetings[0]]
print(f"Earliest meeting: {merged_meetings}")   # [(0, 1)]


# start_time, end_time = sorted_meetings[0]
for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
    # print(current_meeting_start, current_meeting_end)  # 3, 5 | 4, 8 | 9, 10 | 10, 12
    last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]    # 0, 1

    # last_meeting vs current_meeting
    # (0, 1) vs (3, 5)... Thus, append to the current merged_meetings list
    # (3, 5) vs (4, 8)... update [-1] value
    # (9, 10) vs (10, 12)
    # # if the current meeting overlaps with last merged meeting, 
    # # use the later end time of the two
    if current_meeting_start <= last_merged_meeting_end:
        merged_meetings[-1] = (last_merged_meeting_start, 
                               max(current_meeting_end, last_merged_meeting_end))
        print(f"Overlapping meetings: {merged_meetings}")  # [(0, 1), (3, 8)] | [(0, 1), (3, 8), (9, 10)] | [(0, 1), (3, 8), (9, 12)]

    else:
        # add the current meeting since it doesn't overlap
        merged_meetings.append((current_meeting_start, current_meeting_end))
        print(f"Non-overlapping meetings: {merged_meetings}")  # [(0, 1), (3, 5)] | [(0, 1), (3, 5), (4, 8)] | [(0, 1), (3, 5), (4, 8), (9, 10)] | [(0, 1), (3, 5), (4, 8), (9, 10), (10, 12)]

print(f"Final merged meetings: {merged_meetings}")

# Sample Output:
# [(0, 1), (3, 5), (4, 8), (9, 10), (10, 12)]
# Earliest meeting: [(0, 1)]
# Non-overlapping meetings: [(0, 1), (3, 5)]
# Overlapping meetings: [(0, 1), (3, 8)]
# Non-overlapping meetings: [(0, 1), (3, 8), (9, 10)]
# Overlapping meetings: [(0, 1), (3, 8), (9, 12)]
# Final merged meetings: [(0, 1), (3, 8), (9, 12)]

### define above into a function

def merged_meetings(meetings):
    # sort array by start time
    sorted_meetings = sorted(meetings)

    # initialize merged_meetings with the earliest meeting
    merged_meetings = [sorted_meetings[0]]

    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

        # perform check if current meeting start less than last_merged_meeting_end
        # if true add that as the last element
        if (current_meeting_start <= last_merged_meeting_end):
            # (3, 5) vs (4, 8)... update [-1] value
            merged_meetings[-1] = (last_merged_meeting_start, 
                                   max(last_merged_meeting_end, current_meeting_end))
            
        else:
            merged_meetings.append((current_meeting_start, current_meeting_end))

    return merged_meetings

print(f"Merged meetings final function: {merged_meetings(meetings=meetings)}")
