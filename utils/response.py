import logging

from rest_framework.response import Response

# Set up a logger for this module
logger = logging.getLogger(__name__)

def success_response(status, msg, data, *args, **kwargs):
    """
    Generate a success response for the API.

    Args:
        status (int): HTTP status code.
        msg (str): Message detailing the success.
        data (dict): Data to be included in the response.
        *args: Additional positional arguments.
        **kwargs: Additional keyword arguments.

    Returns:
        Response: A DRF Response object with success status.
    """
    response = {
        "status_code": status,
        "status": "success",
        "detail": msg,
        "data": data,
    }
    return Response(data=response, status=status)

def error_response(status, msg, data, *args, **kwargs):
    """
    Generate an error response for the API.

    Args:
        status (int): HTTP status code.
        msg (str): Message detailing the error.
        data (dict): Data to be included in the response.
        *args: Additional positional arguments.
        **kwargs: Additional keyword arguments.

    Returns:
        Response: A DRF Response object with error status.
    """
    response = {
        "status_code": status,
        "status": "failure",
        "detail": msg,
        "data": data
    }
    # Log a warning with the caller function and data if provided
    caller_func = kwargs.get("caller_func", None)
    logger.warning(f"Caller Function: {caller_func} DATA: {data}")
    return Response(data=response, status=status)
