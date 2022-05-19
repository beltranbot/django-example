from django.http import JsonResponse, HttpResponse
import json

from django.forms.models import model_to_dict
from products.models import Product


def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['id', 'title', 'price'])
    return JsonResponse(data)
    # doing it manually
    #     # the fields parameter is optional
    #     data = model_to_dict(model_data, fields=['id', 'title', 'price'])
    #     json_data_str = json.dumps(data) # turns dict to json str
    # return HttpResponse(
    #     data,
    #     headers={"content-type": "application/json"}
    # )
