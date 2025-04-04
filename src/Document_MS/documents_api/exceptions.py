from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.getLogger(__name__)

# hanling error response
def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        # exceptions
        response.data = {
            'errors': response.data,
            'status_code': response.status_code,
        }
        logger.error(f"API Error: {exc}", exc_info=True)
    else:
        # Non-DRF exceptions (Django, Python, etc.)
        logger.critical(f"Unhandled Server Error: {exc}", exc_info=True)
        response = Response(
            {'errors': {'detail': 'Internal server error'}},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    return response