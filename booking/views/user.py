from account.custom_viewset import UserViewSet
from booking.serializers import BookSeatSerializer, TrainScheduleRequestSerializer
from utils.response import error_response, success_response
from rest_framework import status

from booking.services.booking import BookingService

class BookingViewSet(UserViewSet):
    
    def create_booking(self, request):
        """Create booking view"""
        # Deserialize the incoming data
        serializer = BookSeatSerializer(data=request.data)
        # Check if the data is valid
        if not serializer.is_valid():
            # Return an error response if the data is invalid
            return error_response(data=serializer.errors, msg="", status=status.HTTP_400_BAD_REQUEST) 
        
        # Debugging line (commented out)
        # import pdb; pdb.set_trace()

        # Create a new booking using the validated data
        booking, message = BookingService.create_booking(request.user, serializer.validated_data)

        # If booking creation failed, return an error response
        if not booking:
            return error_response(msg=message, data={}, status=status.HTTP_400_BAD_REQUEST)

        # Return a success response if the booking was created successfully
        return success_response(status=status.HTTP_201_CREATED, msg=message, data=booking)   
    
    def get_trains(self, request):
        """Get all trains view"""
        # Deserialize the incoming data
        serializer = TrainScheduleRequestSerializer(data=request.data)
        # Check if the data is valid
        if not serializer.is_valid():
            # Return an error response if the data is invalid
            return error_response(data=serializer.errors, msg="", status=status.HTTP_400_BAD_REQUEST)
        
        # Retrieve the list of trains based on the validated data
        trains = BookingService.get_trains(serializer.validated_data)

        # If no trains are found, return an error response
        if not trains:
            return error_response(msg="No trains found", data={}, status=status.HTTP_400_BAD_REQUEST)

        # Return a success response if trains were found
        return success_response(status=status.HTTP_200_OK, msg="Trains fetched successfully", data=trains)
        
    def get_booking(self, request, booking_uuid):
        """Get booking view"""
        # Retrieve the booking details based on the booking UUID
        bookings = BookingService.get_booking(booking_uuid)
        # Return a success response with the booking details
        return success_response(status=status.HTTP_200_OK, msg="Booking fetched successfully", data=bookings)
