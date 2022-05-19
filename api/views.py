from django.http import JsonResponse
import json

def api_home(request, *args, **kwargs):
    body = request.body # json data -> bstring of json data
    print("request.body")
    print(request.GET)
    print(body)
    data = {}
    try:
        data = json.loads(body)
    except:
        pass

    # data["headers"] = request.headers
    data["params"] = dict(request.GET)
    data["headers"] = dict(request.headers)
    data["content_type"] = request.content_type

    return JsonResponse(data)
