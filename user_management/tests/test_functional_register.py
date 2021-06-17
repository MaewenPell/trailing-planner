from django.test import TestCase, Client
from user_management.users import CreateNewUser


class TestCreateNewUser(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.correct_data = {
            'first_name': "LocalTestUser",
            'last_name': "LastNameTestUser",
            'email': "email@test-user.com",
            'password': "test1234&",
            're_password': "test1234&"
        }

        cls.missing_data = {
            'first_name': "",
            'last_name': "test",
            'email': "email@test-user.com",
            'password': "test1234&",
            're_password': "test1234&"
        }
        cls.res, cls.msg, cls.user = CreateNewUser(cls.correct_data).register()

    def test_view_register(self):
        c = Client()
        response = c.get('/users/register/')
        self.assertEqual(200, response.status_code)

    def test_class_data_are_correct(self):
        self.assertEqual(self.user.first_name, self.correct_data["first_name"])
        self.assertEqual(self.user.last_name, self.correct_data["last_name"])
        self.assertEqual(self.user.email, self.correct_data["email"])

        self.assertEqual(self.msg, "")
        self.assertTrue(self.res)

    def test_username_generated(self):
        # Username should be first_name + first letter of lastname in uppercase
        expected = "LocalTestUserL"
        self.assertEqual(expected, self.user.username)

    def test_all_field_arent_filled_raised_error(self):
        res, msg, _ = CreateNewUser(self.missing_data).register()
        self.assertEqual(msg[0], "Some field are empty")
        self.assertFalse(res)

    def test_password_are_too_short(self):
        res, msg, _ = CreateNewUser(
            {
                'first_name': "LocalTestUser",
                'last_name': "LastNameTestUser",
                'email': "email@test-user.com",
                'password': "test",
                're_password': "test"
            }
        ).register()
        self.assertFalse(res)
        self.assertEqual(msg[0], "Password must contain at least 8 characters")

    def test_password_dont_match(self):
        res, msg, _ = CreateNewUser(
            {
                'first_name': "LocalTestUser",
                'last_name': "LastNameTestUser",
                'email': "email@test-user.com",
                'password': "test1234&",
                're_password': "test1234="
            }
        ).register()
        self.assertFalse(res)
        self.assertEqual(msg[0], "Password don't match")

    def test_password_are_too_weak(self):
        res, msg, _ = CreateNewUser(
            {
                'first_name': "LocalTestUser",
                'last_name': "LastNameTestUser",
                'email': "email@test-user.com",
                'password': "test1234",
                're_password': "test1234"
            }
        ).register()
        self.assertFalse(res)
        self.assertEqual(
            msg[0], "Password must coutain at least a special character")

    def test_first_name_last_name_are_too_long(self):
        long_first_name = int(149)*'test'
        long_last_name = int(151/4)*'test'
        res, msg, _ = CreateNewUser(
            {
                'first_name': f"{long_first_name}",
                'last_name': f"{long_last_name}",
                'email': "email@test-user.com",
                'password': "test1234&",
                're_password': "test1234&"
            }
        ).register()
        self.assertFalse(res)
        self.assertEqual(
            msg[0], "First name or last name is too long (150 char max)")

    def test_first_name_last_name_is_too_short(self):
        res, msg, _ = CreateNewUser(
            {
                'first_name': "a",
                'last_name': "b",
                'email': "email@test-user.com",
                'password': "test1234&",
                're_password': "test1234&"
            }
        ).register()
        self.assertFalse(res)
        self.assertEqual(
            msg[0], "First name or Last name is too short (2 char min)")

    def test_user_register_success(self):
        c = Client()
        request = c.post(
            '/users/create-new-user/',
            {
                'first_name': "LocalTestUser123",
                'last_name': "LastNameTestUser123",
                'email': "email@test-user.com",
                'password': "test1234&",
                're_password': "test1234&"
            })

        self.assertRedirects(request, '/', status_code=302,
                             target_status_code=200, msg_prefix='',
                             fetch_redirect_response=True)

    def test_user_register_fail_messages(self):
        response = self.client.post(
            '/users/create-new-user/',
            data={
                'first_name': "LocalTestUser123",
                'last_name': "LastNameTestUser123",
                'email': "email@test-user.com",
                'password': "test",
                're_password': "test"
            }, follow=True)

        self.assertRedirects(response,
                             '/users/register/', status_code=302,
                             target_status_code=200, msg_prefix='',
                             fetch_redirect_response=True)

        messages = response.context['messages']

        for message in messages:
            self.assertEqual(message.level_tag, 'error')
            self.assertEqual(
                message.message, "Password must contain at least 8 characters")
