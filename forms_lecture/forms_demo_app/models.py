from django.db import models

# Create your models here.
INSTRUMENTS = (
    ('Option 1', 'Value 1'),
    ('Option 2', 'Value 2')
)

class User(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    fav_instrument = models.CharField(max_length=100, choices=INSTRUMENTS)
    rock = models.BooleanField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)