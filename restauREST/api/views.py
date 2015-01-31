from rest_framework import viewsets, filters
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from restauREST.api.serializers import RestaurantSerializer, TableSerializer, PartySerializer
from restauREST.models import Restaurant, Table, Party

filter_backends = filters.DjangoFilterBackend


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filter_fields = ('username', 'restaurant_name', 'email', 'date_joined', 'is_staff', 'is_active', 'last_login',
                     'is_superuser')
    authentication_classes = (TokenAuthentication, SessionAuthentication)


class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    filter_fields = ('table_name', 'seats', 'restaurant')


class PartyViewSet(viewsets.ModelViewSet):
    queryset = Party.objects.all()
    serializer_class = PartySerializer
    filter_fields = ('party_name', 'number_of_males', 'number_of_females', 'number_of_children', 'dinner', 'weekday',
                     'start_time', 'end_time', 'total_time', 'predicted_end_time', 'table')
    search_fields = ('party_name')
