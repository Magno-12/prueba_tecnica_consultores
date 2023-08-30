from django.test import TransactionTestCase, Client

from rest_framework_simplejwt.tokens import RefreshToken

from apps.user.models import User


class AuthIntegrationTest(TransactionTestCase):

    def setUp(self):
        self.client = Client()

        # Create a test user
        self.user_data = {
            'email': 'test@example.com',
            'username': 'testuser',
            'password': 'securepassword'
        }

        self.user = User.objects.create_user(**self.user_data)
        self.user.set_password('securepassword')
        self.user.save()

        self.access = str(RefreshToken.for_user(self.user).access_token)

    def test_login_successful(self):
        response = self.client.post('/auth/login/', {
            'email': self.user_data['email'],
            'password': self.user_data['password']
        })

        self.assertEqual(response.status_code, 200)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_login_invalid_email(self):
        response = self.client.post('/auth/login/', {
            'email': 'invalid@example.com',
            'password': self.user_data['password']
        })

        self.assertEqual(response.status_code, 400)

    def test_login_invalid_password(self):
        response = self.client.post('/auth/login/', {
            'email': self.user_data['email'],
            'password': 'invalidpassword'
        })

        self.assertEqual(response.status_code, 400)

    def test_logout_successful(self):
        # First login the user
        login_response = self.client.post('/auth/login/', {
            'email': self.user_data['email'],
            'password': self.user_data['password']
        })
        self.assertEqual(login_response.status_code, 200)  # Ensure login was successful

        # Then attempt to logout
        response = self.client.post('/auth/logout/', {
            'access_token': login_response.data['access']
        })
        self.assertEqual(response.status_code, 200)


    def test_logout_without_active_session(self):
        response = self.client.post('/auth/logout/')
        self.assertEqual(response.status_code, 401)
