Q4 = """What is the maximum number of meetings that can be 
        accommodated in the meeting room when only one meeting can be 
        held in the meeting room at a particular time?"""

class Maxmeetings():

    #constructer to create meeting start,end and position pairs.

    def __init__(self, start, end, position):

        self.start=start
        self.end=end
        self.position=position

def maxMeetings(meetings,n):

    ans = []
    c = 1
    
    # Sorting of meetings in ascending order according to their finish time
    meetings.sort(key = lambda x: x.end)

    # First meeting is always selected
    ans.append(meetings[0].position)


    prev_end = meetings[0].end
    
    # Checking if meeting can take place or not
    for i in range(1, n):
        if meetings[i].start > prev_end:
            ans.append(meetings[i].position)
            prev_end = meetings[i].end
            c = c + 1
        # return c
    print("Maximum meetings that can take place are:",c)
    print("Selected meetings:")
    print("final selected meetings")

    for i in ans:
        print(i+1, end = " ")
        
	
if __name__ =="__main__":

    # Test code	
    # Start times
    s = [ 1, 2, 0, 6, 9, 10 ]
    # Finish times
    f = [ 3, 5, 7, 8, 11, 12 ]

    n = len(s)
    pair = []
    for i in range(n):
            # Creating pairs of meeting(start,end) and appending to a list
            pair.append(Maxmeetings(s[i], f[i], i))

    maxMeetings(pair, n)
 
