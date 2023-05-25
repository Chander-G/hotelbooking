from django.db import models
from django.contrib.auth.models import User
# Create your models here.

property_type=(
    ('S',"sales"),
    ('R',"rent")
)

class Property(models.Model):
    name=models.CharField(max_length=50)
    property_type=models.PositiveIntegerField(choices=property_type,max_length=20)
    price=models.PositiveIntegerField()
    area=models.DecimalField(decimal_places=2,max_digits=8)
    beds_number=models.PositiveIntegerField()
    baths_number=models.PositiveIntegerField()
    garages_number=models.PositiveIntegerField()
