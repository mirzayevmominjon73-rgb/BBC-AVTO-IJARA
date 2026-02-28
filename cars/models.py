from django.db import models


class About(models.Model):
    title = models.CharField(max_length=255, default="Biz haqimizda")
    description = models.TextField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    phone = models.CharField(max_length=50)
    telegram = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"Kontakt: {self.phone}"


class Employee(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    photo = models.ImageField(upload_to='employees/', blank=True, null=True)

    def __str__(self):
        return self.name



class Car(models.Model):
    CATEGORY_CHOICES = [
        ('auto', 'Avtomobillar'),
        ('promo', 'Aksiyadagi mashinalar'),
        ('electric', 'Electric'),
        ('news', 'Yangiliklarimiz')
    ]
    TRANSMISSION_CHOICES = [
        ('manual', 'Mexanika'),
        ('automatic', 'Avtomat')
    ]

    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    main_image = models.ImageField(upload_to='cars/', blank=True, null=True)  # asosiy rasm
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='auto')
    down_payment = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    interest_rate = models.FloatField(default=25.0)
    transmission = models.CharField(max_length=10, choices=TRANSMISSION_CHOICES, default='manual')
    is_electric = models.BooleanField(default=False)
    is_promo = models.BooleanField(default=False)
    year = models.PositiveIntegerField(null=True, blank=True)
    color = models.CharField(max_length=50, null=True, blank=True)
    cpg = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class CarImage(models.Model):
    car = models.ForeignKey(
        Car,
        related_name='images',
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='cars/')

    def __str__(self):
        return f"{self.car.title} rasmi"



class InterestSetting(models.Model):
    yearly_interest = models.FloatField(default=25.0)

    def __str__(self):
        return f"Foiz: {self.yearly_interest}%"
