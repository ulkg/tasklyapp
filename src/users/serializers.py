from django.contrib.auth.models import User

from rest_framework import serializers

# serializer is a class in a django application: Allows to take in complex query sets and model instances 
# and then convert them to native python data types that can be rendered into JSON / content types.
# Also able to perform deserialization
class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True)
    password = serializers.CharField(write_only=True, required=False)

    def created(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        return user
    
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'first_name', 'last_name', 'email', 'password']