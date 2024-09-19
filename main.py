
class Guest:
    def __init__(self, guest_id, name, email, phone, address):
        self._guest_id = guest_id
        self._name = name
        self._email = email
        self._phone = phone
        self._address = address
        self._reservation_list = []
    # Getter methods
    def get_guest_id(self):
        return self._guest_id
    def get_name(self):
        return self._name
    def get_email(self):
        return self._email
    def get_phone(self):
        return self._phone
    def get_address(self):
        return self._address
    # Setter methods
    def set_name(self, name):
        self._name = name
    def set_email(self, email):
        self._email = email
    def set_phone(self, phone):
        self._phone = phone
    def set_address(self, address):
        self._address = address
    def make_reservation(self, reservation):
        """Adds a reservation to the guest's reservation list"""
        self._reservation_list.append(reservation)
        print(f"Reservation made for {self._name}")
    def get_reservations(self):
        """Returns the list of reservations made by the guest"""
        return self._reservation_list
class Room:
    def __init__(self, room_id, room_type, status, price_per_night, description):
        self._room_id = room_id
        self._room_type = room_type
        self._status = status
        self._price_per_night = price_per_night
        self._description = description
    # Getter methods
    def get_room_id(self):
        return self._room_id
    def get_room_type(self):
        return self._room_type
    def get_status(self):
        return self._status
    def get_price_per_night(self):
        return self._price_per_night
    def get_description(self):
        return self._description
    # Setter methods
    def set_status(self, status):
        self._status = status
    def set_price_per_night(self, price):
        self._price_per_night = price
    def set_description(self, description):
        self._description = description
    def check_availability(self):
        """Returns True if the room is available"""
        return self._status == "Available"
    def update_status(self, status):
        """Updates the room's status (e.g., from 'Available' to 'Reserved')"""
        self._status = status
class Reservation:
    def __init__(self, reservation_id, guest, room, check_in_date, check_out_date, number_of_nights):
        self._reservation_id = reservation_id
        self._guest = guest
        self._room = room
        self._check_in_date = check_in_date
        self._check_out_date = check_out_date
        self._number_of_nights = number_of_nights
    # Getter methods
    def get_reservation_id(self):
        return self._reservation_id
    def get_guest(self):
        return self._guest
    def get_room(self):
        return self._room
    def get_check_in_date(self):
        return self._check_in_date
    def get_check_out_date(self):
        return self._check_out_date
    def get_number_of_nights(self):
        return self._number_of_nights
    # Setter methods
    def set_check_in_date(self, date):
        self._check_in_date = date
    def set_check_out_date(self, date):
        self._check_out_date = date
    def confirm_reservation(self):
        """Confirms reservation if the room is available"""
        if self._room.check_availability():
            self._room.update_status("Reserved")
            print(f"Reservation {self._reservation_id} confirmed for guest {self._guest.get_name()}")
        else:
            print(f"Room {self._room.get_room_id()} is not available.")
    def cancel_reservation(self):
        """Cancels the reservation and marks the room as available"""
        self._room.update_status("Available")
        print(f"Reservation {self._reservation_id} for guest {self._guest.get_name()} has been canceled.")
class Payment:
    def __init__(self, payment_id, amount, payment_date, payment_method, reservation):
        self._payment_id = payment_id
        self._amount = amount
        self._payment_date = payment_date
        self._payment_method = payment_method
        self._reservation = reservation
    # Getter methods
    def get_payment_id(self):
        return self._payment_id
    def get_amount(self):
        return self._amount
    def get_payment_date(self):
        return self._payment_date
    def get_payment_method(self):
        return self._payment_method
    def get_reservation(self):
        return self._reservation
    # Setter methods
    def set_amount(self, amount):
        self._amount = amount
    def set_payment_method(self, method):
        self._payment_method = method
    def process_payment(self):
        """Processes the payment for the reservation"""
        print(f"Processing payment of ${self._amount} for reservation {self._reservation.get_reservation_id()}...")
        print(f"Payment successful using {self._payment_method}.")
    def refund_payment(self):
        """Refunds the payment to the guest"""
        print(f"Refunding payment of ${self._amount} to {self._reservation.get_guest().get_name()}.")
# Create a guest object
guest = Guest(1, "Ted Vera", "tedvera@rmac.com", "+1234567890", "2455 Trinity Drive, Los Alamos, NM")
# Create a room object
room = Room(101, "2 Queen Beds, No Smoking", "Available", 89.85, "Room with 2 Queen Beds, Desk, Coffee Maker, Hair Dryer")
# Create a reservation object
reservation = Reservation(1, guest, room, "2024-08-22", "2024-08-24", 2)
# Create a payment object
payment = Payment(1, 201.48, "2024-08-21", "Mastercard (ending in 1904)", reservation)
# Make a reservation, confirm it, and process the payment
guest.make_reservation(reservation)
reservation.confirm_reservation()
payment.process_payment()
# Print the details of the reservation
def print_confirmation():
    print("Your Reservation is Confirmed")
    print("Thank you for your reservation. Please print your hotel receipt and show it at check-in.")
    print(f"\nYour Name: {guest.get_name()}")
    print(f"Your Email: {guest.get_email()}")
    print(f"Hotel Confirmation Number: {reservation.get_reservation_id()}")
    print(f"\nRoom Information:")
    print(f"Room: {room.get_room_id()}")
    print(f"Room Type: {room.get_room_type()}")
    print(f"Check-in: {reservation.get_check_in_date()}")
    print(f"Check-out: {reservation.get_check_out_date()}")
    print(f"Number of Nights: {reservation.get_number_of_nights()}")
    print("\nSummary of Charges:")
    print(f"Billing Name: {guest.get_name()}")
    print(f"Credit Card: {payment.get_payment_method()}")
    print(f"Room Cost: ${room.get_price_per_night():.2f} per night")
    print(f"Number of Nights: {reservation.get_number_of_nights()}")
    room_total = room.get_price_per_night() * reservation.get_number_of_nights()
    print(f"Room Subtotal: ${room_total:.2f}")
    taxes_fees = room_total * 0.12  # Assuming 12% tax
    print(f"Taxes and Fees: ${taxes_fees:.2f}")
    total = room_total + taxes_fees
    print(f"Total Charges: ${total:.2f}")
# Display the confirmation details
print_confirmation()
