from django.test import TestCase, Client
from user_management.users import CreateNewUser, ConnectUser


class TestCreateNewUser(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.data_login = {
            'username': "userT",
            "password": "test1234&"
        }
        cls.data_register = {
            'first_name': "user",
            'last_name': "test",
            'email': "email@test-user.com",
            'password': "test1234&",
            're_password': "test1234&"
        }
        cls.res, cls.msg, cls.user = CreateNewUser(
            cls.data_register).register()

    def test_user_login_success(self):
        c = Client()
        request = c.post(
            '/users/login-user/',
            {'username': "userT", 'password': 'test1234&'})

        self.assertRedirects(request, '/', status_code=302,
                             target_status_code=200, msg_prefix='',
                             fetch_redirect_response=True)

    def test_user_login_fail(self):
        c = Client()
        request = c.post(
            '/users/login-user/',
            {'username': "userFailed", 'password': 'wrongwrong1234@'})

        self.assertRedirects(request, '/users/login/', status_code=302,
                             target_status_code=200, msg_prefix='',
                             fetch_redirect_response=True)

    def test_user_login_fail_message(self):
        response = self.client.post(
            "/users/login-user/",
            data={'username': "userFailed", 'password': 'wrongwrong1234@'},
            follow=True)

        messages = response.context['messages']

        for message in messages:
            self.assertEqual(message.level_tag, 'error')
            self.assertEqual(message.message, "Authentification failed")
