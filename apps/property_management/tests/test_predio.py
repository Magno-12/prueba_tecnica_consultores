import json

from django.test import TransactionTestCase, Client

from apps.user.models import User
from apps.property_management.models import Predio
from apps.user.models.owner import Owner


class PredioIntegrationTest(TransactionTestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(email="test@example.com", password="testpassword")
        self.owner = Owner.objects.create(
            user=self.user, 
            nombre="Test Owner", 
            tipo="Natural", 
            numero_identificacion="123456", 
            tipo_identificacion="Cédula de ciudadanía"
        )
        self.predio = Predio.objects.create(
            nombre_direccion="Test Address", 
            tipo="Urbano", 
            numero_catastral="123", 
            numero_matricula="456"
        )
        self.predio.propietarios.add(self.owner)

        self.login_data = {
            "email": "test@example.com",
            "password": "testpassword"
        }

    def login(self):
        login_response = self.client.post('/auth/login/', data=self.login_data)
        return login_response.data['access']

    def test_list_predios(self):
        token = self.login()
        response = self.client.get('/predio/', HTTP_AUTHORIZATION=f'Bearer {token}')
        self.assertEqual(response.status_code, 200)

    def test_create_predio(self):
        token = self.login()
        predio_data = {
            "nombre_direccion": "New Address",
            "tipo": "Rural",
            "numero_catastral": "789",
            "numero_matricula": "012",
            "propietarios": [self.owner.id]
        }
        response = self.client.post('/predio/', data=predio_data, HTTP_AUTHORIZATION=f'Bearer {token}')
        self.assertEqual(response.status_code, 201)

    def test_update_predio(self):
        token = self.login()
        updated_data = {
            "nombre_direccion": "Updated Address"
        }
        response = self.client.patch(
            f'/predio/{self.predio.id}/',
            data=json.dumps(updated_data),
            content_type='application/json',
            HTTP_AUTHORIZATION=f'Bearer {token}'
        )
        self.assertEqual(response.status_code, 200)

    def test_delete_predio(self):
        token = self.login()
        response = self.client.delete(f'/predio/{self.predio.id}/', HTTP_AUTHORIZATION=f'Bearer {token}')
        self.assertEqual(response.status_code, 204)
