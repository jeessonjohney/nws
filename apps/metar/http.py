from django.http import JsonResponse


class MetarJsonResponse(JsonResponse):
    def __init__(
        self,
        status=200,
        data={},
        error="",
    ):
        structured_response = {}
        print(status, data, error)
        if str(status)[0] == "2":
            structured_response["message"] = "success"
            structured_response["data"] = data

        else:
            structured_response["message"] = "error"
            structured_response["error"] = error

        super().__init__(data=structured_response, safe=False, status=status)
