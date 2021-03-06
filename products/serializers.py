from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product
from . import validators


class ProductSerializer(serializers.ModelSerializer):
    """
        define my_discount as read only property
        this property belongs to this ProductSerializer
        this is known as an inline field
    """
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    # recommended method
    # adds a url to the resource in the json body response
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk'
    )
    """
    write only field will be required in the data received for the 
    creation of the object but has to be removed before saving the
    object itself (validated_data.pop("email")) because the field
    doesn't exists in the database.
    This is usually done in the create function in the serializer
    """
    # email = serializers.EmailField(write_only=True)

    # linking with validator from external file
    title = serializers.CharField(validators=[
        validators.unique_product_title,
        validators.validate_title_no_hello
    ])
    # name = serializers.CharField(source='name', read_only=True)

    # for foreign relationships
    # email = serializers.CharField(source='user.email', read_only=True)

    class Meta:
        model = Product
        fields = [
            # "user",
            "edit_url",
            "url",
            # "email", for the write only field example
            "pk",
            "title",
            # 'name', copy of the title
            "content",
            "price",
            "sale_price",
            # tells django to look for the my_discount property
            "my_discount"
        ]

    # custom validation
    # def validate_title(self, value):
    #     request = self.context.get('request')
    #     user = request.user
    #     # iexact case insensitive
    #     qs = Product.objects.filter(user=user, title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(
    #             f"{value} is already a product name"
    #         )
    #     return value

    # def create(self, validated_data):
    #     """
    #     called when saving an instance with the serializer
    #     """
    #     # return Product.objects.create(**validated_data)
    #     # email = validated_data.pop('email')
    #     obj = super().create(validated_data)
    #     # print(email, obj)
    #     return obj

    # def update(self, instance, validated_data):
    #     """
    #     called when updating an instance with the serializer
    #     """
    #     email = validated_data.pop('email')
    #     return super().update(instance, validated_data)

    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-edit", kwargs={
            "pk": obj.pk
        }, request=request)

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
