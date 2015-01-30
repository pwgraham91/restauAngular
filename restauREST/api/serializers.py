from rest_framework import serializers
from restauREST.models import Restaurant, Table, Party


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'username', 'restaurant_name', 'email', 'date_joined', 'is_staff', 'is_active', 'last_login',
                  'is_superuser')


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table


class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
