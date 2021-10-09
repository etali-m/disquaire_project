from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField('Nom', max_length=200, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "artiste"

class Contact(models.Model):
    email = models.EmailField('e-mail',max_length=100)
    name = models.CharField('Nom', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "prospect"

class Album(models.Model):
    reference = models.IntegerField('reférence',null = True)
    created_at = models.DateTimeField('date création', auto_now_add=True)
    available = models.BooleanField('disponible',default=True)
    title = models.CharField('titre',max_length=200)
    picture = models.URLField("URL de l'image")
    artists = models.ManyToManyField(Artist, related_name='albums', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "disque"


class Booking(models.Model):
    created_at = models.DateTimeField('date d\'envoi', auto_now_add=True)
    contacted = models.BooleanField('demande traitée ?', default=False)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE) #un contact peut avoir +sieurs reservations
    album = models.OneToOneField(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.contact.name

    class Meta:
        verbose_name = "réservation"
        