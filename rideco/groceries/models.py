from django.db import models

class Lists(models.Model):
    list_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date created')


class Items(models.Model):
    list = models.ForeignKey(Lists, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)