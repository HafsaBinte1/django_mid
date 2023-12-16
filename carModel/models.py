from django.db import models
from carBrand.models import CarBrand
from django.contrib.auth.models import User
# Create your models here.
class CarModel(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    quntity = models.IntegerField()
    description = models.TextField()
    barnd_name = models.ForeignKey(CarBrand,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='carModel/media/uploads', height_field=None, width_field=None, max_length=None,default='')
    

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    post = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return f"Comments by {self.name}"

class Purcehase_history(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    car = models.ForeignKey(CarModel,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} buy this car name: {self.car.name}"