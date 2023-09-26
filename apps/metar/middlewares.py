from django.http import JsonResponse


class LivenessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if "ping" in request.path:
            response_data = {"status": "OK"}
            return JsonResponse(response_data)
        return self.get_response(request)
