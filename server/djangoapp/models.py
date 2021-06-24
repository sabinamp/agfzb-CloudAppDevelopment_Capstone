from django.db import models
from django.utils.timezone import now
from django.conf import settings


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object

class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30, default='car make')
    description = models.CharField(max_length=1000)

    def __str__(self):
        return "Name: " + self.name + "," + \
               "Description: " + self.description


# <HINT> Create a plain Python class `CarDealer` to hold dealer data

class CarDealer(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    DEALER = 'Car Dealer'
    DATABASE_ADMIN = 'Database Admin'
    OCCUPATION_CHOICES = [
        (DEALER, 'Car Dealer'),
        (DATABASE_ADMIN, 'Database Admin')
    ]
    occupation = models.CharField(
        null=False,
        max_length=20,
        choices=OCCUPATION_CHOICES,
        default=DEALER
    )
    social_link = models.URLField(max_length=200)

    def __str__(self):
        return self.user.username + "," + \
               self.occupation


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'WAGON'
    MODEL_TYPES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'WAGON')
    ]
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=30, default='Sedan')
    dealer_id = models.ForeignKey(CarDealer, on_delete=models.DO_NOTHING)
    type = models.CharField(max_length=5, choices=MODEL_TYPES, default=SEDAN)
    year = models.DateField(default=now)

    def __str__(self):
        return self.name + "," + \
               self.type


# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview(models.Model):
    dealer = models.ForeignKey(CarDealer, on_delete=models.CASCADE)
    content = models.TextField()
