from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class MagModel(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1000)
    code = models.CharField(max_length=50000)
    version = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    situation = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)


class ModelStatus(models.Model):
    name = models.CharField(max_length=128)
    process = models.CharField(max_length=50000)


class Feature(models.Model):
    param = models.CharField(max_length=128)
    description = models.CharField(max_length=1000)


class EndPoint(models.Model):
    name = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)


class MagStatus(models.Model):
    status = models.CharField(max_length=128)
    active = models.BooleanField()
    created_by = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_model = models.ForeignKey(MagModel, on_delete=models.CASCADE, related_name="status")


class MagRequest(models.Model):
    input_data = models.CharField(max_length=10000)
    full_response = models.CharField(max_length=10000)
    response = models.CharField(max_length=10000)
    feedback = models.CharField(max_length=10000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_model = models.ForeignKey(MagModel, on_delete=models.CASCADE)
