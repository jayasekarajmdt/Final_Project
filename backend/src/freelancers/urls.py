from django.urls import path,include
from . import views

urlpatterns=[
    path('api',include('freelancers.api.urls')),
    path('', views.Search, name='search'),
    path('searchByType', views.SearchByType, name='searchByType'),
    path('searchByTypeAndPrice', views.SearchByTypeAndPrice, name='searchByTypeAndPrice'),
    path('SearchByTypeAndGender', views.SearchByTypeAndGender, name='SearchByTypeAndGender')
  
] 