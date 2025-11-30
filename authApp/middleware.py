from django.http import JsonResponse

class IPFilterMiddleware:
    """
    Middleware to allow/deny requests based on IP address
    """
    ALLOWED_IPS = [
        "127.0.0.1"
    ]

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = self.get_client_ip(request)
    

        
        if ip not in self.ALLOWED_IPS:
            return JsonResponse(
                {"success": False, "message": "Forbidden: IP not allowed"}, 
                status=403
            )

        response = self.get_response(request)
        return response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
