from django.db import models
from account.models import BaseModel, Account

class Train(BaseModel):
    """Model representing a train"""
    source = models.CharField(max_length=100)  # Source station
    destination = models.CharField(max_length=100)  # Destination station
    train_number = models.CharField(max_length=100)  # Train number
    train_name = models.CharField(max_length=100)  # Train name
    total_seats = models.IntegerField()  # Total number of seats in the train
    price = models.FloatField()  # Price per seat

    def __str__(self):
        return self.train_name  # String representation of the train

class TrainSchedule(BaseModel):
    """Model representing a train schedule"""
    train = models.ForeignKey(Train, on_delete=models.CASCADE)  # Link to the Train model
    journey_date = models.DateField()  # Date of the journey
    departure_time = models.TimeField()  # Departure time
    arrival_time = models.TimeField()  # Arrival time

    journey_end_date = models.DateField()  # End date of the journey
    journey_end_time = models.TimeField()  # End time of the journey

    available_seats = models.IntegerField()  # Number of available seats

    def __str__(self):
        return self.train.train_name  # String representation of the train schedule

class Booking(BaseModel):
    """Model representing a booking"""
    user = models.ForeignKey(Account, on_delete=models.CASCADE)  # Link to the Account model
    train = models.ForeignKey(Train, on_delete=models.CASCADE)  # Link to the Train model
    number_of_seats = models.IntegerField()  # Number of seats booked
    total_price = models.FloatField()  # Total price of the booking
    booking_date = models.DateTimeField(auto_now_add=True)  # Date and time of booking
    booking_status = models.BooleanField(default=False)  # Status of the booking
    schedule = models.ForeignKey(TrainSchedule, on_delete=models.CASCADE)  # Link to the TrainSchedule model
    payment_status = models.BooleanField(default=False)  # Payment status

    def __str__(self):
        return self.user.email  # String representation of the booking

class Seat(BaseModel):
    """Model representing a seat in a train"""
    train = models.ForeignKey(Train, on_delete=models.CASCADE)  # Link to the Train model
    seat_number = models.IntegerField()  # Seat number
    status = models.BooleanField(default=False)  # Status of the seat (booked or not)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, null=True, blank=True)  # Link to the Booking model
    journey_date = models.DateField()  # Date of the journey

    def __str__(self):
        return f"{self.train.train_name} {self.seat_number} {self.booking.user.email if self.booking else 'No Booking'} {self.journey_date}"  # String representation of the seat
