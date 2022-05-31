from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    """
        define my_discount as read only property
        this property belongs to this ProductSerializer
        this is known as an inline field
    """
    my_discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = [
            "pk",
            "title",
            "content",
            "price",
            "sale_price",
            # tells django to look for the my_discount property
            "my_discount"
        ]

    def get_my_discount(self, obj):
        """
            when looking for the my_discount property, this method
            will be called

            the object recieved here is that instance of the model
        """
        if not hasattr(obj, "id"):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()
        # try:
        #     return obj.get_discount()
        # except:
        #     return None

