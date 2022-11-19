from django.urls import path, include
from .views import *


urlpatterns = [

    path('', homepage, name="home"),
    path('contact/', contact, name="contact"),
    path('product/', product, name="product"),
    path('media/', mediapage, name="media"),
    path('building/<int:pk>/', buildingpage, name="building"),
    path('buildingdata/<int:group_id>/<int:pk>/', buildingdata, name="buildingdata")



]
