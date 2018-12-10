from django.db import models

# Create your models here.




class Location(models.Model):
    province = models.CharField(max_length=50)
    District = models.CharField(max_length=50)
    City=models.CharField(max_length=50)

    def __str__(self):
        return str(self.pk)

class Skill(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


TIPOLOGIA_CHOICES = [
    ("male", "Male"),
    ("female", "Female"),
]

TIPOLOGIA2_CHOICES = [
    ("freelancer", "Freelancer"),
    ("educator", "Educator"),
]
class freelancer(models.Model):
    id_no = models.CharField(max_length=20, null=True)
    first_name=models.CharField(max_length=50, null=True)
    last_name=models.CharField(max_length=50, null=True)
    types = models.CharField(max_length=20, choices=TIPOLOGIA2_CHOICES, null=True)
    rating = models.FloatField(default=0.0)
    likes=models.IntegerField(default=0)
    self_desc=models.CharField(max_length=1500, null=True)
    price = models.FloatField(default=0.0)
    skill=models.ManyToManyField(Skill)
    skill_level = models.CharField(max_length=50, null=True)
    expierience=models.IntegerField(default=0)
    recent_review= models.CharField(max_length=650, null=True)
    gender = models.CharField(max_length=20, choices=TIPOLOGIA_CHOICES, null=True)
    profile_picture = models.CharField(max_length=650, null=True)
    recent_works1=models.CharField(max_length=650, null=True)
    recent_works2=models.CharField(max_length=650, null=True)
    recent_works3=models.CharField(max_length=650, null=True)
    city=models.CharField(max_length=50, null=True)
    district=models.CharField(max_length=50, null=True)
    province=models.CharField(max_length=50, null=True)

    def __str__(self):
        return str(self.pk)

