# 8. You are going to model a theater ticketing system. For simplicity imagine all the seats are in a single row.
# t = Theater(50) # Create a Theater which has total no.of seats

# available_total()
# - Returns the available no.of seats which are not booked

# available_seats()
# - Returns all the available seats. Consider the seats are named  "Seat-1" to "Seat-n"
# where n is the total number of seats. 50 in this case.

# book(seats, name)
# - Book the given seats under a name.

# t.available_total() # returns 50 since everything is available
# t.available_seats() # return a list ["seat-1", "seat-2",...."seat-50"]
# t.book(["seat-10", "seat-11"], "vishnu") # book 2 seats for vishnu. Error if those seats are not available.
# t.available_total()  # returns 48
# t.book(["seat-10", "seat-11"], "swetha") # error since they are already booked
# t.book(["seat-1", "seat-2"], "swetha")
# t.available_total()  # returns 46
# t.available_seats() # ["seat-3", "seat-4"..."seat-50"] i.e except 1,2, 10, 11 since they are already booked

# random_book(num_seats, name)
# - Customer does not care of specific seats they just want to book some number of seats.
# So find any available seats and book it. Error if num_seats are less than available.
# t.random_book(10, "karthik") # returns the booked seats ["seat-3", "seat-4"...] 10 seats except  1,2, 10, 11
# t.available_total()  # 36
# If you want to be adventurous, try to book seats together(single contiguous group) instead of randomly choosing.
# If there is no other option, then you can split it into multiple groups.

class Theater:
    def __init__(self, capacity):
        self.cap = capacity
        self.seats = []
        self.cus_data = {}
        n = 1
        while n <= self.cap:
            self.seats.append(n)
            n = n + 1

    def available_total(self):
        return self.cap

    def available_seats(self):
        return self.seats

    def customer(self):
        return self.cus_data

    def book(self, seats, customer):
        yes = []
        no = []

        for seat in seats:
            if seat in self.seats:
                yes.append(seat)
            else:
                no.append(seat)

        if len(no) == 0:
            for seat in seats:
                self.seats.remove(seat)  # self.seats.remove(seats[0:len(seats)])
            self.cap = self.cap - len(seats)
            self.cus_data[tuple(seats)] = customer
        else:
            if len(no) == 1:
                print("Error - Seat", tuple(no), "not available.")
            else:
                print("Error - Seats", tuple(no), "not available.")

    def random_book(self, num_seats, name):
        if num_seats <= self.cap:
            t = 1
            seat_cus = []

            while t <= num_seats:
                seat_cus.append(self.seats[0])
                self.seats.remove(self.seats[0])
                t = t + 1
            self.cap = self.cap - num_seats
            self.cus_data[tuple(seat_cus)] = name

            # continuous=self.seats[0]+1
            # m=2
            # while continuous in self.seats:
            # if m<=num_seats:
            # continuous=continuous+1
            # call a function - use break


t = Theater(50)
print(t.available_total())
print(t.available_seats())
t.book([10, 11], "vishnu")
print(t.available_total())
print(t.available_seats())
t.book([10, 11], "swetha")
t.book([1, 2], "swetha")
print(t.available_total())
print(t.available_seats())
t.book([2, 3], "nivetha")
print(t.available_total())
print(t.available_seats())
print(t.customer())
t.random_book(10, "karthik")
print(t.available_total())
print(t.available_seats())
print(t.customer())
