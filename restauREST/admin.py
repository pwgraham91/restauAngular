from django.contrib import admin

# from django.contrib.auth.admin import UserAdmin
from restauREST.models import Restaurant, Table, Party

admin.site.register(Restaurant)
admin.site.register(Table)
admin.site.register(Party)