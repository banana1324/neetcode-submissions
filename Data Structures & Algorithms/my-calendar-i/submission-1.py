class MyCalendar:
    
    def __init__(self):
        self.events = []

    def book(self, startTime: int, endTime: int) -> bool:
        for event in self.events:
            if event[0] <= startTime and event[1] > startTime:
                return False
            if event[0] < endTime and event[1] >= endTime:
                return False
            if event[0] >= startTime and event[1] <= endTime:
                return False
        self.events.append([startTime, endTime])
        return True
    


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)