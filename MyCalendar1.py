from typing import List

class MyCalendar:

    def __init__(self):
        self.bookings = []

    def book1(self, start: int, end: int) -> bool: # Original implementation where the insertions remain in order(abandoned cause it got so confusing :0)
        # Case for bookings is empty
        if self.bookings.length() == 0:
            self.bookings.append([start, end])

        # check if current booking is before the 1st booking
        if start < self.bookings[0][0]:
            if end < self.bookings[0][1]:
                self.bookings.insert(0, [start, end])
                return True
            return False

        # check if current booking is a middle booking
        for i in range(0, self.bookings.length() - 1):
            if start > self.bookings[i][1]:
                if start < self.bookings[i + 1][0]:
                    if end <self.bookings[i + 1][1]:
                        self.bookings.insert(i + 1, [start, end])
                        return True
                    return False
                

        # check if current booking is after last booking
            
        # return false

    def book2(self, start: int, end:int) -> bool: # reworked brute force strategy because its simpler to understand
        for booking in self.bookings:
            if start < booking[1] and end > booking[0]:
                return False
        self.bookings.append((start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)