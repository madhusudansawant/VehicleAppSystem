from rest_framework.views import exception_handler
from rest_framework.response import Response


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None and response.status_code in [401, 403]:
        return Response(
            {
                "success": False,
                "status_code": response.status_code,
                "message": response.data.get("detail", "Permission denied"),
            },
            status=response.status_code
        )

    return response
