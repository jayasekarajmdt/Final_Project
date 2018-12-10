from rest_framework import serializers

from freelancers.models import freelancer
from freelancers.models import Skill






class freelancerSerializer(serializers.ModelSerializer):
    skill=serializers.StringRelatedField(many=True)
    
    class Meta:
        model = freelancer
        fields=('id','first_name','last_name','rating','profile_picture','price','types','skill',
             'recent_works1','recent_works2','recent_works3','likes','skill_level','self_desc','gender','city','district','province','skill_level','expierience','recent_review')


class SkillSerializer(serializers.ModelSerializer):
    skill_list=freelancerSerializer(many=True)

    class Meta:
        model=Skill
        field=('name','skill_list')