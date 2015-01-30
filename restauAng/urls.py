from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import routers
from restauREST.api.views import RestaurantViewSet, TableViewSet, PartyViewSet

router = routers.DefaultRouter()
router.register(r'restaurants', RestaurantViewSet, base_name='restaurants')
router.register(r'tables', TableViewSet, base_name='tables')
router.register(r'partys', PartyViewSet, base_name='partys')

urlpatterns = patterns("",
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
)