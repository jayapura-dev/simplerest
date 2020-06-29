from ..models import Distrik, Kampung
from .serializers import DistrikSerializers, KampungSerializers
from rest_framework import viewsets, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class DistrikViewset(viewsets.ModelViewSet):
    serializer_class = DistrikSerializers
    queryset = Distrik.objects.all()

class KampungViewset(viewsets.ModelViewSet):
    serializer_class = KampungSerializers
    queryset = Kampung.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)