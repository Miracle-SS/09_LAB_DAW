from django.db import models

# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Framework(models.Model):
    name = models.CharField(max_length=20)

    language = models.ForeignKey(
        Language,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=20)

    languages = models.ManyToManyField(
        Language
    )

    def __str__(self):
        return self.name