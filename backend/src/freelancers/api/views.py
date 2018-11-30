from rest_framework.generics import ListAPIView,RetrieveAPIView
from freelancers.models import freelancer
from .serializers import freelancerSerializer

class FreelancerListView(ListAPIView):
    queryset=freelancer.objects.all()
    serializer_class=freelancerSerializer


class FreelancerDetailView(RetrieveAPIView):
    queryset=freelancer.objects.all()
    serializer_class=freelancerSerializer