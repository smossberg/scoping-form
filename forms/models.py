from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=400)
    abbrevation = models.CharField(max_lenght=8)
    version = models.CharField(max_lenght=42)


class Project_type(models.model):
    name = models.CharField(max_lenght=42)


class Engagement(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    project_type = models.ForeignKey(Project_type)
    description = models.CharField(max_lenght=1000)


class Task(models.Model):
    project = models.ForeignKey(Engagement)
    name = models.CharField(max_lenght=50)
    description = models.CharField(max_length=200)


class Result(models.model):
    project = models.ForeignKey(Engagement)
    name = models.CharField(max_lenght=50)
    description = models.CharField(max_length=200)


class Requirement(models.model):
    project = models.ForeignKey(Engagement)
    name = models.CharField(max_lenght=50)
    description = models.CharField(max_length=400)
