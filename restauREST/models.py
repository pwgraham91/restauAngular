from django.contrib.auth.models import AbstractUser
from django.db import models

from datetime import datetime


class Restaurant(AbstractUser):
    restaurant_name = models.CharField(max_length=50)

    def __unicode__(self):
        return u"{}".format(self.username)


class Table(models.Model):
    table_name = models.CharField(max_length=10)
    seats = models.SmallIntegerField()
    restaurant = models.ForeignKey(Restaurant, related_name='restaurant_table')

    def __unicode__(self):
        return u"{}".format(self.table_name)


class Party(models.Model):
    party_name = models.CharField(max_length=50, blank=True)
    number_of_males = models.CharField(max_length=2)
    number_of_females = models.CharField(max_length=2)
    number_of_children = models.CharField(max_length=2)
    dinner = models.BooleanField(default=False)
    weekday = models.BooleanField(default=False)
    start_time = models.DateTimeField(auto_now_add=True, null=True)
    end_time = models.DateTimeField(null=True, blank=True)
    total_time = models.CharField(max_length=2, blank=True)
    predicted_end_time = models.DateTimeField(null=True, blank=True)
    table = models.ForeignKey(Table, related_name='table_party')

    def check_datetime(self):
        self.dinner = datetime.now().hour >= 16
        self.weekday = datetime.now().weekday() <= 4
        self.save()

    def __unicode__(self):
        return u"pk:{} name:{}".format(self.pk, self.party_name)
