from rest_framework import serializers

from freelancers.models import freelancer

class freelancerSerializer(serializers.ModelSerializer):
    class Meta:
        model = freelancer
        fields=('id','first_name','last_name')