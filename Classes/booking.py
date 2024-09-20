import datetime


class Booking:
    def __init__(self):
        self.mem = []

    def book(self, start, stop):
        start_b = datetime.datetime.strptime(start, "%Y-%m-%d")
        stop_b = datetime.datetime.strptime(stop, "%Y-%m-%d")

        range = self.generate(start_b, stop_b)
        first = range[0]
        last = len(range) - 1
        
        if not self.mem:
            self.mem.append(range)
            return True
        
        diff = list(set(range) & set(self.mem[0]))
        
        for book in self.mem:
            last_date = len(book) - 1
            if book[1:last_date] in range[1:last]:
                return False
            return True


    def generate(self, start, stop):
        days = stop - start
        date_generated = [start + datetime.timedelta(days=x) for x in range(0, (stop-start).days + 1)]
        return date_generated


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
