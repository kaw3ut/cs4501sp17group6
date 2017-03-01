from django.test import TestCase
from django.core.urlresolvers import reverse
from .models import Listing, User
import json

class ListingTestPopulated(TestCase):

	fixtures = ['db_init.json']

	def test_show_all_listings(self):
		response = self.client.get(reverse('listings')).json()
		self.assertEqual(response['ok'], True)

	def test_show_one_listing(self):
		response = self.client.get(reverse('listing_detail', args=[1]))
		self.assertContains(response, 'info')

	def test_create_listing(self):
		data = {
			'title': 'Apartment for rent',
			'address': '123 Bluejay Lane',
			'residence_type': "A",
			'num_of_bedrooms': '2',
			'num_of_bathrooms': '1',
			'price': '600',
			'sqft': '800',
			'lot_size': "S",
			'max_occupancy': '3',
			'availability_start': '2017-06-01',
			'availability_end': '2018-05-31', 
			'availability_status': 'AVAIL',
			'description': 'Please give me money',
			'post_date': '2017-03-01',
			'post_expiration_date': '2017-03-03',
			'last_edited_date': '2017-03-01',
			'laundry': True,
			'parking': True,
			'pet_friendly': False,
			'smoking': False,
			'water': True,
			'gas': False,
			'power': False,
			'wifi': True,
			'wheelchair_access': False,
			'furnished': False,
			'balcony': True,
			'yard': False,
			'images': True,
			'gym': True,
			'maintenance': True,
			'user': 1
		}
		response = self.client.post(reverse('new_listing'), data)
		self.assertContains(response, 'successfully created')
		

	def test_update_listing(self):
		data = {
			"title": "Townhouse Available in Friendly Neighborhood",
      		"address": "123 Memory Lane Charlottesville, VA 22904",
      		"residence_type": "T",
      		"num_of_bedrooms": "4",
      		"num_of_bathrooms": "2",
      		"price": "1000",
      		"sqft": "1765",
      		"lot_size": "S",
      		"max_occupancy": "4",
      		"availability_start": "2017-03-11",
      		"availability_end": "2017-07-30",
      		"availability_status": "AVAIL",
      		"description": "A beautiful townhouse available for sale in Charlottesville, VA!",
      		"post_date": "2017-02-11",
      		"post_expiration_date": "2017-07-30",
      		"last_edited_date": "2017-02-14",
  		    "laundry": False,
  	    	"parking": False,
  	    	"pet_friendly": False,
  	    	"smoking": False,
  	    	"water": False,
  	    	"gas": False,
  	    	"power": False,
  	    	"wifi": False,
  	    	"wheelchair_access": False,
  	    	"furnished": False,
  	    	"balcony": False,
  	    	"yard": False,
  	    	"images": False,
  	    	"gym": False,
  	    	"maintenance": False,
          	"user": 1
		}
		response = self.client.post(reverse('listing_detail', args=[1]), data)
		print(response.json())
		self.assertContains(response, 'successfully updated')

	def test_delete_listing(self):
		pass

class ListingTestEmpty(TestCase):

	def test_show_nonexistent_listing(self):
		response = self.client.get(reverse('listing_detail', kwargs={'id':999}))
		self.assertContains(response, 'no listing exists')

class UserTestPopulated(TestCase):

	fixtures = ['db_init.json']

	def test_show_all_users(self):
		pass

	def test_show_one_user(self):
		pass

	def test_create_user(self):
		pass

	def test_update_user(self):
		pass

	def test_delete_user(self):
		pass

class UserTestEmpty(TestCase):

	def test_show_nonexistent_user(self):
		pass
