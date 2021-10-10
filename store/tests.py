from django.urls import reverse
from django.test import TestCase

from .models import Album, Artist, Contact, Booking

# Create your tests here.
class IndexPageTestCase(TestCase):
    #test that index page return code status 200
    def test_index_page(self):
         response = self.client.get(reverse('index'))
         self.assertEquals(response.status_code, 200)

#detail page
class DetailPageTestCase(TestCase):

    def setUp(self):
        impossible = Album.objects.create(title="Transmission Impossible")
        self.album = Album.objects.get(title="Transmission Impossible")

    # test that detail page return 200 if the item exists
    def test_detail_page_returns_200(self):
        album_id = self.album.id
        response = self.client.get(reverse('store:detail', args=(album_id,)))
        self.assertEqual(response.status_code, 200)

    def test_detail_page_returns_404(self): 
        album_id = self.album.id + 1
        response = self.client.get(reverse('store:detail', args=(album_id,)))
        self.assertEqual(response.status_code, 404)

class BookingPageTestCase(TestCase):

    #the setUp function create a new booking
    def setUp(self):
        Contact.objects.create(name="Freddi", email="fred@gmail.com")
        impossible = Album.objects.create(title="Transmission Impossible")
        journey = Artist.objects.create(name="Journey")
        impossible.artists.add(journey)
        self.contact = Contact.objects.get(name="Freddi")
        self.album = Album.objects.get(title="Transmission Impossible")

    #test that a new booking is made
    def test_new_booking_is_registered(self):
        old_bookings = Booking.objects.count()
        album_id = self.album.id
        name = self.contact.name
        email =  self.contact.email
        response = self.client.post(reverse('store:detail', args=(album_id,)), {
            'name': name,
            'email': email
        })
        new_bookings = Booking.objects.count()
        self.assertEqual(new_bookings, old_bookings + 1)

    #test that a bookikng is belongs to a contact
    def test_new_booking_belongs_to_a_contact(self):
        album_id = self.album.id
        name = self.contact.name
        email =  self.contact.email
        response = self.client.post(reverse('store:detail', args=(album_id,)), {
            'name': name,
            'email': email
        })
        booking = Booking.objects.first()
        self.assertEqual(self.contact, booking.contact)

    #test that a new booking is belongs to an album
    def test_new_booking_belongs_to_an_album(self):
        album_id = self.album.id
        name = self.contact.name
        email = self.contact.email
        response = self.client.post(reverse('store:detail', args=(album_id,)), {
            'name': name,
            'email': email
        })
        booking = Booking.objects.first()
        self.assertEqual(self.album, booking.album)

    #test that an album is not available after a booking
    def test_album_not_available_if_booking(self):
        album_id = self.album.id
        name = self.contact.name
        email =  self.contact.email
        response = self.client.post(reverse('store:detail', args=(album_id,)), {
            'name': name,
            'email': email
        })
        # Make the query again, otherwise `available` will still be set at `True`
        self.album.refresh_from_db()
        self.assertFalse(self.album.available)
