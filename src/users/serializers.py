from django.contrib.auth.models import User

from rest_framework import serializers

# serializer is a class in a django application: Allows to take in complex query sets and model instances 
# and then convert them to native python data types that can be rendered into JSON / content types.
# Also able to perform deserialization
class UserSerializer(serializers.ModelSerializer):
    
    # write_only - don't show password hashes with required false
    password = serializers.CharField(write_only=True, required=False)
    
    # called when post request is made
    def create(self, validated_data): 
        # pop returns value of key and password key is removed from validated data
        password = validated_data.pop('password')
        # create new user object in database using validated data fields
        user = User.objects.create(**validated_data)
        # take care of hashing logic
        user.set_password(password)
        # perform db transaction
        user.save()
        return user
    
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'first_name', 'last_name', 'email', 'password']