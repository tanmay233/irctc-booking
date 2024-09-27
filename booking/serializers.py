from rest_framework import serializers

# Serializer to handle seat booking requests
class BookSeatSerializer(serializers.Serializer):
    train_number = serializers.IntegerField()  # The train number for the booking
    schedule_id = serializers.IntegerField()  # The schedule ID for the selected train
    number_of_seats = serializers.IntegerField()  # The number of seats to be booked

# Serializer to handle the response after booking a seat
class BookingResponseSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()  # Unique identifier for the booking
    number_of_seats = serializers.IntegerField()  # Number of seats booked
    total_price = serializers.FloatField()  # Total price for the booking
    booking_date = serializers.DateTimeField()  # Date and time the booking was made
    booking_status = serializers.BooleanField()  # Status of the booking (True/False)
    schedule_id = serializers.IntegerField()  # ID of the train schedule
    payment_status = serializers.BooleanField()  # Payment status (True/False)

# Serializer for adding train information
class TrainSerializer(serializers.Serializer):
    source = serializers.CharField(max_length=100)  # Train source station
    destination = serializers.CharField(max_length=100)  # Train destination station
    train_number = serializers.CharField(max_length=100)  # Unique train number
    train_name = serializers.CharField(max_length=100)  # Train name
    total_seats = serializers.IntegerField()  # Total seats available on the train
    price = serializers.FloatField()  # Price per seat on the train

# Serializer for displaying train schedule information
class TrainScheduleSerializer(serializers.Serializer):
    train = TrainSerializer()  # Nested serializer to display train details
    journey_date = serializers.DateField()  # Date of the journey
    departure_time = serializers.TimeField()  # Train departure time
    arrival_time = serializers.TimeField()  # Train arrival time
    journey_end_date = serializers.DateField()  # Date of journey completion
    journey_end_time = serializers.TimeField()  # Time of journey completion
    available_seats = serializers.IntegerField()  # Number of seats still available

# Serializer for adding a new train schedule
class AddTrainScheduleSerializer(serializers.Serializer):
    train_number = serializers.IntegerField()  # Train number for the new schedule
    journey_date = serializers.DateField()  # Date of the journey
    departure_time = serializers.TimeField()  # Departure time for the journey
    arrival_time = serializers.TimeField()  # Arrival time at the destination
    journey_end_date = serializers.DateField()  # End date of the journey
    journey_end_time = serializers.TimeField()  # End time of the journey
    available_seats = serializers.IntegerField()  # Total number of available seats

# Serializer for updating an existing train schedule, all fields are optional
class UpdateTrainScheduleSerializer(serializers.Serializer):
    journey_date = serializers.DateField(required=False)  # Optional: new journey date
    departure_time = serializers.TimeField(required=False)  # Optional: new departure time
    arrival_time = serializers.TimeField(required=False)  # Optional: new arrival time
    journey_end_date = serializers.DateField(required=False)  # Optional: new end date
    journey_end_time = serializers.TimeField(required=False)  # Optional: new end time
    available_seats = serializers.IntegerField(required=False)  # Optional: new available seats count

# Serializer to handle requests for train schedule based on source, destination, and journey date
class TrainScheduleRequestSerializer(serializers.Serializer):
    source = serializers.CharField(max_length=100)  # Source station
    destination = serializers.CharField(max_length=100)  # Destination station
    journey_date = serializers.DateField()  # Journey date for the train schedule request

# Serializer for seat-related data
class SeatSerializer(serializers.Serializer):
    seat_number = serializers.IntegerField()  # Number of a specific seat

# Serializer to provide full booking details, including train and schedule information
class FullBookingDetailsSerializer(serializers.Serializer):
    train = TrainSerializer()  # Nested serializer for train details
    schedule = TrainScheduleSerializer()  # Nested serializer for train schedule details
    number_of_seats = serializers.IntegerField()  # Number of seats booked
    total_price = serializers.FloatField()  # Total price of the booking
    booking_date = serializers.DateTimeField()  # Date and time of the booking
    booking_status = serializers.BooleanField()  # Status of the booking (confirmed/canceled)
