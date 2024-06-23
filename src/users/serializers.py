from django.contrib.auth.models import User

from rest_framework import serializers

# serializer is a class in a django application: Allows to take in complex query sets and model instances 
# and then convert them to native python data types that can be rendered into JSON / content types.
# Also able to perform deserialization
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'first_name', 'last_name', 'email']