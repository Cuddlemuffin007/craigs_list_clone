from django.contrib import admin

from pkmn_app.models import City, AccountProfile

admin.site.register([AccountProfile, City])
