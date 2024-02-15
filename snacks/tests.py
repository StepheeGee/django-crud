from django.test import TestCase
from django.urls import reverse
from .models import Snack

class SnackTests(TestCase):
    def setUp(self):
        self.snack = Snack.objects.create(name='Chips', description='Crunchy and delicious')

    def test_snack_list_view(self):
        url = reverse('snacks:snack_list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'snacks/snack_list.html')

    def test_snack_create_view(self):
        url = reverse('snacks:snack_create')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'snacks/snack_form.html')

    def test_snack_detail_view(self):
        url = reverse('snacks:snack_detail', args=[self.snack.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'snacks/snack_detail.html')
