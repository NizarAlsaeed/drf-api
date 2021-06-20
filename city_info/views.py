from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import City
from .serializers import CitySerializer
# Create your views here.
class CityList(ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
class CityDetail(RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
