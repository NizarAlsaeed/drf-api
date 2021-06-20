from django.urls import path
from .views import CityList, CityDetail


urlpatterns = [
    path('v1',CityList.as_view(), name='list'),
    path('v1/<int:pk>/', CityDetail.as_view(), name='detail'),
]
