from account.custom_viewset import AdminViewSet  # Importing the custom Admin viewset for admin-specific permissions and authentication
from booking.serializers import TrainSerializer, AddTrainScheduleSerializer, UpdateTrainScheduleSerializer  # Importing serializers to validate and process the data
from utils.response import error_response, success_response  # Custom utility functions to standardize success and error responses
from rest_framework import status  # HTTP status codes for consistency in API responses
from booking.services.booking import BookingService  # Service layer for business logic related to booking operations

# Admin-specific ViewSet for managing bookings (like adding and updating trains and schedules)
class AdminBookingViewSet(AdminViewSet):

    # Method to add a new train to the system
    def add_train(self, request):
        # Validate the incoming request data using the TrainSerializer
        serializer = TrainSerializer(data=request.data)
        if not serializer.is_valid():
            # If data is invalid, return an error response with the validation errors
            return error_response(data=serializer.errors, msg="", status=status.HTTP_400_BAD_REQUEST)
        
        # If validation is successful, use the BookingService to add the train
        train = BookingService.add_train(serializer.validated_data)

        if not train:
            # If the train could not be added, return an error response
            return error_response(msg="Train not added", data={}, status=status.HTTP_400_BAD_REQUEST)
        
        # If the train was added successfully, return a success response with the train details
        return success_response(status=status.HTTP_201_CREATED, msg="Train added successfully", data=train)

    # Method to add a train schedule
    def add_train_schedule(self, request):
        # Validate the incoming request data using AddTrainScheduleSerializer
        serializer = AddTrainScheduleSerializer(data=request.data)
        if not serializer.is_valid():
            # If validation fails, return an error response with the validation errors
            return error_response(data=serializer.errors, msg="", status=status.HTTP_400_BAD_REQUEST)
        
        # Use BookingService to add the train schedule
        schedule = BookingService.add_train_schedule(serializer.validated_data)

        if not schedule:
            # If the schedule could not be added, return an error response
            return error_response(msg="Schedule not added", data={}, status=status.HTTP_400_BAD_REQUEST)
        
        # If the schedule was added successfully, return a success response with the schedule details
        return success_response(status=status.HTTP_201_CREATED, msg="Schedule added successfully", data=schedule)

    # Method to update an existing train schedule
    def update_train_schedule(self, request, schedule_id):
        # Validate the incoming request data using UpdateTrainScheduleSerializer
        serializer = UpdateTrainScheduleSerializer(data=request.data)
        if not serializer.is_valid():
            # If validation fails, return an error response with the validation errors
            return error_response(data=serializer.errors, msg="", status=status.HTTP_400_BAD_REQUEST)
        
        # Use BookingService to update the train schedule by passing the schedule_id and validated data
        schedule = BookingService.update_train_schedule(schedule_id, serializer.validated_data)

        if not schedule:
            # If the schedule could not be updated, return an error response
            return error_response(msg="Schedule not updated", data={}, status=status.HTTP_400_BAD_REQUEST)
        
        # If the schedule was updated successfully, return a success response with the updated schedule details
        return success_response(status=status.HTTP_201_CREATED, msg="Schedule updated successfully", data=schedule)
