from django.urls import path
from . import views

from .views import FreelancerListView,FreelancerDetailView,SearchFreelancerListView,AdvanceSearchFreelancerListView

urlpatterns=[
    path('',FreelancerListView.as_view()),
    path('searchList/',SearchFreelancerListView.as_view()),
    path('searchList/AdvanceSearch',views.AdvanceSearchFreelancerListView),
    path('<pk>',FreelancerDetailView.as_view())
] 