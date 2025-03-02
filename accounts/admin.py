from django.contrib import admin
from. models import Golfer, FavoriteGolfer
# Register your models here.

class GolferAdmin(admin.ModelAdmin):
    list_display = ('name', 'tier')

class FavoriteGolferAdmin(admin.ModelAdmin):
    list_display = ('user', 'golfer') #Display the users favirye golfer ib the admin
    list_filter = ('user',) #filter bu user (helos admins view daborute golfers per user)


#rigister models in admin panel
admin.site.register(Golfer, GolferAdmin)
admin.site.register(FavoriteGolfer, FavoriteGolferAdmin)
