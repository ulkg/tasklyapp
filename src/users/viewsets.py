from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer

from .permissions import IsUserOwnerOrGetAndPostOnly

# modelviewset has predefined methods for create etc., ViewSet requires own declaration
class UserViewSet(viewsets.ModelViewSet):
    # tells premissions viewset has over models of users in the database - in this case all
    queryset = User.objects.all()
    permission_classes = [IsUserOwnerOrGetAndPostOnly]
    serializer_class = UserSerializer