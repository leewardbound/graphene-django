from django.db import models


class MyFakeModel(models.Model):
    cool_name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)


class MyFakeModelWithChoices(models.Model):
    cool_name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=8, choices=(("ok", "OK"), ("not_ok", "NOT OK!"))
    )

# We should be able to register 2 models each with a status choices field
class AnotherFakeModelWithChoices(models.Model):
    other_name = models.CharField(max_length=50)
    status = models.CharField(
        max_length=8, choices=(("enabled", "Enabled"), ("disabled", "DISABLED!"))
    )


class MyFakeModelWithPassword(models.Model):
    cool_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
