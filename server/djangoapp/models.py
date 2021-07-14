from django.core.validators import MinValueValidator, MaxValueValidator
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
    """ CarMake Class"""
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
    city = models.CharField(null=False, max_length=100, default="New York")

    def __str__(self):
        return "Dealer " + self.user.username + "," + \
               self.city


#   Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    YEAR_CHOICES = []
    for r in range(now().year, 1970, -1):
        YEAR_CHOICES.append((r, r))
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'WAGON'
    SPORTS = 'sports_car'
    PASSAT = 'passat'
    SALON = 'salon'
    COUPE = 'coupe'
    MODEL_TYPES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'WAGON'),
        (SPORTS, 'SPORTS CAR'),
        (PASSAT, 'PASSAT'),
        (SALON, 'SALON'),
        (COUPE, 'COUPE')
    ]
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=30, default='Sedan')
    dealer_id = models.ForeignKey(CarDealer, on_delete=models.DO_NOTHING, null=True, blank=True)
    year = models.IntegerField(choices=YEAR_CHOICES, default=now().year, null=False)
    type = models.CharField(max_length=15, choices=MODEL_TYPES, default=SEDAN)

    # year = models.PositiveIntegerField(validators=[MinValueValidator(1900), MaxValueValidator(now().year)],
    #                                    default=now().year - 5,
    #                                    help_text="Use the following format: <YYYY>")

    def __str__(self):
        return self.name + "," + \
               self.type + "," + \
               self.car_make.name


# a plain Python class `DealerReview` to hold review data
class DealerReview(models.Model):
    dealer = models.ForeignKey(CarDealer, on_delete=models.CASCADE)
    review = models.TextField()
    sentiment = models.TextField(blank=True)

    def __str__(self):
        return "Review: " + self.review
