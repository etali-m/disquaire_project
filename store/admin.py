from django.contrib import admin

# Register your models here.
from .models import Booking, Contact, Album, Artist


class BookingInlines(admin.TabularInline):
    model = Booking
    fieldsets = [
        (None, {'fields': ['album', 'contacted']}) #list columns
    ]
    extra = 0
    verbose_name = "Réservation"
    verbose_name_plural = "Réservations"

class AlbumArtistsInline(admin.TabularInline):
    model = Album.artists.through #Le modele est Album mais on va recuperer les données en passant par la tabble artist
    extra = 1
    verbose_name = "Disque"
    verbose_name_plural = "Disques"

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    inlines = [BookingInlines,] # list of bookings made by a contact


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    inlines = [AlbumArtistsInline, ] # artists with theirs albums


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    search_fields = ['reference', 'title'] #On rechercher dans les reférences et les titres

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_filter = ['created_at', 'contacted']