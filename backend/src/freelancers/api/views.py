from rest_framework.generics import ListAPIView,RetrieveAPIView
from freelancers.models import freelancer
from .serializers import freelancerSerializer
from rest_framework import filters
from django.http import HttpResponse
from django.http import request
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import serializers
from django.core import serializers
from rest_framework import generics

import json

class FreelancerListView(ListAPIView):
    queryset=freelancer.objects.all()
    serializer_class=freelancerSerializer

class SearchFreelancerListView(ListAPIView):
    queryset=freelancer.objects.all()
    serializer_class=freelancerSerializer
    filter_backends=(filters.SearchFilter,)
    search_fields=('first_name','last_name')
         
    

class FreelancerDetailView(RetrieveAPIView):
    queryset=freelancer.objects.all()
    serializer_class=freelancerSerializer



def AdvanceSearchFreelancerListView(request):
        first_name=request.POST.get('cityName')
        print(request)
        print(first_name)
        queryset=freelancer.objects.filter(first_name=first_name)
        print(queryset)
        test = []
        for val in queryset:
            print(val)
            fl = FreeelanceView()
            posts_serialized = FreeelanceView()
            test.append(fl)
        posts_serialized = serializers.serialize('json', test)
        return Response(posts_serialized, safe=False) 
    


class FreeelanceView(object):
    firstName = "" 
    lastName = "" 
    id = 0 

class MultipleFieldLookupMixin(object):
    """
    Apply this mixin to any view or viewset to get multiple field filtering
    based on a `lookup_fields` attribute, instead of the default single field filtering.
    """
    def get_object(self):
        queryset = self.get_queryset()             # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs[field]: # Ignore empty fields.
                filter[field] = self.kwargs[field]
        obj = get_object_or_404(queryset, **filter)  # Lookup the object
        self.check_object_permissions(self.request, obj)
        return obj


class RetrieveFreelancerView(MultipleFieldLookupMixin, generics.RetrieveAPIView):
    queryset=freelancer.objects.all()
    serializer_class=freelancerSerializer
    lookup_fields = ('first_name', 'id')



