from django.urls import path

from .views import FreelancerListView,FreelancerDetailView

urlpatterns=[
    path('',FreelancerListView.as_view()),
    path('<pk>',FreelancerDetailView.as_view())
] 