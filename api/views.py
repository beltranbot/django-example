import json

from django.forms.models import model_to_dict
from products.models import Product
# from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer


@api_view(["GET", "POST"])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        # data = model_to_dict(
        #     model_data,
        #     fields=["id", "title", "price", "sale_price"]
        # )
        data = ProductSerializer(instance).data
    return Response(data)
    # doing it manually
    #     # the fields parameter is optional
    #     data = model_to_dict(model_data, fields=['id', 'title', 'price'])
    #     json_data_str = json.dumps(data) # turns dict to json str
    # return HttpResponse(
    #     data,
    #     headers={"content-type": "application/json"}
    # )
