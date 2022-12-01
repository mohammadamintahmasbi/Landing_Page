from django.db import models

# Create your models here.
class SlideShow(models.Model):
    image = models.ImageField()
    message = models.CharField(max_length = 30)
    title = models.CharField(max_length = 30)
    text = models.TextField()

class Services(models.Model):
    title = models.CharField(max_length = 30)
    text = models.TextField()

class Selected_Title(models.Model):
    title = models.CharField(max_length = 30)
    banner = models.TextField()

class Activites(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length = 30)
    text = models.TextField()

class Person(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length = 30)
    role = models.CharField(max_length = 30)
    social_id = models.AutoField(primary_key = True)

class SlideShow(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length = 30)
    text = models.TextField()

class Contant_Us(models.Model):
    WebSite_address = models.URLField()
    email = models.EmailField()
    telephone = models.IntegerField()
    address = models.CharField(max_length = 50)

class Messages(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()
    title = models.CharField(max_length = 30)
    message = models.TextField()

