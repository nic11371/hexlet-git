from datetime import date


class Booking:
    def __init__(self):
        self.mem = set()

    def book(self, start, stop):
        
        start_d = start.split('-')
        stop_d = stop.split('-')
        start_j = ''.join(start_d)
        stop_j = ''.join(stop_d)
        start_b = date(start_j)
        stop_b = date(stop_j)
        # book_d = stop_d - start_d
        if start_b not in range(start_b, stop_b) and stop_d not in range(start_b, stop_b):
            self.mem.add(start_b)
            self.mem.add(stop_b)
            print(self.mem)
            return True
        return False
        


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
