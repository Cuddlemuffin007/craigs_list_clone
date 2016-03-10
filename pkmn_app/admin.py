from django.contrib import admin

from pkmn_app.models import City, AccountProfile, Pokemon, Category, SubCategory

admin.site.register([AccountProfile, City, Pokemon, Category, SubCategory])
