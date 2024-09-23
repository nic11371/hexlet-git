from datetime import date


class Booking:
    def __init__(self):
        self.mem = []

    def book(self, start, stop):
        start_b = date.fromisoformat(start)
        stop_b = date.fromisoformat(stop)
        
        range_book = (start_b, stop_b)

        if start_b == stop_b or start_b > stop_b:
            return False

        if not self.mem:
            self.mem.append(range_book)
            return True
        
        for elem in self.mem:
            if elem[0] < start_b < elem[1]:
                return False
            elif elem[0] < stop_b < elem[1]:
                return False
            else:
                return True


booking = Booking()
print(booking.book('2008-11-11', '2008-11-13'))  # True
print(booking.book('2008-11-12', '2008-11-12'))  # False
print(booking.book('2008-11-10', '2008-11-12'))  # False
print(booking.book('2008-11-12', '2008-11-14'))  # False
print(booking.book('2008-11-10', '2008-11-11'))  # True
print(booking.book('2008-11-13', '2008-11-14'))  # True


# def test_booking():
#     booking = Booking()

#     assert not booking.book('2008-11-10', '2008-11-05')
#     assert booking.book('2008-11-11', '2008-11-13')
#     assert not booking.book('2008-11-12', '2008-11-12')
#     assert not booking.book('2008-11-12', '2008-11-14')
#     assert booking.book('2008-11-10', '2008-11-11')
#     assert not booking.book('2008-11-12', '2008-11-13')
#     assert not booking.book('2008-11-13', '2008-11-13')
#     assert booking.book('2008-11-13', '2008-11-14')
#     assert booking.book('2008-05-08', '2008-05-18')
#     assert not booking.book('2008-05-09', '2008-05-10')


# test_booking()
