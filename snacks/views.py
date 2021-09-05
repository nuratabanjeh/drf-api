from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Snacks
from .serializers import SnacksSerializer

class SnacksList(ListCreateAPIView):
    queryset = Snacks.objects.all()
    serializer_class = SnacksSerializer

class SnacksDetail(RetrieveUpdateDestroyAPIView):
    queryset = Snacks.objects.all()
    serializer_class = SnacksSerializer