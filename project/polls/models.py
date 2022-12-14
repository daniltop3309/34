from django.db import models


class PostList(models.Model):
    name = models.CharField("name", "name", max_length=100)
    age = models.IntegerField("age", "age")
