from django.contrib.auth.models import User
from django.http import response
from django.test import TestCase
from django.urls import reverse

from store.models import Category, Product


class TestBasketView(TestCase):
    def setUp(self):
        User.objects.create(username='admin')
        Category.objects.create(name='django', slug='django')
        Product.objects.create(category_id=1, title='django beginners',
                               create_by_id=1, slug='django-beginners', price='20.00', image='django')
        Product.objects.create(category_id=1, title='django beginners',
                               create_by_id=1, slug='django-beginners', price='20.00', image='django')
        Product.objects.create(category_id=1, title='django beginners',
                               create_by_id=1, slug='django-beginners', price='20.00', image='django')
        self.client.post(reverse('basket:basket_add'), {"productid": 1, "productqty": 1, "action": "post"}, xhr=True)
        self.client.post(reverse('basket:basket_add'), {"productid": 2, "productqty": 2, "action": "post"}, xhr=True)

    def test_basket_url(self):
        '''
        Test homepage response status
        '''
        response = self.client.get(reverse('basket:basket_summary'))
        self.assertEqual(response.status_code, 200)

    def test_basket_add(self):
        '''
        Test adding items to basket
        '''

        response = self.client.post(
            reverse('basket:basket_add'), {"productid": 3, "productqty": 1, "action": "post"}, xhr=True)
        self.assertEqual(response.json(), {'qty': 4})
        response = self.client.post(reverse('basket:basket_add'), {
                                    "productid": 2, "productqty": 1, "action": "post"}, xhr=True)
        self.assertEqual(response.json(), {'qty': 3})
